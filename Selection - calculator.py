N1 = int(input("Please Enter First  Number: "))# lets you pick the numbers you want to calculate
N2 = int(input("Please Enter Second Number: "))
QQ = input("Please Enter The  Equation:")#pick out of + - * /

if QQ == "*":#this is what they get if they want to times the  numbers
  AA = N1*N2
  print("Answer:",AA)
elif QQ == "-":#this is what they get if they want to minus the  numbers
  AA = N1-N2
  print("Answer:",AA)
elif QQ == "/":#this is what they get if they want to divide the  numbers
  AA = N1/N2
  print("Answer:",AA)
elif QQ == "+":#this is what they get if they want to add the  numbers
  AA = N1+N2
  print("Answer:",AA)
else:
  print("Input error")#this is what they get if you did a wrong or invalid input
