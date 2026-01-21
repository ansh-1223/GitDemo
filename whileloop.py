it = 10
while it>=1:
    if it==9:
        it=it-1
        continue #continue skips the current iteration and goes to next iteration 
    if it==3:
        break #it halts the loop and gets out
    print(it)
    it=it-1
