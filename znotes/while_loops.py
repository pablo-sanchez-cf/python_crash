name = raw_input("Enter Name: ")
appetite = "hungry"
cookies = True
cookies_count = 10

while cookies == True:
    if appetite == "hungry" and cookies_count > 0:
        cookies_count -= 1
        print(name + " is " + appetite + " and ate a cookie and now there are " + str(cookies_count) + " left")
    else:
        appetite = "not hungry"
        cookies = False
        print(name + " is " + appetite + " anymore. He's full of cookies!")