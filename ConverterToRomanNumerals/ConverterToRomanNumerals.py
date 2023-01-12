
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


a = 0
while a == 0 :
    print("Welcome")
    inputx = input ("Enter the value you want to convert: ")
    b= inputx.isnumeric()
    if b == True :
        inputx=int(inputx)
        if (inputx >= 1) and (inputx <4000):
            roman = ''
            for i, r in num_map:
                while inputx >= i:
                    roman += r
                    inputx -= i
            print(roman)
        
        else:
            print("Not Valid Input!")

    elif b== False :
        inputx = str(inputx)
        inputx = inputx.title()
        if inputx == "Exit" :
            print("Exiting the program...")
            a = 1
            break
        else:
            print("Not valid input!")
    

