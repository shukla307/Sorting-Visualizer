import time

def bubble_sort(data,drawDate,timeTrick):
    
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
            
                data[j],data[j+1]=data[j+1],data[j]
                drawDate(data,['yellow' if x==j or x==j+1 else "green" for x in range(len(data))])
                time.sleep(timeTrick)
    drawDate(data,['yellow' for x in range(len(data))])
