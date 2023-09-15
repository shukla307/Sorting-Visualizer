import time

def insertion_sort(data,drawDate,timeTrick):
    for i in range(1,len(data)):
        k=data[i]
        j=i-1
        while(k<data[j] and j>-1):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=k
        drawDate(data,['red' if x==i or x==j else "green" for x in range(len(data))])
        time.sleep(timeTrick)
    drawDate(data,['red' for x in range(len(data))])
