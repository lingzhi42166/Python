import tkinter
import tkinter.filedialog
import os
import xlwings as xw

# 链接Excel表格 并指定不显示的打开excel 读取文件 默认是打开的
def client_excel():
  
  app=xw.App(visible=False,add_book=False)
  app.display_alerts=False
  app.screen_updating=False
  print(file_url[0])
  wb = app.books.open(file_url[0]) 

  sheetName = int(sheet_name.get())
  sheet = wb.sheets[sheetName]
  row_text = row.get()
  start = int(column_start.get())
  end = int(column_end.get()) + 1
  for i in range(start,end):
    i = str(i)
    row_data = sheet.range(row_text+i).value
    row_data = round(row_data, 2)
    print(row_data)
    sheet.range(row_text+i).value = row_data
  over = tkinter.Label(root,text='完成',justify=tkinter.RIGHT)
  over.place(x=10,y=260)
  wb.save()
  wb.close()
  app.quit()



#创建窗口
root = tkinter.Tk()
#设置窗口的标题
root.title('水泥渗量')
#定义窗口大小
root['height'] = 360
root['width'] = 360
#关联变量
sheet_name = tkinter.StringVar()
sheet_name.set('')
row = tkinter.StringVar()
row.set('')
column_start = tkinter.StringVar()
column_start.set('')
column_end = tkinter.StringVar()
column_end.set('')


#添加按钮及按钮点击事件处理函数
def addInformation():
  global file_url
  file_url = tkinter.filedialog.askopenfilenames()
  


buttonAdd = tkinter.Button(root,text='选择文件',command=addInformation)
buttonAdd.place(x=10,y=10,width=100,height=30)

sheet_label = tkinter.Label(root,text='Sheet:',justify=tkinter.RIGHT)
sheet_label.place(x=10,y=60)

sheet_text = tkinter.Entry(root,width=6,textvariable=sheet_name)
sheet_text.place(x=80,y=60)

row_label = tkinter.Label(root,text='行:',justify=tkinter.RIGHT)
row_label.place(x=10,y=100)

row_text = tkinter.Entry(root,width=6,textvariable=row)
row_text.place(x=80,y=100)

column_label = tkinter.Label(root,text='开始列:',justify=tkinter.RIGHT)
column_label.place(x=10,y=140)

column_text = tkinter.Entry(root,width=6,textvariable=column_start)
column_text.place(x=80,y=140)

column1_label = tkinter.Label(root,text='结束列:',justify=tkinter.RIGHT)
column1_label.place(x=10,y=180)

column1_text = tkinter.Entry(root,width=6,textvariable=column_end)
column1_text.place(x=80,y=180)




start_Button = tkinter.Button(root,text='开始修改',command=client_excel)
start_Button.place(x=10,y=220,width=100,height=30)










#消息循环 让窗口不断的刷新 并保持窗口不会处理完程序后就消失
root.mainloop()