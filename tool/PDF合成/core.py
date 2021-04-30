"""
tkinter.filedialog.asksaveasfilename():选择  路径保存，返回 路径
tkinter.filedialog.asksaveasfile():选择 文件保存，创建文件并返回文件流对象
tkinter.filedialog.askopenfilename():选择 文件，返回 路径
tkinter.filedialog.askopenfile():选择 文件，返回IO流对象
tkinter.filedialog.askdirectory():选择目录，返回目录名
tkinter.filedialog.askopenfilenames():选择 多个文件，以元组形式返回多个 路径
tkinter.filedialog.askopenfiles():选择 多个文件，以列表形式返回多个IO流对象
"""
import tkinter
import tkinter.filedialog
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#创建窗口
root = tkinter.Tk()
#设置窗口的标题
root.title('PDF合成工具')
#定义窗口大小
root['height'] = 360
root['width'] = 360
#文件名关联变量
fileName = tkinter.StringVar()
fileName.set('')

#添加按钮及按钮点击事件处理函数
def addInformation():
  global pdf_fileName
  pdf_fileName = tkinter.filedialog.askopenfilenames()
  labelPage = tkinter.Label(root,text='选择了:{num}个文件'.format(num=len(pdf_fileName)),justify=tkinter.RIGHT)
  labelPage.place(x=120,y=15)
def outInformation():
  global outUrl
  outUrl = tkinter.filedialog.askdirectory()
def merageInformation():
  meragePdf()

buttonAdd = tkinter.Button(root,text='选择输入文件',command=addInformation)
buttonAdd.place(x=10,y=15,width=100,height=30)

buttonOut = tkinter.Button(root,text='选择输出文件的目录',command=outInformation)
buttonOut.place(x=10,y=65,width=120,height=30)

file_name = tkinter.Label(root,text='输出文件名',justify=tkinter.RIGHT)
file_name.place(x=10,y=100)

entryName = tkinter.Entry(root,width=30,textvariable=fileName)
entryName.place(x=80,y=100)

buttonmerage = tkinter.Button(root,text='开始合并',command=merageInformation)
buttonmerage.place(x=10,y=160,width=100,height=30)

# PDF合成处理函数
def meragePdf():
  #创建一个文件对象
  output = PdfFileWriter()
  outputPages = 0
  if pdf_fileName:
    for pdf_file in pdf_fileName:
        print("路径：%s"%pdf_file)

        # 读取源PDF文件
        input = PdfFileReader(open(pdf_file, "rb"))

        # 获得源PDF文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount

        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))

    labelPage = tkinter.Label(root,text='文件总页数:{outputPages}'.format(outputPages=outputPages),justify=tkinter.RIGHT)
    labelPage.place(x=10,y=120)
    # 打开要写入的文件对象
    outputStream = open(os.path.join(outUrl, entryName.get()+'.pdf'), "wb")
    #把PDF文件对象写入指定的文件对象中  正式生成PDF文件
    output.write(outputStream)
    outputStream.close()
    print("PDF文件合并完成！")
  else:
    print("没有可以合并的PDF文件！")


#消息循环 让窗口不断的刷新 并保持窗口不会处理完程序后就消失
root.mainloop()