#two ways to test true or flase
ItemsinCart=0
if ItemsinCart!=2:
    #raise Exception('Product cart count not matching')
    pass
assert(ItemsinCart==0)#assert always  takes only true conditions,for false it throws error

#if we don't want to fail the test then we use try and except
try:
    with open('file.txt','r') as reader:
        reader.readline()
except:
    print("Reached this block due to failure in try block")

#if we want to print the exact message from python when script fails we catch the exception
try:
    with open('file.txt','r') as reader:
        reader.readline()
except Exception as e:
    print(e)

#finally block execute with try block no matter test fails or pass
finally:
    print("cleaning up")