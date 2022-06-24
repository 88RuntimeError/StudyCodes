import schedule
import time

q=0
def job():
    global q
    print('黎总，要努力奋斗赚钱，少玩游戏')
    q += 1

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    if q == 5:
        break
w=1
while w<10:
    print(w)
    w+=1