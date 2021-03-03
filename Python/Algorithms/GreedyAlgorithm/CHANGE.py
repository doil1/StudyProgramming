
"""
CHANGE
"""


n = 1260       #총 금액
cnt =0
coins = [500,100,50,10]     #거스름돈

for coin in coins:          # coins[0]~coins[4] 순서로 
    cnt += n//coin          # cnt증가
    n %=coin

print(cnt)