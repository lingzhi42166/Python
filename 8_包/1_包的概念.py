""" 
  包就是存放很多模块的一个目录
  对于大型项目来说，一个项目会有很多模块，那么为了方便管理后期维护
  就指定了包这个方案，把所有的模块放在一起
  换言之 包是组织命名空间和类的重要方式

  怎么创建一个包: 
    创建一个__init__.py文件 表示这是一个包 该文件可以是空文件 
    __init.py的主要用途是设置__all__变量(*返回的对象)及初始化包的代码
    该文件是自动执行的

    如果我们想引入一个目录下面多个包的话 就可以利用__init__
    如果我们通过import引入的是一个目录 会报错 提示没有这个module
    那么我们想偷懒 不想挨个引入该目录下的多个包 那么就利用from import的方式引入
    


"""
# 绝对引入 
import package.cars.cars  # 把package/cars/cars.py 下的所有变量 都注册到package.cars.cars命名空间
package.cars.cars.addCar()

import package.cars.cars as addCarMethod # 注册到addCarMethod命名空间
addCarMethod.addCar()

from package.cars import *  # 引入package/cars/__init__.py 文件的变量__all__ 的所有成员  并注册到 当前全局命名空间中
cars.addCar()

# import package.car # No module named 'package.car'