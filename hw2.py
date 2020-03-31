def change_char(str):
  for i in range(len(str)):
    str1=str[0]
    if(str[i]==str1)and(i!=0):
      print('$',end='')
    else:
      print(str[i],end='')
    
change_char('circuit')