def set6():
  # SET 6
  day = input("Please provide a day of the week: ").lower()
  
  if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("It's a weekday")
  elif day == "saturday" or day == "sunday":
    print("It's the weekend")
  else:
    print("Invalid day entered")
  