#write a function for sort a list
#input:list
#output:list

def sorted(x):
    for i in range(1, len(x)):
        while x[i-1] > x[i]:
            x.append(x[i-1])
            del x[i-1]
        else:
            continue
    return x
