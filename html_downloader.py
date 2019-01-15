from urllib.request import urlopen

class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urlopen(url)
        
        if response.getcode() != 200: #判断是否成功访问
            return None
        
        return response.read()
