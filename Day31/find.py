

def index_range(data, num):
    index = data.index(num)
    i = index - 1
    j = index + 1
    while i >= 0 and data[i] == num:
        i -= 1
    start = data.index(i)
    while j <= (len(data) -1 ) and data[j] == num:
        j += 1
    end = data.index(j)
    return '[%s - %s]' % (start+1, end-1)


data = [1, 2, 3, 3, 3, 4, 5]

res = index_range(data, 3)
print(res)

