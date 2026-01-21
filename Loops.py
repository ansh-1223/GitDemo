greeting="Good morning"
# if else
if greeting=="Good morning":
    print("match")
else:
    print("not match")
print("loop over")

#for loop
values=[1,2,3,4,5,6,7,8,9]
for i in values:
    print(i*2)

sumall=0
for j in range (1,6):#range(i,j)-> i to j-1
    sumall=sumall+j
print(sumall)

print("*******************************************")

for k in range (1,10,5): #third argument is the addidtion value of k
    print(k)
print("********************************************")
for m in range(10): #only upper bound range starts from 0
    print(m)