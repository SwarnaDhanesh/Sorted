def Ascending(val):
    return val[1]
Value1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
secondvalue=0
for i in range(1,6):
 secondvalue=secondvalue+1
Value1.sort(key=Ascending)
print(Value1)