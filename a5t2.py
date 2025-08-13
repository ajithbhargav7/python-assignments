list1=list(range(1,10))
print("original list:",list1)
list2=[ ]
for i in range(5):
      list2.append(list1[i])
print("extracted list:",list2)  
list2.reverse()
print("reversed list:",list2)