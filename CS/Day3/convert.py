def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      # // = floordiv(a,b)
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))