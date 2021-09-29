# Author: Yongdong Xi (Sep 28 2021)

a = int(input("How many scores does this team get"))
if a <= 8:
    print("this team earns nothing")
elif a <= 11:
    print("this team earns bronze medal")
elif a < 15:
    print("this team earns silver medal")
else:
    print("this team earns gold madel")
