# -*- coding:utf-8 -*-
"""
@outhor:Yangmengyu
@file: paiban1.0.py
@time: 2023/2/15 10:09
@desc:
"""
# 导入schedule模块
import schedule
# 导入datetime模块，它是一个提供日期和时间相关功能的标准库模块[^1^][1]
import datetime

# 定义一个类，用来表示班次
class Shift:
    # 定义一个初始化方法，用来设置班次的名称，开始时间，结束时间，绑定关系和排斥关系等属性
    def __init__(self, name, start_time, end_time, binds=None, excludes=None):
        # 使用self关键字来创建实例属性
        self.name = name # 班次的名称，例如"早班"，"晚班"等
        self.start_time = start_time # 班次的开始时间，使用datetime.time对象来表示
        self.end_time = end_time # 班次的结束时间，使用datetime.time对象来表示
        self.binds = binds # 班次的绑定关系，使用一个列表来表示，列表中的元素是其他的班次对象，表示这个班次必须和列表中的班次一起安排
        self.excludes = excludes # 班次的排斥关系，使用一个列表来表示，列表中的元素是其他的班次对象，表示这个班次不能和列表中的班次一起安排

    # 定义一个方法，用来返回班次的字符串表示，方便打印和调试
    def __str__(self):
        # 使用str.format方法来格式化字符串，使用{}占位符来表示要插入的变量，使用:来指定变量的格式，例如%I表示12小时制，%M表示分钟，%p表示上午或下午等[^2^][2]
        return "{}: {} - {}".format(self.name, self.start_time.strftime("%I:%M %p"), self.end_time.strftime("%I:%M %p"))

# 定义一个函数，用来模拟自动排班的逻辑
def auto_scheduling():
    # 这里可以写你的自动排班的代码，例如从数据库中读取员工信息，根据一些规则和算法来分配班次，然后将结果保存到数据库或者发送邮件等
    # 这里只是简单地打印一句话来表示函数被调用了
    print("Auto scheduling is running...")

# 使用schedule模块的every方法来创建一个调度器对象，然后使用do方法来指定要执行的函数
# 这里我们指定每隔一天执行一次auto_scheduling函数
schedule.every().day.do(auto_scheduling)

# 使用datetime.time方法来创建时间对象，传入小时，分钟，秒等参数[^1^][1]
# 创建一个早班对象，开始时间是8:00，结束时间是12:00
morning_shift = Shift("早班", datetime.time(8, 0, 0), datetime.time(12, 0, 0))
# 创建一个主班对象，开始时间是下午12：00，结束时间是下午14：30
main_shift = Shift("主班", datetime.time(12, 00, 0), datetime.time(14, 30, 0))
# 创建一个下午班对象，开始时间是下午2:30，结束时间是下午5:30
afternoon_shift = Shift("下午班", datetime.time(14, 30, 0), datetime.time(17, 30, 0))
# 创建一个休息班对象，开始时间是8:00，结束时间是17:30
rest_shift = Shift("休息班", datetime.time(8, 0, 0), datetime.time(17, 30, 0))
# 创建一个休息下午班对象，开始时间是12:00，结束时间是17:30
rest_afternoon_shift = Shift("休息下午班对象", datetime.time(12, 0, 0), datetime.time(17, 30, 0))
# 创建一个夜班对象，开始时间是下午17:30，结束时间是第二天早上八点
# 把datetime.time对象转换成datetime.datetime对象，再和datetime.timedelta对象相加
night_shift = Shift("夜班", datetime.time(17, 30, 0), datetime.datetime.combine(datetime.date.today(), datetime.time(8, 0, 0)) + datetime.timedelta(days=1))
# 创建一个周末上午班对象，开始时间是8点，结束时间是16点，绑定关系是休息班，排斥关系是晚班
weekend_morning_shift = Shift("周末上午班", datetime.time(8, 0, 0), datetime.time(12, 0, 0), binds=[rest_shift], excludes=[night_shift])
# 创建一个周末下午班对象，开始时间是14点30，结束时间是17点30，绑定关系是休息班，排斥关系是晚班
weekend_afternoon_shift = Shift("周末下午班", datetime.time(14, 30, 0), datetime.time(17, 30, 0), binds=[rest_shift], excludes=[night_shift])
# 创建一个节假日上午班对象，开始时间是8点，结束时间是12点，绑定关系是休息班，排斥关系是晚班
holiday_morning_shift = Shift("节假日上午班", datetime.time(8, 0, 0), datetime.time(12, 0, 0), binds=[rest_shift], excludes=[night_shift])
# 创建一个节假日下午班对象，开始时间是14点30，结束时间是17点30，绑定关系是休息班，排斥关系是晚班
holiday_afternoon_shift = Shift("节假日下午班", datetime.time(14, 30, 0), datetime.time(17, 30, 0), binds=[rest_shift], excludes=[night_shift])
# 创建一个列表，用来存储所有的班次对象
shifts = [morning_shift,main_shift, afternoon_shift, night_shift, rest_shift, rest_afternoon_shift,weekend_morning_shift, weekend_afternoon_shift,holiday_morning_shift,holiday_afternoon_shift]


# 打印所有的班次对象，使用for循环来遍历列表中的元素，使用print函数来打印元素
for shift in shifts:
    print(shift)