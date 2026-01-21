values= [1,2,"anshuman",4]#list data type which can hold any date type
names=["anshu","singh"]
hobbies=["singing","biking"]
print(values[0])

print(values[2])
print(values[-1]) #prints the last value of list

print(values[1:3])#prints exclusive of last index and inclsive of first

values.insert(3,'singh') #inserts at that position

values.append('end') # adds values at the end
print(values)

values[2]='ANSHUMAN'#UPDATING

del values[0]
print(values)

#Tuple same as list but its immutable where values cannot be changed

val=(1,2,"Anshuman",5.5)
print(val[1])

#val[2]="rahul"

print(val)

#dictionary they are key value pairs

dic= {"a":1, 4:"Hello", "b":"world"}
print(dic["b"])
print(dic[4])

#dictionary at runtime

dict={}

dict["a"]="hello"
dict["b"]="world"
print(dict)
print(dict["a"])