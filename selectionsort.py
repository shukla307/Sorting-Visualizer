import time

def selection_sort(data,drawDate,timeTrick):

    for i in range(len(data)):
        mini=i
        for j in range(i+1,len(data)):
            if(data[j]<data[mini]):
                mini=j
            drawDate(data,['pink' if x==j or x==i or x==mini else "green" for x in range(len(data))])
            time.sleep(timeTrick)
        data[i],data[mini]=data[mini],data[i]
        
    drawDate(data,['pink' for x in range(len(data))])
