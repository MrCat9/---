from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set() #用于存放从网页中获取的新的urls
        links = soup.find_all('a', href = re.compile(r"/item/")) #从网页中获取所有的url
        for link in links:
            new_url = link['href'] #提取出网页中的不完整的url
            new_full_url = urllib.parse.urljoin(page_url, new_url) #补全url
            new_urls.add(new_full_url) #将补全后的url添加到urls中
        return new_urls #返回新的urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {} #用于存放数据
        
        #url
        res_data['url'] = page_url #保存这条数据的来源url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1') #用bs4找到标题
        res_data['title'] = title_node.get_text() #保存标题
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary') #用bs4找到简介
        if summary_node is None: #有些词条可能没有简介
            return
        res_data['summary'] = summary_node.get_text() #保存简介
        
        return res_data #返回保存的数据
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,"lxml",from_encoding='utf-8') #用bs4解析
        new_urls = self._get_new_urls(page_url, soup) #从网页中获取新的urls
        new_data = self._get_new_data(page_url, soup) #从网页中获取新的数据
        return new_urls, new_data #返回新的urls和数据
