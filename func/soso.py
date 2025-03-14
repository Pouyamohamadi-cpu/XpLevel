import ctypes

class libsh:
  def setup(nxn):
    libshl = ctypes.CDLL(nxn)
    libshl.absvalue.restype = ctypes.c_int
    libshl.absvalue.argtypes = [ctypes.c_int]