""" 
  日志默认是输出在控制台的
  那么既然为了维护和写日志的初衷  我们肯定希望日志是以文本文件的形式保存下来的

  还是通过logging.basicConfig()

"""
import logging

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(
  filename=r'.\9_调试\log.log',  # 用r''表示''内部的字符串默认不转义    用python3写文件的时候没有指定编码模式，其默认使用的是encoding=‘cp936’ 是GBK基础上开发的编码方式 所以微软的CP936通常被视为等同GBK 需要用GBK的方式读取文件
  level=logging.DEBUG,
  format=LOG_FORMAT,
  datefmt = DATE_FORMAT ,
)
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")

