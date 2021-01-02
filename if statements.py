def test(a, b, c):
  if a == b or b == c or c == a:
    return True
  else:
    return False

Answer = test(5,6,7)
print (Answer)

#Extra Credit

def Test(a,b,c):
  if a == b or b == int(c) or int(c) == a:
    return True
  else:
    return False

Result = Test(7,8,"8")
print(Result)