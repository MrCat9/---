class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding = 'utf-8')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1'>") #制成表格，启用边框
        
        for data in self.datas:
            fout.write("<tr>") #行
            fout.write("<td>%s</td>" % data['url']) #单元格内容
            fout.write("<td>%s</td>" % data['title']) #单元格内容
            fout.write("<td>%s</td>" % data['summary']) #单元格内容
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()        
    
    
