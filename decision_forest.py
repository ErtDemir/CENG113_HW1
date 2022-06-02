#Student ID: 260201059
lstat = float(input("Enter % lower status of the population(lstat):"))
rm = float(input("Enter average number of rooms per dwelling(rm):"))
# Tree A
if lstat >= 9.7 :
    if lstat >= 20 :
        nox = float(input("Enter nitric oxides concentration (parts per 10 million)(nox):"))
        if nox >= 0.6 :
            a = 10
        else:
            a = 17
    else:
        a = 18
else:
    if rm < 6.9 :
        age = float(input("Enter proportion of owner-occupied units built prior to 1940(age):"))
        if age < 88 :
            if rm < 6.6:
                a = 23
            else:
                a = 28
        else:
            a = 36
    else:
        if rm < 7.4 :
            a = 34
        else:
            a = 45
# Tree B
if rm < 7.1 :
    if lstat >= 15 :
        if nox >= 0.6 :      #We question the definition of nox in these lines
            if lstat >= 20 : #
                b= 10        #
            else:            #
                b = 15       #
        elif nox < 0.6 :     #
            b = 18           #
        else:        
            nox = float(input("Enter nitric oxides concentration (parts per 10 million)(nox):"))
            if nox >= 0.6:
                if lstat >= 20 :
                    b = 10
                else:
                    b = 15
            else:
                b = 18
    else:
        if rm < 6.5 :
            if lstat >= 9.6:
                b = 21
            else:
                b = 24
        else:
            if lstat >= 4.9:
                b = 26
            else:
                b = 32
else:
    if rm < 7.4 :
        b = 33
    else:
        b = 46
#Tree C
if rm < 6.7 :
    if lstat >= 14 :
        crim = float(input("Enter per capita crime rate by town(crim):"))
        if crim >= 7 :
            c = 12
        else:
            c = 17
    else:
        if lstat >= 9.5 :
            c = 21
        else:
            rad = float(input("Enter index of accessibility to radial highways(rad):"))
            if rad < 7.5 :
                c = 24
            else:
                c = 34
else:
    if rm < 7.5 :
        if lstat >= 5.5 :
            ptratio = float(input("Enter pupil-teacher ratio by town(ptratio):"))
            if ptratio >= 19:
                c = 22
            else:
                c = 31
        else:
            c = 34
    else:
        c = 45
# Calculate
average = (a + b + c)/3
# Outputs
print("Decision Tree A :",a)
print("Decision Tree B :",b)
print("Decision Tree C :",c)
print("Average of Decision Forest :",average)