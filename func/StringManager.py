class StrManager:
  def InPut(strlo):
    input_value = strlo
    return input_value
  def Replacer(c,v,x):
    out = c.replace(c, v)
    return out
class IntManager:
  def InPut(c):
    try:
      ink = int(c)
      return ink
    except ValueError:
      print("Invalid input: Please provide a valid numeric string.")