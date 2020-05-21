'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''

'''
START HERE
'''

'''Write a File'''
#1) Create a file with Python that is named after your first and last name.  
#   Then write your first name on the first line with Python and your last name
#   on the second line with Python. 
#    
file1 = open("ashlieHewett.txt", "a")


string1 = "Ashlie"
string2 = "Hewett"
file1 = open("ashlieHewett.txt", "w")
file1.write(string1)
file1.write(string2)


#2) In the same file you just created describe one of the projects you created
#   with at least 5 lines and how you think you can improve.

#    

#3) Within 5 lines of the previous lines you've written on, describe what line 
#   you are on, on that line. Then close the file
#    
file1.close()

'''Read a file'''
#4) Open the previous file you created. Create an if statement that checks if
#   the mode is r. If the mode is r, create a variable named contents and set
#   the variable with .read() of the file you created. Print the contents of
#    the file. Close the file
file1 = open("ashlieHewett.txt", "r")
contents= file1.read()
print(contents)
file1.close()


#5) Open the same file you created. Create a variable that uses .readLines() of
# the file Create a for loop that prints each line in the file.
file1 = open("ashlieHewett.txt.", "r")
reading = file1.readLines()
for reading in file1:
    print(reading)
#6) Print the first, middle, and last line in the file.
file1 = open("ashlieHewett.txt", "r")
print(file1.readLine(1))

