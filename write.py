#by this way there is no need to close the file its handled
with open('test.txt','r') as reader:
    content=reader.readlines()
    reversed(content)#reverses the list
    with open('test.txt','w') as writer: #we write to file in write mode by default its in read mode
        for line in reversed(content):
            writer.write(line)

