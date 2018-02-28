class UrlManager(object):
    def __init__(self): #初始化
        self.new_urls = set()
        self.old_urls = set()
            
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: #判断这个url既不是待爬取的url（new_urls），也不是已爬取的url（old_urls）
            self.new_urls.add(url) #那就把它添加到待爬取的urls

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url) #批量添加仍然调用单条添加的方法
        
    def has_new_url(self):
        return len(self.new_urls) != 0 #判断是否还有未爬取的url
    
    def get_new_url(self):
        new_url = self.new_urls.pop() #从未爬取的urls中取出一条url，并将该条url从urls中移除
        self.old_urls.add(new_url) #将该条url添加到已爬取的urls中
        return new_url
