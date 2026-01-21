file= open("test.txt")
#print(file.read(5)) #Read all the contents of the file and value passed is number of bites
#read one single line at a time and pointer goes to next line
#print(file.readline())
#print(file.readline())

#print line by line using readline
#line= file.readline()
#while line!="":
#    print(line)
#    line= file.readline()

#readlines stores the values in a list so that we can iterate
for line in file.readlines():
    print(line) 
file.close()