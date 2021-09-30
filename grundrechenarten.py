import random 

while(True):
    a=random.randint(1,10)
    b=random.randint(1,10)
    f=random.randint(1,4)
    print("a:",a)
    print("b:",b)
    print("f", f)
    
    if f == 1:
        op_name = "Addition"
        op = "+"
        r = a + b
        
    elif f == 2:
        op_name = "Subtraktion"
        op = "-"
        if a < b:
            a1 = a
            b1 = b
            r = b1 -a1 
            b = a1 
            a = b1
            
        else :
            r = a - b
           
    elif f == 3:
        op_name = "Multiplikation"
        op = "*"
        r = a * b
        
    else:
        op_name = "Division"
        op = "/"
        divisor = a
        dividend = a * b
        r = dividend / divisor
        a = dividend
        b = divisor
        
    while(True):
        res = int(input("Was ist das Ergebnis der " + op_name + " von : "+ str(a) + " "+op+" " + str(b)+" ?"))
        if res == r :
            print("Richtig")
            break 
        else: 
            print("Falsch")
