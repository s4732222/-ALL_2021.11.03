import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


adress=[]
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016960")#漢口路(山西路~中清路間)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V440470")#德芳南路
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V028800")#經貿路
'''
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V115901")#市政路-環中路橋外慢車道(往北)
'''
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017100")#中清路一段/進化北路口(往北近端號誌桿)(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017140")#中清路一段/進化北路口(往南近端號誌桿)(往南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016940")#中清路一段(武昌路~漢口路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016700")#中清路二段(大連路~文心路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V015140")#中清路二段(文心路~大連路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003340")#中清路二段(經貿一路~大鵬路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V496200")#中清路二段(大鵬路~經貿一路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V040600")#中清路二段(經貿一路~敦化路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016100")#中清路二段、經貿七路(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016140")#中清路二段、經貿七路(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V094800")#中清路二段、黎明路三段(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016040")#中清路二段、經貿九路(向南)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014820")#臺灣大道何厝街大墩路(向東)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014922")#臺灣大道-惠中路-慢車道(往東)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053421")#臺灣大道-朝富路-慢車道(往東)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053420")#臺灣大道-朝富路-快車道(往東)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014960")#臺灣大道-惠中路-快車道(往西)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V021461")#臺灣大道-河南路-慢車道(往西)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014900")#臺灣大道-惠中路-(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V014940")#臺灣大道-惠中路-(往南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V021400")#臺灣大道-河南路-(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V021440")#臺灣大道-河南路-(往南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V053400")#臺灣大道-朝富路(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003461")#臺灣大道-黎明路(往西)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V495460")#五權西路二段-萬和路二段(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V058760")#五權西路-益豐路(往西)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V494820")#五權西路-龍富路(往東)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V116160")#五權西路-環中路(往東)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V091960")#環中路一段、松竹路三段(向西)
value=[]
#寫成i個陣列儲存
for i in range(len(adress)):
    data=[]
    html = urllib.request.urlopen(adress[i]).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

#下載關鍵字
    table = soup.find('table', {'class': 'table table-bordered table-striped table-hover table-condensed'})
    trs = table.find_all('tr')[1:]
    rows = list()

#用逗號分隔
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')])
    print(rows)

#判斷網址有幾筆車流，取該車流出來
    for i in range(len(rows)):
        data.append(rows[i][2])
    print('volume:',data)

#加總車流量
    sum=0
    for j in range(len(data)):
        sum = int(data[j])+sum
    print(sum)

#將車流量存成陣列
    value.append(sum)
    #print('全部車流量:', value)

#抓取陣列
a=value[5]
print('中清路一段/進化北路口(往北近端號誌桿)(往南):', a)
b=value[6]
print('中清路一段(武昌路~漢口路間)(向南):', b)
c=value[8]
print('中清路二段(文心路~大連路間)(向南):', c)
d=value[11]
print('中清路二段(經貿一路~大鵬路間)(向南):', d)
e=value[13]
print('中清路二段、經貿七路(向南):', e)
f=value[15]
print("中清路二段、經貿九路(向南):", f)
g=value[4]
print("中清路一段/進化北路口(往北近端號誌桿)(往北):", g)
h=value[7]
print("中清路二段(大連路~文心路間)(向北):", h)
i=value[10]
print("中清路二段(大鵬路~經貿一路間)(向北):", i)
j=value[11]
print("中清路二段(經貿一路~敦化路間)(向北):", j)
k=value[12]
print("中清路二段、經貿七路(向北):", k)
l=value[14]
print("中清路二段、黎明路三段(向北):", l)
m=value[16]
print("臺灣大道何厝街大墩路(向東):", m)
n=value[17]
print("臺灣大道-惠中路-慢車道(往東):", n)
o=value[18]
print("臺灣大道-朝富路-慢車道(往東):", o)
p=value[19]
print("臺灣大道-朝富路-快車道(往東):", p)
q=value[20]
print("臺灣大道-惠中路-快車道(往西):", q)
r=value[21]
print("臺灣大道-河南路-慢車道(往西):",r)
s=value[22]
print("臺灣大道-惠中路-(往北):", s)
u=value[23]
print("臺灣大道-惠中路-(往南):", u)
v=value[24]
print("臺灣大道-河南路-(往北):", v)
w=value[25]
print("臺灣大道-河南路-(往南):", w)
x=value[26]
print("臺灣大道-朝富路(往北):", x)
y=value[27]
print("臺灣大道-黎明路(往西):", y)
z=value[28]
print("臺灣大道-黎明路(往北):", z)
aa=value[29]
print("五權西路二段-萬和路二段(往北):", aa)
bb=value[30]
print("五權西路-益豐路(往西):", bb)
cc=value[31]
print("五權西路-龍富路(往東):", cc)
dd=value[32]
print("五權西路-環中路:", dd)
ee=value[33]
print("環中路一段、松竹路三段(向西):", ee)
   
    


#錯誤示範    
"""
    for i in range(len(rows)):
        if len(rows[i])<=1:
            data.append(rows[i][2])
        elif len(rows[i])>=2:
            data.append(rows[i][2])
    print(data)
"""