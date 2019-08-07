import requests,re
from bs4 import BeautifulSoup
path='F:\\1\\'
Mainurl="http://www.141ju.com/h0415/mp4list3/"
def getcontent(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        print('1')

def getnameAndPic(dic):
    print('开始下载图片')
    soup=BeautifulSoup(getcontent(Mainurl).text,'html.parser')
    for s in soup.find_all('a',attrs={'data-original':re.compile(r'.*')}):
        name=s.get('title')
        jpgurl=s.get('data-original')
        with open(path+'略缩图\\'+name+'.jpg','wb')as f:
            f.write(getcontent(jpgurl).content)
    return name

def getmp4():
    print('开始下载视频')
    soup = BeautifulSoup(getcontent(Mainurl).text, 'html.parser')
    i=0
    L=soup.find_all('a', attrs={'data-original': re.compile(r'.*')})#得到所有的后缀列表tag
    for s in L:
        name=s.get('title')
        i+=1
        print(str(i)+'/'+str(len(L)))#计数器
        newurl = 'http://www.141ju.com'+s.get('href')#得到单个页面的url
        soup2=BeautifulSoup(getcontent(newurl).text,'html.parser')#解析单个页面
        a=soup2.find_all('a',attrs={'href':'#'})[0]#找到下载链接
        with open(path+'视频\\'+name+'.mp4','wb')as f:#写入文件
            f.write(getcontent(a.text).content)
def main():
    dic={}
    name=getnameAndPic(dic)
    getmp4()
main()

