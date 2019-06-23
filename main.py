import requests
from lxml import etree
import json
url_root = 'https://hz.lianjia.com'

def get_page():
    url_region = []
    res = requests.get(url_root + '/ershoufang/rs/')
    res_page = etree.HTML(res.text)
    url_xpath = res_page.xpath('//*[@data-role="ershoufang"]/div/a/@href')
    name_xpath = res_page.xpath('//*[@data-role="ershoufang"]/div/a/text()')     #地区
    for i,j in zip(url_xpath,name_xpath):
        region = url_root + str(i)
        url_region.append([region,j])
    del url_region[8:11]
    return url_region
print(get_page())
def get_housing():
    Housing_information = []
    for i in get_page():
        res = requests.get(i[0])
        res_page = etree.HTML(res.text)
        url_page = res_page.xpath('//*[@class="contentBottom clear"]/div[2]/div/@page-data')
        page_num = json.loads(url_page[0])
        # page_num['totalPage']
        for j in range(1,int(page_num['totalPage'])+1):
            message = requests.get(i[0] + 'pg' +str(j))
            message_ht = etree.HTML(message.text)
            Community = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/a/text()')   #小区
            Apartment = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/text()')  # 户型
            apart = []
            price = []
            comm = []
            for q in Community:
                comm.append(i[1])
            for k in Apartment:
                a = k.split('|')[1].replace(' ', '')
                apart.append(a)
            Price = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[6]/div[1]/span/text()')   #价格
            # Unit = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[6]/div/text()')   #单价
            for p in Price:
                l = str(j) + '万'
                price.append(p)
            for c,x,h,r in zip(comm,Community, apart, price):
                Housing_information.append([c,x, h, r])
    return Housing_information
#测试代码
def test():
    Housing_information = []
    for i in get_page():
        message = requests.get(i[0])
        message_ht = etree.HTML(message.text)
        Community = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/a/text()')   #小区
        comm = []
        for q in Community:
            comm.append(i[1])
        Apartment = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/text()')   #户型
        apart = []
        for k in Apartment:
            a = k.split('|')[1].replace(' ', '')
            apart.append(a)
        Price = message_ht.xpath('//*[@class="sellListContent"]/li/div/div[6]/div[1]/span/text()')   #价格
        price = []
        for j in Price:
            p = str(j)+'万'
            price.append(p)

        for c,x,h,r in zip(comm,Community,apart,price):
            Housing_information.append([c,x,h,r])
    return Housing_information

print(test())