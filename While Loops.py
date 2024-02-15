# While Loops
#python loop
# Python has two primitive loop commands:
# while loops
# for loops
#*The while loop
#Exmple:
i = 2
while i < 5:
    print(i)
    i += 1


#*The break statement
i = 1
while i < 6:
        print(i)
        if i == 3:
            break
        i +=1



#*The continue Statement
        i = 0
        while i < 6:
             i += 1
             if i == 3:
                  continue
             print(i)



#* The else statement
             # If the loop finished normally (without a break), then the code under the else statement is executed
             i = 1
             while i < 5:
                  print(i)
        else:
                  print("i is no longer than 6")



