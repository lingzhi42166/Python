import tkinter
import tkinter.filedialog
import os
import xlwings as xw
import random

index = 0

# 链接Excel表格 并指定不显示的打开excel 读取文件 默认是打开的
def client_excel():
  global app
  global wb 
  global sheet
  app=xw.App(visible=False,add_book=False)
  app.display_alerts=False
  app.screen_updating=False
  wb = app.books.open(excel_Url) 
  sheet = wb.sheets[0]

def random_time(arr,bit):
  return round(random.uniform(arr[0],arr[1]),bit)
# 获取一个指定范围指定位数的喷量随机数
def random_flow(arr,bit):
  return round(random.uniform(arr[0],arr[1]),bit)


# 获取指定时间的一组时间数据
def get_TimeInfo(totalTime):
  first_timeArr = []
  second_timeArr = []
  result = 0
  
  for i in range(9):
    # 获取行第9个
    if i == 8:
      first = random_time([0.9,1],2)
      second = random_time([1.2,1.27],2)
      first_timeArr.append(first)
      second_timeArr.append(second)
      result += first + second
      break
    # 获取行前8个
    first = random_time([1.06,1.15],2)
    second = random_time([3.37,3.5],2)
    first_timeArr.append(first) 
    second_timeArr.append(second) 
    result += first + second
  if(result < totalTime or result > totalTime and result - totalTime > 0.001):
    return get_TimeInfo(totalTime)
  else:
    return {
      'first_timeArr' : first_timeArr,
      'second_timeArr' : second_timeArr
    }

# 获取指定喷量的一组时间数据
def get_FlowInfo(totalArr):
  first_flowArr = []
  second_flowArr = []
  index = 0
  result = 0
  
  first_flowArr.append(random_flow([5.2,5.7],1))
  first_flowArr.append(random_flow([12,12.4],1))
  for i in range(6):
    first_flowArr.append(random_flow([73.4,73.8],1))

  first_flowArr.append(random_flow([25,25.5],1))
  
  for i in first_flowArr:
    # round(totalArr[index] - i, 1) 四舍五入并指定保留小数点
    second_flowArr.append(round(totalArr[index] - i, 1))
    result += second_flowArr[index] + i
    index += 1
  return {
    'first_flowArr' : first_flowArr ,
    'second_flowArr' : second_flowArr
  }


#创建窗口
root = tkinter.Tk()
#设置窗口的标题
root.title('水泥搅拌桩生成器')
#定义窗口大小
root['height'] = 360
root['width'] = 360

#关联变量
model_flow1 = tkinter.StringVar()
model_flow1.set('')
model_flow2 = tkinter.StringVar()
model_flow2.set('')
model_flow3 = tkinter.StringVar()
model_flow3.set('')
model_flow4 = tkinter.StringVar()
model_flow4.set('')
model_flow5 = tkinter.StringVar()
model_flow5.set('')
model_flow6 = tkinter.StringVar()
model_flow6.set('')
model_flow7 = tkinter.StringVar()
model_flow7.set('')
model_flow8 = tkinter.StringVar()
model_flow8.set('')
model_flow9 = tkinter.StringVar()
model_flow9.set('')

model_time = tkinter.StringVar()
model_time.set('')







model_label = tkinter.Label(root,text='每米喷量值',justify=tkinter.RIGHT)
model_label.place(x=10,y=10)


flow1 = tkinter.Entry(root,width=6,textvariable=model_flow1)
flow1.place(x=16,y=36)

flow2 = tkinter.Entry(root,width=6,textvariable=model_flow2)
flow2.place(x=66,y=36)

flow3 = tkinter.Entry(root,width=6,textvariable=model_flow3)
flow3.place(x=116,y=36)

flow4 = tkinter.Entry(root,width=6,textvariable=model_flow4)
flow4.place(x=166,y=36)

flow5 = tkinter.Entry(root,width=6,textvariable=model_flow5)
flow5.place(x=216,y=36)

flow6 = tkinter.Entry(root,width=6,textvariable=model_flow6)
flow6.place(x=266,y=36)

flow7 = tkinter.Entry(root,width=6,textvariable=model_flow7)
flow7.place(x=16,y=66)

flow8 = tkinter.Entry(root,width=6,textvariable=model_flow8)
flow8.place(x=66,y=66)

flow9 = tkinter.Entry(root,width=6,textvariable=model_flow9)
flow9.place(x=116,y=66)


time = tkinter.Label(root,text='总时间',justify=tkinter.RIGHT)
time.place(x=10,y=96)

total_time = tkinter.Entry(root,width=6,textvariable=model_time)
total_time.place(x=16,y=122)

def addInformation():
  global excel_Url
  excel_Url = tkinter.filedialog.askopenfilenames()[0]
  print(excel_Url)


buttonAdd = tkinter.Button(root,text='选择文件',command=addInformation)
buttonAdd.place(x=10,y=160,width=100,height=30)


def merageInformation():
  global index 
  global total_time
  arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']
  
  # flowArr = [10.4,25.2,147.6,147.2,147.8,148,148.4,147.4,51.5]
  # total_time = 38.29

  flowArr = [flow1.get(),flow2.get(),flow3.get(),flow4.get(),flow5.get(),flow6.get(),flow7.get(),flow8.get(),flow9.get()]
  for i in range(9):
    flowArr[i] = float(flowArr[i])
  # print(flowArr)
  total_time = float(total_time.get())
  # print(total_time)
  allTime = get_TimeInfo(total_time)
  allFlow = get_FlowInfo(flowArr)
  # print(allTime)
  if(allTime and allFlow):
    print(allTime)
    client_excel()
    for z in range(2):
      index += 1
      j = str(index)
      timeRange_index = 0
      flowRange_index = 1
      for i in range(9):
        if(z==0):
          # print(arr[timeRange_index] + j )
          # print(arr[flowRange_index] + j)
          sheet.range(arr[timeRange_index] + j).value = allTime['first_timeArr'][i]
          sheet.range(arr[flowRange_index] + j).value = allFlow['first_flowArr'][i]
          timeRange_index +=2
          flowRange_index += 2
        else:
          # print(arr[timeRange_index] + j )
          # print(arr[flowRange_index] + j)
          sheet.range(arr[timeRange_index] + j).value = allTime['second_timeArr'][i]
          sheet.range(arr[flowRange_index] + j).value = allFlow['second_flowArr'][i]
          timeRange_index +=2
          flowRange_index += 2
    wb.save()
    wb.close()
    app.quit()
        


buttonmerage = tkinter.Button(root,text='开始',command=merageInformation)
buttonmerage.place(x=10,y=200,width=100,height=30)









#消息循环 让窗口不断的刷新 并保持窗口不会处理完程序后就消失
root.mainloop()