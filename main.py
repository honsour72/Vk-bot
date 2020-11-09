# CHANGES 3.0
import time
import bot_vk
import diff
morning_hour = 8
evening_hour = 19

waiting_time, plan = diff.difference(morning_hour, evening_hour)
print("До отправки сообщения осталось: ", str(waiting_time/60/60) + " часов " + "(" + str(waiting_time/60) + " минут" + ")")
print("Ожидание...")
time.sleep(waiting_time)
bot_vk.send_message()
print("Сообщение написано в " +str(time.localtime().tm_hour) + " часов, " + str(time.localtime().tm_min) + " минут")
print("Варимнт схемы:", plan)

if plan == "A":
    for i in range(30):    
        print("Ожидание: 11 часов (660 минут или 39600 секунд)")
        time.sleep(11*60*60) 
        bot_vk.send_message()
        print("Сообщение написано в " +str(time.localtime().tm_hour) + " часов, " + str(time.localtime().tm_min) + " минут")
        print("Ожидание: 13 часов (780 минут или 46800 секунд)")
        time.sleep(13*60*60) 
        bot_vk.send_message()
        print("Сообщение написано в " +str(time.localtime().tm_hour) + " часов, " + str(time.localtime().tm_min) + " минут")
    
if plan == "B":
    for i in range(30):    
        print("Ожидание: 13 часов (780 минут или 46800 секунд)")
        time.sleep(13*60*60) 
        bot_vk.send_message()
        print("Сообщение написано в " +str(time.localtime().tm_hour) + " часов, " + str(time.localtime().tm_min) + " минут")
        print("Ожидание: 11 часов (660 минут или 39600 секунд)")
        time.sleep(11*60*60) 
        bot_vk.send_message()
        print("Сообщение написано в " +str(time.localtime().tm_hour) + " часов, " + str(time.localtime().tm_min) + " минут")


    
