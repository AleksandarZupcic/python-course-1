def number_labeler(num):
    num = int(num)
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 2 == 0:
        print("even")
    else:
        print("odd")

while True:
    num = input("INSERT NUMBER: ")
    if num == 0:
        break
    elif num.isdigit():
        number_labeler(num)
    else:
        print("You didn't give a whole number, try again..")