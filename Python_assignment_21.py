#Q-1 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# enter the starting range number
start_num = int(1500)
  
# enter the ending range number
end_num = int(2700)
  
# initialise counter with starting number
cnt = start_num
  
# check until end of the range is achieved
while cnt <= end_num:
    
    # if number divisible by 7 and 5
    if cnt % 7 == 0 and cnt % 5 == 0:
        print(cnt, " is divisible by 7 and 5.")
          
    # increment counter
    cnt += 1

#Q-2 Write a Python program that accepts a word from the user and reverse it.

# Python code to Reverse each word
# of a Sentence individually
  
# Function to Reverse words
def reverseWordSentence(Sentence):
  
    # Splitting the Sentence into list of words.
    words = Sentence.split(" ")
      
    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]
      
    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)
  
    return newSentence
  
# Driver's Code 
Sentence = "GeeksforGeeks is good to learn"
# Calling the reverseWordSentence 
# Function to get the newSentence
print(reverseWordSentence(Sentence))

#Q-3 Write a Python program to calculate a dog&#39;s age in dog&#39;s years.  Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

# importing required libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import datetime
import sys
  
# window class
class Window(QMainWindow):
    
    # Constructor 
    def __init__(self):
        super().__init__()
  
        # setting title of the window
        self.setWindowTitle("Python ")
  
        # width of the window
        self.w_width = 400
  
        # height of the window
        self.w_height = 400
  
        # setting geometry of the window
        self.setGeometry(100, 100, self.w_width, self.w_height)
  
        # method calling
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for components creation
    def UiComponents(self):
        # creating head label
        head = QLabel("Dog Age Calculator", self)
  
        head.setWordWrap(True)
  
        # setting geometry of the head
        head.setGeometry(0, 10, 400, 60)
  
        # font work 
        font = QFont('Times', 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
  
        # setting font to the head
        head.setFont(font)
  
        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
  
        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)
  
  
        # creating a label
        age_label = QLabel("Age of Dog ", self)
  
        # setting geometry to the label
        age_label.setGeometry(50, 120, 147, 40)
  
        # setting alignment
        age_label.setAlignment(Qt.AlignCenter)
  
        # setting stylesheet
        age_label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2px solid black;"
                                 "background : rgba(70, 70, 70, 35);"
                                 "}")
  
        age_label.setFont(QFont('Times', 9))
  
        # creating a spin box
        self.age = QSpinBox(self)
  
        # setting geometry to the spin box
        self.age.setGeometry(203, 120, 147, 40)
  
        # setting maximum value of spin box
        self.age.setMaximum(20)
  
        # setting minimum value of spin box
        self.age.setMinimum(1)
  
        # setting suffix to the spin box
        self.age.setSuffix(" year(s)")
  
        # setting font and alignment
        self.age.setFont(QFont('Times', 9))
        self.age.setAlignment(Qt.AlignCenter)
  
  
  
        # creating a push button
        calculate = QPushButton("Calculate Age", self)
  
        # setting geometry to the push button
        calculate.setGeometry(100, 200, 200, 40)
  
        # adding action to the button
        calculate.clicked.connect(self.calculate)
  
        # adding color effect to the push button
        color = QGraphicsColorizeEffect()
        color.setColor(Qt.blue)
        calculate.setGraphicsEffect(color)
  
  
        # creating a label to show result
        self.result = QLabel(self)
  
        # setting properties to result label
        self.result.setAlignment(Qt.AlignCenter)
  
        # setting geometry
        self.result.setGeometry(50, 280, 300, 70)
  
        # making it multi line
        self.result.setWordWrap(True)
  
        # setting stylesheet
        # adding border and background
        self.result.setStyleSheet("QLabel"
                                  "{"
                                  "border : 3px solid black;"
                                  "background : white;"
                                  "}")
  
        # setting font
        self.result.setFont(QFont('Arial', 11))
  
  
    # method for calculating the dog's age
    def calculate(self):
  
        # getting the spin box value
        value = self.age.value()
  
        # if value is 1
        if value == 1:
  
            # dog age is 15
            d_age = 15
  
        # if value is 2
        elif value == 2:
  
            # dog age is 24
            d_age = 24
  
        # else dog age get incremented by 4
        else:
            d_age = 24 + (value - 2) * 4
  
  
        # showing age through label
        self.result.setText("If your dog were a human, it would be : " +str(d_age) + " years old !")
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())

#Q-4 Write a Python program to check a triangle is equilateral, isosceles or scalene

# Python3 program for the above approach
 
# Function to check if the triangle
# is equilateral or isosceles or scalene
def checkTriangle(x, y, z):
 
    # _Check for equilateral triangle
    if x == y == z:
        print("Equilateral Triangle")
 
    # Check for isosceles triangle
    elif x == y or y == z or z == x:
        print("Isosceles Triangle")
 
    # Otherwise scalene triangle
    else:
        print("Scalene Triangle")
 
 
# Driver Code
 
# Given sides of triangle
x = 8
y = 7
z = 9
 
# Function Call
checkTriangle(x, y, z)

#Q-5 Write a Python program to detect the number of local variables declared in a function.
# Implementation of above approach
  
# A function containing 3 variables 
def fun():
    a = 1
    str = 'GeeksForGeeks'
  
  
# Driver program
print(fun.__code__.co_nlocals)

#Q-6 Write a Python program to execute a string containing Python code.

# Python program to illustrate use of exec to
# execute a given code as string.
 
# function illustrating how exec() functions.
def exec_code():
    LOC = """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
"""
    exec(LOC)
     
# Driver Code
exec_code()

#Q-7 Write a Python program to convert a given list of tuples to a list of  strings using map function.

# Python3 code to demonstrate
# convert list of tuples to list of list
# using list comprehension
  
# initializing list 
test_list = [(1, 2), (3, 4), (5, 6)]
  
# printing original list 
print("The original list of tuples : " + str(test_list))
  
# using list comprehension
# convert list of tuples to list of list
res = [list(ele) for ele in test_list]
  
# print result
print("The converted list of list : " + str(res))

#Q-8 Write a Python program to split a given dictionary of lists into list ofdictionaries using map function.

# Python3 code to demonstrate 
# to convert dictionary of list to 
# list of dictionaries
# using list comprehension
  
# initializing dictionary
test_dict = { "Rash" : [1, 3], "Manjeet" : [1, 4], "Akash" : [3, 4] }
  
# printing original dictionary
print ("The original dictionary is : " + str(test_dict))
  
# using list comprehension
# to convert dictionary of list to 
# list of dictionaries
res = [{key : value[i] for key, value in test_dict.items()}
         for i in range(2)]
  
# printing result
print ("The converted list of dictionaries " +  str(res))

#Q-9 Write a Python program to scan a specified directory and identify the sub directories and files.

import os
for dirpath, dirs, files in os.walk("./my_directory/"):  
            for filename in files:
                        fname = os.path.join(dirpath,filename)
                        with open(fname) as myfile:
                                    print(myfile.read())

#Q-10 Write a Python program to parse a string representing time and returnsthe structure time.

import time
time_string = "22 January, 2020"
print("String representing time:",time_string)
result = time.strptime(time_string, "%d %B, %Y")
print(result)
time_string = "30 Nov 00"
print("\nString representing time:",time_string)
result = time.strptime(time_string, "%d %b %y")
print(result)
time_string = '04/11/15 11:55:23'
print("\nString representing time:",time_string)
result = time.strptime(time_string, "%m/%d/%y %H:%M:%S")
print(result)
time_string = '12-11-2019'
print("\nString representing time:",time_string)
result = time.strptime(time_string, "%m-%d-%Y")
print(result)
time_string = '13::55::26'
print("\nString representing time:",time_string)
result = time.strptime(time_string, "%H::%M::%S")
print(result)

#Q-11. Write a Python code to send some sort of data in the URL&#39;s query string.

import requests
payload = {'key1': 'value1', 'key2': 'value2'}
print("Parameters: ",payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)
print("\nPass a list of items as a value:")
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
print("Parameters: ",payload)
r = requests.get('https://httpbin.org/get', params=payload)
print("Print the url to check the URL has been correctly encoded or not!")
print(r.url)

''' Q-12 Write a Python code to send a request to a web page, and print the
information of headers. Also parse these values and print key-value
pairs holding various information.'''

import requests
res = requests.get('https://www.google.com/')
print("Response text of https://google.com/:")
print(res.text)
print("\n==============================================================================")
print("\nContent of the said url:")
print(res.content)
print("\n==============================================================================")
print("\nRaw data of the said url:")
r = requests.get('https://api.github.com/events', stream = True)
print(r.raw)
print(r.raw.read(15))


#Q-13 Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.

import csv
csv_columns = ['id','Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)

#Q-14 Write a Python program that reads each row of a given csv file and skip
#the header of the file. Also print the number of rows and the field names.

import csv
fields = []
rows = []
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

#Q-15 Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))