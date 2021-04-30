import tkinter
import tkinter.filedialog
import os
import xlwings as xw
import random


# 链接Excel表格 并指定不显示的打开excel 读取文件 默认是打开的
def client_excel():
  global app
  global wb 
  global sheet
  app=xw.App(visible=False,add_book=False)
  app.display_alerts=False
  app.screen_updating=False
  wb = app.books.open(file_url[0]) 
  sheet = wb.sheets[0]

  

  
  print('end')


#创建窗口
root = tkinter.Tk()
#设置窗口的标题
root.title('搅拌桩时间')
#定义窗口大小
root['height'] = 600
root['width'] = 360

counter  = 0


min_time_value = tkinter.StringVar()
min_time_value.set('1.25')

max_time_value = tkinter.StringVar()
max_time_value.set('1.35')

last_min_time_value = tkinter.StringVar()
last_min_time_value.set('1.63')

last_max_time_value = tkinter.StringVar()
last_max_time_value.set('1.68')

last_min_time_value1 = tkinter.StringVar()
last_min_time_value1.set('1.13')

last_max_time_value1 = tkinter.StringVar()
last_max_time_value1.set('1.18')

total_time_value = tkinter.StringVar()
total_time_value.set('98.87')

num_value = tkinter.StringVar()
num_value.set('19')

def addInformation():
  global file_url
  file_url = tkinter.filedialog.askopenfilenames()



buttonAdd = tkinter.Button(root,text='选择文件',command=addInformation)
buttonAdd.place(x=10,y=10,width=100,height=30)

min_time = tkinter.Label(root,text='时间最小值:',justify=tkinter.RIGHT)
min_time.place(x=10,y=60)

min_time_text = tkinter.Entry(root,width=6,textvariable=min_time_value)
min_time_text.place(x=80,y=60)

max_time = tkinter.Label(root,text='时间最大值:',justify=tkinter.RIGHT)
max_time.place(x=10,y=100)

max_time_text = tkinter.Entry(root,width=6,textvariable=max_time_value)
max_time_text.place(x=80,y=100)

last_min_time = tkinter.Label(root,text='最后一米下沉时间最小值:',justify=tkinter.RIGHT)
last_min_time.place(x=10,y=140)
last_mintime_text = tkinter.Entry(root,width=6,textvariable=last_min_time_value)
last_mintime_text.place(x=180,y=140)

last_max_time = tkinter.Label(root,text='最后一米下沉时间最大值:',justify=tkinter.RIGHT)
last_max_time.place(x=10,y=180)
last_max_text = tkinter.Entry(root,width=6,textvariable=last_max_time_value)
last_max_text.place(x=180,y=180)

last_min_time1 = tkinter.Label(root,text='最后一米提升时间最小值:',justify=tkinter.RIGHT)
last_min_time1.place(x=10,y=220)
last_min_text = tkinter.Entry(root,width=6,textvariable=last_min_time_value1)
last_min_text.place(x=180,y=220)

last_max_time1 = tkinter.Label(root,text='最后一米提升时间最大值:',justify=tkinter.RIGHT)
last_max_time1.place(x=10,y=260)
last_max_text = tkinter.Entry(root,width=6,textvariable=last_max_time_value1)
last_max_text.place(x=180,y=260)

total_time = tkinter.Label(root,text='合计时间:',justify=tkinter.RIGHT)
total_time.place(x=10,y=300)
total_time_text = tkinter.Entry(root,width=6,textvariable=total_time_value)
total_time_text.place(x=80,y=300)


num = tkinter.Label(root,text='条数:',justify=tkinter.RIGHT)
num.place(x=10,y=340)
num_text = tkinter.Entry(root,width=6,textvariable=num_value)
num_text.place(x=80,y=340)

def start():
  global min_value,max_value,last_down_min_value,last_down_max_value,last_up_min_value,last_up_max_value,total_value,num
  min_value = float(min_time_value.get())
  max_value = float(max_time_value.get())
  last_down_min_value = float(last_min_time_value.get())
  last_down_max_value = float(last_max_time_value.get())
  last_up_min_value = float(last_min_time_value1.get())
  last_up_max_value = float(last_max_time_value1.get())
  total_value = float(total_time_value.get())
  num = int(num_value.get())
  computers()

# 获取一个指定范围指定位数的时间随机数
def random_flow(arr,bit):
  return round(random.uniform(arr[0],arr[1]),bit)

def reset():
  min_time_value.set('')
  max_time_value.set('')
  last_min_time_value.set('')
  last_max_time_value.set('')
  last_min_time_value1.set('')
  last_max_time_value1.set('')
  total_time_value.set('')
  num_value.set('')


  

def computers():
  total_arr = []
  last_arr = []
  # print(min_value,max_value,last_down_min_value,last_down_max_value,last_up_min_value,last_up_max_value,total_value,num)
  index = num - 1
  for i in range(index):
    arr = []
    for j in range(4):
      arr.append(random_flow([min_value,max_value],2))
    total_arr.append(arr)
  for i in range(2):
    last_arr.append(random_flow([last_down_min_value,last_down_max_value],2))
    last_arr.append(random_flow([last_up_min_value,last_up_max_value],2))
  total_arr.append(last_arr)

  result = 0
  for i in total_arr:
    for j in range(4):
      result += i[j]
  if(result > total_value and result - total_value < 0.001):
    print(result)
    client_excel()
    write(total_arr)
    return 
  else:
    return computers() 

  # write(total_arr)
  # print(total_arr)

def write(total_arr):
  global counter
  arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ"]
  # print(total_arr)
  # print(len(total_arr))
  index1 = 0 
  for i in range(num):
    for j in range(4):
      index = str(j+counter+1)
      # print(index1)
      sheet.range(arr[index1] + index).value = total_arr[i][j]
      # print(arr[index1])
    index1 += 2
  counter += 6
  wb.save()
  wb.close()
  app.quit()
  app.kill()  # 有时quite退出不成功 就需要kill掉

button_start= tkinter.Button(root,text='开始',command=start)
button_start.place(x=10,y=360,width=100,height=30)

button_reset= tkinter.Button(root,text='重置',command=reset)
button_reset.place(x=120,y=360,width=100,height=30)

#消息循环 让窗口不断的刷新 并保持窗口不会处理完程序后就消失
root.mainloop()