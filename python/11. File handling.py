# File handling --> performing operations on files e.g. create, open, read, write and close
# Store data when program finishes, handle external files and process large files


# Opening a file --> open()
#file = open('filename.txt', 'mode')
#first argument (filename.txt) input our file name/path to be opened
#mode = what action do we want to open the file with (read, write, append)


# Closing a file --> .close()
#file = open('test123.txt', 'r')
#file.close()
# file has to be re-opened after closed, to read or write


# Checking file properties - when file is open you can check its properties
#O = open('test123.txt','w')
#print(f"Filename: {O.name}")        # returns filename
#print(f"Mode taken: {O.mode} ")     # tells what mode used (write in this case)
#print(f"Is it closed?: {O.closed}") # returns false because file is opened
#O.close()                           # we close the file
#print(f"Is it closed?: {O.closed}") # returns true because file is closed


# Reading a file ---> .read() which shows contents of the file
#A = open('rndom.py','r') 
#contents = A.read()  # this returns the contents as text, even if the content is code
#print(contents)
#A.close() # closing file after - good for saving the file + freeing up memory



# Writing a file ---> "w" mode, creates new file or overwrites existing file

# "with" makes sure to close the file automatically, "as" sets variable name for file
#with open('test123.txt','w') as random:        
# this writes in the the file (what "w" mode is) you cannot read contents in "write mode" and vice versa
   #random.write("Hello!")                      
   #random.write(" I just written my first file!")
# once finished, automatically closes the file + prints this output
#print("File is closed.")
# which here you can re-open and read this time
#with open('test123.txt','r') as random_2:
#    contents = random_2.read()
#    print(contents)


#with open("test123.txt","w+") as file:  # "w+" turns file blank --> allows us to read and write
    #file.write("New file! \n")
    #file.write("NEW ME!")
    
    #file.seek(0)            # .seek() counts a char = 1 byte, so starting at 0 -> we start at 0 char (first word)
    #contents = file.read()  # we can read this time due to "w+"
    #print(contents)

#print("File is closed")


#with open("test123.txt","a+") as file:          this case we are using "a+" which is append --> 
    #file.write("\nHere, we keep old contents \n")  Like I said here, keeps previous content but we can add on new
    #file.write("But we can write which adds new stuff")

    #file.seek(0)                   start from char 0 (first word)
    #contents = file.read()
    #print(contents)
#print("File is finished!")   


# if file not found --> python outputs "FileNotFoundError"
#try:
    #f = open('test123.txt','r')
#except FileNotFoundError:
    #print("This file is not found!")
