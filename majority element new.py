
# coding: utf-8

# In[13]:


import numpy as np
import sys
flag=0
def merge_sort(sequence, master_length, count):
    global flag
    if len(sequence)==1:
        #print(sequence)
        return sequence
    else:
        partition= round(len(sequence)/2)
        sort_sequence1=merge_sort(sequence[:partition],master_length, count)
        sort_sequence2=merge_sort(sequence[partition:],master_length, count)
        sorted_array=[]
        #print(sort_sequence1)
        #print(sort_sequence2)
        flag1=0
        flag2=0
        if len(sort_sequence1)==1:
            flag1=1
        if len(sort_sequence2)==1:
            flag2=1
        while len(sort_sequence1)!=0 and len(sort_sequence2)!=0:
            #print('im here')
            #print(sort_sequence1)
            #print(sort_sequence2)
            #print(sort_sequence1[0])
            #print(sort_sequence2[0])
            if sort_sequence1[0]<=sort_sequence2[0]:
                sorted_array.append(sort_sequence1[0])
                
                #print(sorted_array)
                if flag1==1:
                    if sort_sequence1[0] in count:
                        count[sort_sequence1[0]]=count[sort_sequence1[0]]+1
                        #print(count)
                        if count[sort_sequence1[0]]>(master_length/2):
                            #print('im at 1')
                        
                            flag=1
                    else:
                        count[sort_sequence1[0]]=1
                        #print(count)
                sort_sequence1.pop(0)
            else:
                sorted_array.append(sort_sequence2[0])
                #print(sorted_array)
                if flag2==1:
                    if sort_sequence2[0] in count:
                        count[sort_sequence2[0]]=count[sort_sequence2[0]]+1
                        #print(count)
                        if count[sort_sequence2[0]]>(master_length/2):
                            #print('im at 2')
                            flag=1
                    else:
                        count[sort_sequence2[0]]=1
                        #print(count)
                sort_sequence2.pop(0)
        if len(sort_sequence1)!=0:
            if flag1==1:
                    if sort_sequence1[0] in count:
                        count[sort_sequence1[0]]=count[sort_sequence1[0]]+1
                        #print(count)
                        if count[sort_sequence1[0]]>(master_length/2):
                            #print('im at 1')
                        
                            flag=1
                    else:
                        count[sort_sequence1[0]]=1
                        #print(count)
            for i in sort_sequence1:
                sorted_array.append(i)
                
                
        elif len(sort_sequence2)!=0:
            if flag2==1:
                    if sort_sequence2[0] in count:
                        count[sort_sequence2[0]]=count[sort_sequence2[0]]+1
                        #print(count)
                        if count[sort_sequence2[0]]>(master_length/2):
                            #print('im at 2')
                            flag=1
                    else:
                        count[sort_sequence2[0]]=1
                        #print(count)
            for j in sort_sequence2:
                sorted_array.append(j)
                
        
        
        
    return sorted_array


    

def majority_element(sequence):
    global flag
    count=dict()
    master_length=len(sequence)
    sorted_seq=merge_sort(sequence, master_length,count)
    #print('flag')
    #print(flag)
    if flag==1:
            return 1
    return 0
            
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    print(majority_element(a))
    
    
    
        
        
    
    


# In[14]:




