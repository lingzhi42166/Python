""" 
  py文件有两种运行方式
  一种是直接运行 
  一种是作为模块导入
  
  这两种方式运行 都会自动在全局作用域中 挂载一个 __name__属性
  如果是直接运行 那么__name__就自动设置为字符串__main__
  如果是作为模块导入时被运行的 就自动设置为模块名
"""
# __all__=['x','test']  # * 实际返回的是 __all__属性
x = 1
def test(x=x):
  x+=1
  print('test',x)
if(__name__=='__main__'):
  print('哈哈我是直接运行的')
elif(__name__=='testPage'):
  print('哈哈我是作为模块运行的')
  
print(__name__) # 如果是作为模块导入执行的 话 设为模块名testPage  如果是直接运行的话 就自动设置为字符串__main__