import xlwings as xw
import random
#指定不显示地打开Excel，读取Excel文件

# value = sheet.range('B2').value
# value = value.split(',')
# print(value)

# 链接Excel表格 并指定不显示的打开excel 读取文件 默认是打开的
def client_excel(fileName,sheetName):
  global app
  global wb 
  global sheet
  app = xw.App(visible=False, add_book=False)
  wb = app.books.open(fileName) 
  sheet = wb.sheets(sheetName)

def read_flow():
  global flowRange
  flowRange = {}
  for i in range(1,5):
    row = i + 1
    flowRange[i] = sheet.range('B%d' %row).value.split(',')
    flowRange.get(i)[0] = float(flowRange.get(i)[0])
    flowRange.get(i)[1] = float(flowRange.get(i)[1])

def read_time():
  global timeRange
  timeRange = {}
  for i in range(1,5):
    row = i + 6
    timeRange[i] = sheet.range('B%d' %row).value.split(',')
    timeRange.get(i)[0] = float(timeRange.get(i)[0])
    timeRange.get(i)[1] = float(timeRange.get(i)[1])


def random_time(data):
  result = 0
  range_time = []
  one_list = []
  two_list = []
  for i in range(9):
    one_list.append(round(random.uniform(timeRange[1][0], timeRange[1][1]), 2))
    two_list.append(round(random.uniform(timeRange[3][0], timeRange[3][1]), 2))
  one_list.append(round(random.uniform(timeRange[2][0], timeRange[2][1]), 2))
  two_list.append(round(random.uniform(timeRange[4][0], timeRange[4][1]), 2))
  print(one_list,two_list)
  for i in range(9):
    result += one_list[i]
    result += two_list[i]
  if data[9] - result > 0.00001 or result - data[9] > 0.00001:
    random_time(data)
    print(result)
  else:
    range_time.append(one_list)
    range_time.append(two_list)
    print(data[9],result)
    return range_time


def read_data():
  global data
  data = []
  line = ['A','B','C','D','E','F','G','H','I','J','K']
  for i in range(1):
    temporary_list = []
    for line in line:
      temporary_list.append(sheet.range(line + '12').value)
    data.append(temporary_list)

def count():
  key = True
  result = 0
  count = 0
  for i in data:
    randomTime_list = random_time(i)
  print(randomTime_list)


client_excel('test.xls','Sheet1')
read_flow()
read_time()
read_data()
count()
# print(flowRange)
# print(timeRange)
print(data)


# print(round(random.uniform(5.2, 5.7), 1))

