"""
다이나믹프로그래밍 연습(피보나치 수열)
"""
d = [0]*100

def fibonacci(x):
    if x == 1 or x==2:
        return 1
    if d[x]!= 0:
        return d[x]
    d[x] = fibonacci(x-1)+fibonacci(x-2)
    
    return d[x]

print(fibonacci(99))
