""" 
  日志(log):
    概念:
      记录软件运行时所发生的事件
    作用:
      程序调试
      了解软件运行情况
      分析故障，问题定位
    如果应用的日志信息足够详细和丰富，还可以用来做用户行为分析，如：分析用户的操作行为、类型洗好、地域分布以及其它更多的信息，由此可以实现改进业务、提高商业利益。

    logging模块的日志级别(从上往下依次升高):
      DEBUG    调试问题                                                  10
      INFO     证明事情按预期工作                                          20   
      WARNING  表明发生意外 但程序正常工作 用于警告 （如，磁盘可用空间较低）      30
      ERROR    由于一个更严重的问题，软件已不能执行一些功能了                   40
      CRITICAL 严重错误，表明软件已不能继续运行了                             50    

        说明:
          如果指定了一个日志级别 那么应用程序只会记录大于等于该级别的日志  小于的会被丢弃
          logging模块默认的使30 也就是只记录WARNING及以上的日志
          可以通过logging.basicConfig方法调整

    
"""
import logging

print('1')

""" 记录日志的方式 """
logging.debug('debug')  # 创建一条DEBUG级别的日志记录
logging.info('INFO')        
logging.warning('warningTxt') # WARNING:root:warningTxt  日志级别：Logger名称：用户输出消息   root是默认的日志名称
logging.error('errorTxt')     # ERROR:root:errorTxt      日志级别：Logger名称：用户输出消息   root是默认的日志名称
logging.critical('critical')  # CRITICAL:root:critical


print('2')