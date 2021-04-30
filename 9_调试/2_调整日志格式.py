""" 
日志字段信息于日志格式:
  简单来讲就是怎么记录日志
  一条日志信息对应一个事件的发生 那么一个事件应该包含以下几个字段 (日志格式)
    事件发生时间
    事件发生位置
    事件的严重程度--日志级别
    事件内容    
  当然还可以包括一些其他信息，如进程ID、进程名称、线程ID、线程名称等

  默认的日志格式为   日志级别：Logger名称：用户输出消息

  logging模块提供了logging.basicConfig方法 配置日志格式和日志的级别(默认是WARNING)

  函数参数的具体说明 就不在这里写了 看博客
  https://www.cnblogs.com/Nicholas0707/p/9021672.html
"""

import logging

""" 调整日志格式和级别 """
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s %(name)s %(levelname)s %(message)s",
  datefmt = '%Y-%m-%d  %H:%M:%S %a'  
)
print('================')
logging.debug('debug') 
logging.info('INFO')        
logging.warning('warningTxt')
logging.error('errorTxt')    
logging.critical('critical') 