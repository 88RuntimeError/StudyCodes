# _*_ coding:utf-8 _*_
# 开发时间：2022/6/20 下午9:25
# 功能：
import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
driver=webdriver.Chrome() #创建浏览器对象
class TrainSpider(object):
    #定义类属性
    login_url='https://kyfw.12306.cn/otn/resources/login.html' #登录的页面
    profile_url='https://kyfw.12306.cn/otn/view/index.html' #个人中心的网址
    leftTicket='https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc' #余票查询页面
    #定义init初始化方法
    def __init__(self,from_station,to_station,train_date):
        self.from_station=from_station
        self.to_station=to_station
        self.train_date=train_date
        self.station_code =self.init_station_code() #self.station_code结果为dict
    #定义登录方法
    def login(self):
        #打开登录的页面
        driver.get(self.login_url)
        WebDriverWait(driver,1000).until(
            ec.url_to_be(self.profile_url) #等待直到URL成为个人中心页面
        )
        print('登录成功')
    def init_station_code(self):#从爬取车站点代码excel中读取
        wb=openpyxl.load_workbook('stationCode.xlsx')
        ws=wb.active #使用活动表
        lst=[] #用于存储所有车站点名称及代号
        for row in ws.rows:#遍历所有行
            sub_lst=[]#用于存储每行中的车站名称及代号
            for cell in row:
                sub_lst.append(cell.value)
            lst.append(sub_lst)
        #print(dict(lst)) #将列表车化成字典
        return dict(lst)
    def search_ticket(self):
        driver.get(self.leftTicket) #请求url
        # 找到出发站到达站的 隐藏的HTML标签
        fromStation_input=driver.find_element(By.ID,'fromStation')
        toStation_input=driver.find_element(By.ID,'toStation')
        # 找到出发时间的的input标签
        train_date_input=driver.find_element(By.ID,'train_date')
        # 根据key获取value
        fromStationCode=self.station_code[self.from_station] #根据出发地找到出发地的代号
        toStationCode=self.station_code[self.to_station] #根据目的地找到目的地的代码
        # 执行js代码
        #我们要反取值放入隐藏的标签中
        driver.execute_script('arguments[0].value="%s"'%fromStationCode,fromStation_input)#fromStation_input的是放入value 的位置
        driver.execute_script('arguments[0].value="%s"'%toStationCode,toStation_input)
        driver.execute_script('arguments[0].value="%s"'%self.train_date,train_date_input)

        # 执行点击查询按钮，执行查询操作
        queryTicketTag=driver.find_element(By.ID,'query_ticket')
        queryTicketTag.click()# 执行单击事件

        # 解析车次，显示等待，等待tbody的出现
        WebDriverWait(driver,1000).until(
            ec.presence_of_element_located((By.XPATH,'//tbody[@id="queryLeftTable"]/tr'))
        )
        # 筛选出有数据的tr，去掉属性为 datatran 的tr
        trains=driver.find_elements(By.XPATH,'//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        #分别遍历每个车次
        for train in trains:
            print(train)
        


    #负责调用其它方法（组织其它代码）
    def run(self):
        #1.登录
        self.login()#执行登录方法
        #2.余票查询(编写方法把车站点代码读取）
        self.search_ticket()

#启动爬虫程序
def start():
    spider =TrainSpider('上海','成都','2022-06-27') #类的实例化
    spider.run()
    #spider.init_station_code()

if __name__ == '__main__':
    start()



