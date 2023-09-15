import time


def partition(array, head,tail,drawData,timeTick):
 
    border=head
    pivot=array[tail]
    drawData(array,colorArray(len(array),head,tail,border,border))
    time.sleep(timeTick)
    
    # compare each element with pivot
    for j in range(head,tail):
        if array[j] < pivot:
            drawData(array,colorArray(len(array),head,tail,border,j,True))
            time.sleep(timeTick)
            
            array[border], array[j] = array[j], array[border]
            border+=1
        drawData(array,colorArray(len(array),head,tail,border,j))
        time.sleep(timeTick)

    drawData(array,colorArray(len(array),head,tail,border,tail,True))
    time.sleep(timeTick)
    (array[border], array[tail]) = (array[tail], array[border])
 
    # Return the position from where partition is done
    return border
 
    # function to perform quicksort
 
 
def quick_sort(array, head,tail,drawData,timeTick):
    if head < tail:
        pi = partition(array, head,tail,drawData,timeTick)
        quick_sort(array, head, pi - 1,drawData,timeTick)
        quick_sort(array, pi + 1, tail,drawData,timeTick)
 
 


def colorArray(Length,head,tail,border,curIdx,isSwapping=False):
    colorArray=[]
    for i in range(Length):
        if(i>=head and i<=tail):
            colorArray.append("gray")
        else:
            colorArray.append("white")
        if i==tail:
            colorArray[i]=="orange"
        elif(i==border):
            colorArray[i]=="red"
        elif(i==curIdx):
            colorArray[i]=="yellow"

        if isSwapping:
            if i==border or i==curIdx:
                colorArray[i]=="gray"
    return colorArray


















            


    
 
