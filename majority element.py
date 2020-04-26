
# coding: utf-8

# In[121]:


import numpy as np
import sys
def merge_sort(sequence):
    if len(sequence)==1:
        return sequence
    else:
        partition= round(len(sequence)/2)
        sort_sequence1=merge_sort(sequence[:partition])
        sort_sequence2=merge_sort(sequence[partition:])
        sorted_array=[]
        while len(sort_sequence1)!=0 and len(sort_sequence2)!=0:
            #print(sort_sequence1)
            #print(sort_sequence2)
            #print(sort_sequence1[0])
            #print(sort_sequence2[0])
            if sort_sequence1[0]<=sort_sequence2[0]:
                sorted_array.append(sort_sequence1[0])
                sort_sequence1.pop(0)
                #print(sorted_array)
            else:
                sorted_array.append(sort_sequence2[0])
                sort_sequence2.pop(0)
                #print(sorted_array)
        if len(sort_sequence1)!=0:
            for i in sort_sequence1:
                sorted_array.append(i)
        elif len(sort_sequence2)!=0:
            for j in sort_sequence2:
                sorted_array.append(j)
        return sorted_array

def binary_search(sequence,low,high,element):#a is input sequence b is list of elements to search
        
            index=low+round((high-low)/2)
            #print(index)
            if sequence[index]==element:
                return index
            
            
                
            elif sequence[index]<element:
                if low==index:
                    return -1
                else:
                    low=index
                    return binary_search(sequence,low,high,element)
            
            else:
                if high==index:
                    return -1            
                else:
                    high=index
                    return binary_search(sequence,low,high,element)
                
                
def repetition_count(sequence,index):
    item=sequence[index]
    k=index+1
    flag=0
    count=1
    if k<len(sequence):
        while flag!=1:
            if sequence[k]==item:
                count=count+1
                if k== (len(sequence)-1):
                    break
                k=k+1
            else:
                flag=1
    
    flag=0
    j=index-1
    if j>0:
        while flag!=1:
            if sequence[j]==item:
                count=count+1
                if j==0:
                    break
                j=j-1
                
            else:
                flag=1
    
    return count 
        
            
    

def majority_element(sequence):
    sorted_seq=merge_sort(sequence)
    #print(sorted_seq)
    for i in range(len(sequence)):
        #index=binary_search(sorted_seq,0,len(sequence),i)
        #print('index, count')
        #print(index)
        count=repetition_count(sorted_seq,i)
        #print(count)
        if count>(len(sequence)/2):
            #print(i)
            return 1
    return 0
            
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    print(majority_element(a))
    
    
        
        
    
    


# In[123]:





# In[21]:




