import numpy
import random
import string
#----------------------------
capAlp=string.ascii_uppercase 
lowAlp=string.ascii_lowercase
signs=string.punctuation
numbers=string.digits
#----------------------------
def generate(leng,c,l,s,n): #this function creates the password depending on the user's desire. 
    if(c==True and l==False and s==False and n==False):
        gen=random.sample(capAlp,leng)
        passw="".join(gen)
    elif(s==True and l==False and n==False and c==False):
        gen=random.sample(signs,leng)
        passw="".join(gen)
    elif(n==True and s==False and l==False and c==False):
        gen=random.sample(numbers,leng)
        passw="".join(gen)
    elif(l==True and s==False and c==False and n==False):
        gen=random.sample(lowAlp,leng)
        passw="".join(gen)
    elif(c==True and l==True and s==False and n==False):
        joined=capAlp+lowAlp
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(c==True and s==True and n==False and l==False):
        joined=capAlp+signs
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(c==True and n==True and s==False and l==False):
        joined=capAlp+numbers
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(l==True and s==True and c==False and n==False):
        joined=lowAlp+signs
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(l==True and n==True and s==False and c==False):
        joined=lowAlp+numbers
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(s==True and n==True and l==False and c==False):
        joined=signs+numbers
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(c==True and l==True and s==True and n==False):
        joined=capAlp+lowAlp+signs
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(c==True and l==True and n==True and s==False):
        joined=capAlp+lowAlp+numbers
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(l==True and s==True and n==True and c==False):
        joined=lowAlp+signs+numbers
        gen=random.sample(joined,leng)
        passw="".join(gen)
    elif(c==True and l==True and s==True and n==True):
        joined=capAlp+lowAlp+numbers+signs
        gen=random.sample(joined,leng)
        passw="".join(gen)
        
    return passw
#----------------------------
c=False
lw=False
s=False
n=False
#----------------------------
print("Welcome to PasswordGen\n\n")
length=input("Length of the password that you desire: ")
l=int(length)
#----------------------------
cap=input("\nWill your password include capital letters: ")
low=input("\nWill your password include lowercase letters: ")
sign=input("\nWill your password include signs: ")
num=input("\nWill your password include numbers: ")
#----------------------------
cap.lower()
if(cap=="y" or cap=="yes"):
   c=True
#----------------------------
low.lower()
if(low=="y" or low=="yes"):
   lw=True
#----------------------------
sign.lower()
if(sign=="y" or sign=="yes"):
   s=True
#----------------------------   
num.lower()
if(num=="y" or num=="yes"):
   n=True
#----------------------------
result=generate(l,c,lw,s,n)
print(result)