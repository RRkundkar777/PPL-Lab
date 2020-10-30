def DectoBin(a,p=False):       
    bin_a = 0;n = 0;copy_a = a # variable n is used to place the binary digits at their place, 
    while(a!=0):               # copy_a is used coz a modifies to 0 after the loop 
        bin_a+=(10**n)*(a%2)   # variable n is a power of ten which places the digits at correct place, you can also use typecasting
        a=a//2;n+=1            # for proper placing the % operator collects the remainders
    if(p==False):
        return bin_a           # the result is accordingly printed or returned
    else:
        print(f'The Binary equivalent of {copy_a} is {bin_a}')

def BintoDec(a,p=False):
    a = int(a) 
    copy_a = a; Dec_a = 0 ; n = 0 # the variable n is the power of 2 according to digit position RUN --> infoBintoDec() for more 
    while(not a==0):
        Dec_a+=(a%10)*(2**n)      # in this expression, the digits (and not remainders) of binary number are taken, multiplied  
        a = a//10; n+=1           # by suitable power of 2 and are added to our result simultaneously. RUN --> infoBintoDec() for more 
    if p==False:
        return Dec_a              # the result is accordingly returned or printed 
    else:
        print('The Decimal equivalent of {0} is {1}'.format(copy_a,Dec_a))

def add(num1,num2):
    return DectoBin(BintoDec(num1) + BintoDec(num2) ) 

def sub(num1,num2):
    return DectoBin(BintoDec(num1) - BintoDec(num2) ) 

def div(num1,num2):
    if(num1<num2 or BintoDec(num1)%BintoDec(num2) != 0):
            raise Exception("Cannot Find Binaries")
    else:
        return DectoBin(BintoDec(num1)//BintoDec(num2))

def mult(num1,num2):
    return DectoBin(BintoDec(num1) * BintoDec(num2) ) 

print("\nWelcome to Pyronite 1.0.0 BinCalc ")

print("""1.Add 2.Subtract 3.Muliply 4.Divide""")

try:
    onc = int(input("Enter an Operation number\n"))
    if(onc>4):
        raise IndexError("ERROR: Out of Bounds\n")
except Exception as e:
    print(e)

try:
    num1 = str(input("Enter first binary number\n"))
    for i in range(len(num1)):
        if(int(num1[i])>1):
            raise ValueError("ERROR: Entered number should contain only binary bits\n")
    if(len(num1)>8):
        raise BufferError("ERROR: Number is too large to be processed\n")
except Exception as e:
    print(e)


try:
    num2 = str(input("Enter second binary number\n"))
    for i in range(len(num2)):
        if(int(num2[i])>1):
            raise ValueError("ERROR: Entered number should contain only binary bits\n")
    if(len(num2)>8):
        raise BufferError("ERROR: Number is too large to be processed\n")
except Exception as e:
    print(e)


if(onc == 1):
    print(f"Addition of {num1} and {num2} is {add(num1,num2)}")
elif(onc == 2):
    print(f"Subtraction of {num1} and {num2} is {sub(num1,num2)}")
elif(onc == 3):
    print(f"Multiplication of {num1} and {num2} is {mult(num1,num2)}")   
elif(onc == 4):
    print(f"Division of {num1} and {num2} is {div(num1,num2)}")
else:
    raise IndexError("onc Out of Bounds\n")   


