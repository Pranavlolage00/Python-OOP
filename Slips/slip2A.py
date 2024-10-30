#A) Write a Python function that accepts a string and calculate the number of upper case 
#letters and lower case letters. 
#Sample String: 'The quick Brown Fox'
#Expected Output: 
#No. of Upper case characters: 3
#No. of Lower case characters: 13
from tkinter import *

def accept():
    s1=input("Enter String:")
    uc=0
    lc=0
    for ch in s1:
        if ch.isupper():
            uc+=1
        if ch.islower():
            lc+=1
    print("UpperCase Count",uc)
    print("LowerCase Count",lc)
    return

accept()            
        
