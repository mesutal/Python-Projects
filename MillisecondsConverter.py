
#PROGRAM THAT CONVERTS MILLISECONDS TO HOURS, MİNUTES AND SECONDS

a = 0
while a == 0 :
    print("Welcome")
    millis = input ("Enter the millisecond value you want to convert: ")
    b= millis.isnumeric()
    if b == True :
        millis = int(millis)
        seconds=(millis/1000)%60
        seconds = int(seconds)
        minutes=(millis/(1000*60))%60
        minutes = int(minutes)
        hours=(millis/(1000*60*60))%24
        hours = int(hours)
        if ( millis == 0 ) :
            print("Not valid input!")
        else:

            if ( millis < 1000 ) :
                print("just {} millisecond/s".format(millis)) 

            elif ( seconds == 0 ) and ( hours == 0 ) :
                print("{} minute/s ".format(minutes))

            elif ( minutes == 0 ) and ( hours == 0 ) :
                print("{} second/s ".format(seconds))
            
            elif ( seconds == 0 ) and ( minutes == 0 ) :
                print("{} hour/s ".format(hours))

            elif ( seconds == 0 )  :
                print("{} hour/s {} minute/s ".format(hours,minutes))

            elif ( minutes == 0 ) :
                print("{} hour/s {} second/s ".format(hours,seconds))

            elif ( hours == 0 )  :
                print("{} minute/s {} second/ss ".format(minutes,seconds))

            else:
                print ("%d hour/s %d minute/s %d second/s" % (hours, minutes, seconds))

    elif b== False :
        millis = str(millis)
        millis = millis.title()
        if millis == "Exit" :
            print("Exiting the program...")
            a = 1
            break
        else:
            print("Not valid input!")