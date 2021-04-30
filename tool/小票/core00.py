import random

# # 首米喷量范围 1
# round(random.uniform(5.2,5.7), 1)
# # 第二米喷量范围 2 
# round(random.uniform(12,12.4), 1)
# # 中间喷量范围 3 ~8
# round(random.uniform(73.4,73.8), 1)
# # 末米喷量范围 9
# round(random.uniform(25,25.5), 1)

# # 首行时间范围一 前8个 1~8
# round(random.uniform(1.06,1.15), 2)
# # 首行时间范围一 第九个 9
# round(random.uniform(0.9,1), 2)
# # 第二行范围一 前8个 1~8
# round(random.uniform(3.37,3.5), 2)
# #第二行范围二 第九个 9
# round(random.uniform(1.2,1.27), 2)


testArr = [10.4,25.2,147.6,147.2,147.8,148,148.4,147.4,51.5]
totalFlow = 973.5
totalTime = 38.29




# 获取一个指定范围指定位数的时间随机数
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
def get_FlowInfo(totalFlow,totalArr):
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
    # round(testArr[index] - i, 1) 四舍五入并指定保留小数点
    second_flowArr.append(round(totalArr[index] - i, 1))
    result += second_flowArr[index] + i
    index += 1
  return {
    'first_flowArr' : first_flowArr ,
    'second_flowArr' : second_flowArr
  }


print(get_TimeInfo(38.29))
print(get_FlowInfo(totalFlow))
