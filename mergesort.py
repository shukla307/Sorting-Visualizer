import time

def merge_sort(data,drawData,timeTick):
    merge_sort_algo(data, 0, len(data)-1,drawData,timeTick)

def merge_sort_algo(data, l, r,drawData,timeTick):
    if l < r:
        m = (l+r)//2

        merge_sort_algo(data, l, m,drawData,timeTick)
        merge_sort_algo(data, m+1, r,drawData,timeTick)
        merge(data, l,r, m,drawData,timeTick)

    
def merge(list1, left_index, right_index, middle,drawData,timeTick):
    drawData(list1,colorArray(len(list1),left_index, right_index, middle))
    time.sleep(timeTick)
        
    
    left_sublist = list1[left_index:middle + 1]  
    right_sublist = list1[middle+1:right_index+1]  
  
    # Initial values for variables that we use to keep  
    # track of where we are in each list1  
    left_sublist_index = 0  
    right_sublist_index = 0  
    sorted_index = left_index  



    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):  
  
        # If our left_sublist has the smaller element, put it in the sorted  
        # part and then move forward in left_sublist (by increasing the pointer)  
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:  
            list1[sorted_index] = left_sublist[left_sublist_index]  
            left_sublist_index = left_sublist_index + 1  
        # Otherwise add it into the right sublist  
        else:  
            list1[sorted_index] = right_sublist[right_sublist_index]  
            right_sublist_index = right_sublist_index + 1  
  
  
        # move forward in the sorted part  
        sorted_index = sorted_index + 1  
  
       
    # we will go through the remaining elements and add them  
    while left_sublist_index < len(left_sublist):  
        list1[sorted_index] = left_sublist[left_sublist_index]  
        left_sublist_index = left_sublist_index + 1  
        sorted_index = sorted_index + 1  
  
    while right_sublist_index < len(right_sublist):  
        list1[sorted_index] = right_sublist[right_sublist_index]  
        right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1 
         
    
    
    drawData(list1,["brown" if x>=left_index and x<=right_index else "green" for x in range(len(list1))])
    time.sleep(timeTick)
    

def colorArray(Length,left,middle,right):
    colorArray=[]
    for i in range(Length):
        if(i>=left and i<=right):
            if(i>=left and i<=middle):
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")
    return colorArray



























            
        
    

 
