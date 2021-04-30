""" 
  书P217

"""
import pickle
# dumps 返回 对象二进制的字节形式
print(pickle.dumps([1,2,3]))#b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
