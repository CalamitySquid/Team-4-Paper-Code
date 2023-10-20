def set9():
  # SET 9
  password = input("Please enter a password: ").lower()
  length = len(password)
  if length < 6:
    print("Password too short.")
  else:
    contains_digit = any(char.isdigit() for char in password)
    contains_letter = any(char.isalpha() for char in password)
  if contains_digit and contains_letter:
      print("Password is strong.")
  elif contains_digit:
      print("Weak password.")
  elif contains_letter:
      print("Moderate password.")