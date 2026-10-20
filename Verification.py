password="~Mamb!chwa~"
while True:
  entered_password=str(input("Enter your password: "))
  if entered_password==password:
    print("log in successful!!")
    break
  else:
    print("try again")