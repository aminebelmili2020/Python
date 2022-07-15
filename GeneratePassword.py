from lib2to3.pygram import Symbols
import random
import string

letters=string.ascii_letters
num='0123456789'
spe='-+*&!%$_./=_(*#@'
symbols=letters+num+spe
len=int(input("Enter Pass. length: "))
password="".join(random.sample(symbols, len))
print(password)