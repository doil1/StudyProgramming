#!/usr/bin/env python
# coding: utf-8

# # 하노이의 탑
# 

# #### 3개의 기둥 중 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는다.
# 
# 
#    ## Rule
#    ### 1.한 번에 하나의 원판만 옮길 수 있다.
#    ### 2. 큰 원판이 작은 원판 위에 있어서는 안된다.

#    

#           

# ## Principal of Algorithm
# 
#    #### n개의 원반을 기둥으로 옮기려면,
#    #### 1.맨 아래를 제외한 원반들을 다른 기둥(other)으로 옮기고,
#    #### 2.맨 아래 원반을 목적지 기둥(to)으로 옮기고,
#    #### 3.다른 기둥에 옮겼던 원반들을 그 위에 얹는다.

# In[3]:



 
def Hanoi(n, start, destination, other):
 if n == 1:
     print(start, "->", destination)    ##1개의 원반일 때
     return
 Hanoi(n - 1, start, other, destination)     ##1.맨 아래를 제외한 원반들을 다른 기둥으로 옮기고,.
 print(start, "->", destination)             ##2.맨 아래 원반을 모적지 기둥으로 옮긴고,
 Hanoi(n - 1, other, destination, start)     ## 다른 기둥에 옮겼던 우너반들을 그 위에 얹는다.


# In[4]:


Hanoi(5,1,2,3)


# In[ ]:




