print("Belarusian ruble and dollar exchanger on February 28")
EX=input("Please ebter the amount(such as 10P or 20$):")
if EX[-1] in ['P','p']:
    D=eval(EX[0,-1])/2.58
    print("The dollars you can get are{:.2f}D".format(D))
elif EX[-1] in ['$']:
    R=eval(EX[0,-1])*2.58
    print("The ruble you can get are{:.2f}R".format(R))
else
    print("Input error")