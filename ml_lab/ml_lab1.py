import pickle as pk
import array as arr
import time
import math
import random


print("MODULES IN PYTHON\n")
print("time module")
print("curr time: ",time.ctime(time.time()))
time.sleep(3)
print("slept for 3 seconds")
print("Math module")
print("pi: ",math.pi)
print("sin: ",math.sin(0))
print("FUNCTIONS IN PYTHON")
print("abs()",abs(-5))
d={41733001:"Abhigyan",41733002:"Guna Sekar",41733004:"Aditya Raj"}

print("len()",len(d))
print("type()",type(d))
#---------------------------------------
print("FILE HANDLING IN PYTHON")
file=open("poem.txt",'w')
file.write("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.""")
with open("poem.txt","r+") as file:
 print("readline(): ",file.readline())
 print("readlines(): ",file.readlines())
 print("write(): ",file.write("Sathyabama University"))
 print("writelines(): ",file.writelines(["BE CSE Data Science","BE CSE AI ML","BE EEE"]))
 file.seek(0)
 print(file.readlines())

with open("binary.dat","wb+") as file:
 print("dump(): ",d)
 pk.dump(d,file)
 file.seek(0)
 print("load(): ",pk.load(file))
 #-----------------------------------------------
 print("exception handling")
try:
 numerator = 10
 denominator = 0
 result = numerator/denominator
 print(result)
except:
 print("Error: Denominator cannot be 0.")

d={41733001:"Abhigyan",41733002:"Guna Sekar",41733004:"Aditya Raj"}
try:
 with open("binary1.dat","rb+") as file:
  print("dump(): ",d)
  pk.dump(d,file)
  print("executed successfully")
except:
  print("wrong mode enabled")
 # -------------------------------------------------
  print("INHERITANCE IN PYTHON")
class Person:
  def _init_(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()