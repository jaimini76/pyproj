def fibonacci(n):

    # list to store fibonacci
    l=[]

    if n < 0:
        print("Negative values not supportred.")
        return l
    elif n == 0:
        l.append(0)
        return l
    elif n == 1:
        l.append(0)
        l.append(1)
        return l
    else:
        l.append(0)
        l.append(1)
        i=2
        j=0
        while j <= n:
            fib_num = l[i-1] + l[i-2]
            l.append(fib_num)
            j = fib_num
            i += 1
        return l

arr =  fibonacci(4)

print(f"arr = {arr}")


#def fibonacci(n):

#i = 2
#l = []
#l.add(0)
#l.add(1)
#j = 0
#While j <= N:
#	 X = l[i-1]) +l[i-2]
#	 l.add(x)
#	J = x


