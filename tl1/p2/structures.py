from ctypes import *

class payload_X(Structure):
    _fields_ = [("token", c_long),
                ("operation", c_int),
                ("data", c_long)]
