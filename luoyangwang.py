import requests,threading,re
from multiprocessing import Process
from bs4 import BeautifulSoup as bs
import threadpool
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#url="https://people.lyd.com.cn/duihuabumen/26_ruyangxian/"
#urls=["/duihuabumen/15_jianxiqu/", "/duihuabumen/16_xigongqu/", "/duihuabumen/17_laochengqu/", "/duihuabumen/18_chanhehuizuqu/", "/duihuabumen/19_luolongqu/", "/duihuabumen/20_jiliqu/", "/duihuabumen/21_yanshishi/", "/duihuabumen/22_xinanxian/", "/duihuabumen/23_yichuanxian/", "/duihuabumen/24_mengjinxian/", "/duihuabumen/25_luoningxian/",  "/duihuabumen/27_luanchuanxian/", "/duihuabumen/28_yiyangxian/", "/duihuabumen/29_songxian/", "/duihuabumen/59_longmenyuanquguanweihui/", "/duihuabumen/108_gaoxinqu/", "/duihuabumen/115_yibinqu/"]
urls=["/duihuabumen/20_jiliqu/"]
header={'Referer': 'https://people.lyd.com.cn/duihuabumen/26_ruyangxian/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
def text(txt="ruyangwang",title="空",desc=None):
    txt=txt.replace("/","")
    with open("./lyddata/"+txt+".txt","a+") as fp:
        if desc:
            fp.write(title+"\n"+desc+"\n---------------------\n")
        else:
            fp.write(title+"\n")
def geturl(url,count=0):
    print("开始采集:"+url)
    con = requests.get(url,verify=False,headers=header)
    con.encoding=con.apparent_encoding
    if con.status_code==200:
        soup=bs(con.text,'html.parser')

        #try:
        pagecount=soup.select("h6.blue18cu")
        if len(pagecount)!=0:
            if count!=1:
                for source in pagecount:
                    title = source.span.a.text
                    desc = "https://people.lyd.com.cn" + source.span.a['href']
                    text(url[38:47],title, desc)
                    text(url[38:47]+"title", title)
                    print("采集完成:" + url)
            else:
                pagenum=soup.select("span.hui14 strong")[0].text
                return pagenum
        else:
            newurl=re.search(r"wscckey=(.*)';",con.text).group(1)
            geturl(url+"?wscckey="+newurl,count)
        '''
        except:
            print("采集出错")
            pass'''
    else:
        print("响应码错误:"+str(con.status_code))
        geturl(url,count)


if __name__ == '__main__':
    #text("ruyangwang", "第n页url:  " + url + "1")
    def xianurl(url,count=10):
        codes=[]
        #print(type(int(count)))
        #exit()
        count=int(count)
        for code in list(range(1,count)):
            codes.append(url+str(code))
        pool = threadpool.ThreadPool(10)
        tasks = threadpool.makeRequests(geturl, codes)
        [pool.putRequest(task) for task in tasks]
        pool.wait()
    for url in urls:
        count=geturl("https://people.lyd.com.cn"+url,count=1)
        xianurl("https://people.lyd.com.cn"+url,count)
    '''
    for i in range(1,227):
        #t=Process(target=geturl,args=(url+str(i),))
        #t.start()#多进程
        #t2=threading.Thread(target=geturl,args=(url+str(i),))
        #t2.start()
        #t2.join()
        if i==226:
            print("共收集2257条信息:")
            exit()'''





