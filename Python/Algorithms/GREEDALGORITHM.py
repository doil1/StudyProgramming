#!/usr/bin/env python
# coding: utf-8

# In[2]:



#coins = [10,20,21,40,50]
coins = [21,10,40,20,50]
coins.sort()
#print(coins)
result = []
total = 150
num = 5,
average = total//num
i =0
for coin in coins:
    if coin > average:
        result.append(average)
        continue
    else:
      # coin <average:
        total-=coin
        result.append(coin)
        i+=1
        continue
    average = total//(num-i)
print(result)


# In[ ]:





# In[ ]:




