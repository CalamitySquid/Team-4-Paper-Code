def set3():
  # SET 3
  age = int(input("Please state your age: "))
  
  if age < 5:
    print("Your ticket is free!")
  elif 5<=age and age <=12:
    print("Your ticket is $8")
  
  elif 13<=age and age <=59:
    print("Your ticket is $12")
  
  elif age >= 60:
    print("Your ticket is $10")
  