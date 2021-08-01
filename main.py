import random
import datetime
import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
'''随机生成各时间段航班数（6点到7点和21点到22点航班数较少）'''
x_value = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y_value = [13,20,20,20,20,20,20,20,20,20,20,20,20,20,20,7]
for value in range(0,15):
    tmp = random.randint(1,5)
    y_value[value] = y_value[value] - tmp
    y_value[value + 1] = y_value[value + 1] + tmp

'''结合之前随机生成的各时间段航班数随机生成一天内航班时刻表'''
listtime = []
def randomtimes(start, end, n, frmt="%H:%M:%S"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime=[random.random() * (etime - stime) + stime for _ in range(n)]
    time_str=[t.strftime(frmt) for t in time_datetime]
    listtime.append(time_str)
xtime = []
for i in range(0,17):
    xtime.append(f"{x_value[i]}:00:00")
for i in range(0,16):
    randomtimes(xtime[i],xtime[i+1],y_value[i])
print(y_value)
print('\n')
for i in range(0,16):
    print(listtime[i])
print('\n')
detime = []
for i in range(0,16):
    detime.append([])
    for j in range(0,y_value[i]):
        rantime1 = random.randint(0, min(4, 15 - i))
        rantime2 = random.randint(0,y_value[i+rantime1]-1)
        detime[i].append(listtime[i+rantime1][rantime2])

'''绘制Sample Request Schedule'''
for i in range(0,16):
    print(detime[i])
plt.title('Sample Request Schedule')
plt.xlabel('time')
plt.ylabel('number')
for i in range(0,16):
    for j in range(0,y_value[i]):
        input_values = [listtime[i][j],detime[i][j]]
        number = [300-i*j,300-i*j]
        plt.plot(input_values,number,linewidth = 1)
plt.show()

'''绘制flights per hour'''
data = [Bar(x = x_value, y = y_value)]
x_axis_config = {'title':'time'}
y_axis_config = {'title':'number of flight'}
my_layout = Layout(title = 'flights per hour', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='e:/pythonProject5/pic')