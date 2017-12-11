

def look(data, num):
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data) - i - 1):
            if data[i] + data[j] == num:
                return (i,j)






data = [1,3, 1, 2, 2, 3]
res = look(data, 3)
print(res)