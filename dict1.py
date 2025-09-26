def return_sum(myDict):
  values = []
  for i in myDict:
        values.append(myDict[i])
  final = sum(values)
  return final
# Driver fuction
my_dict={'a' : 100, 'b' : 200, 'c' : 300}
print('sum:', return_sum(my_dict))
