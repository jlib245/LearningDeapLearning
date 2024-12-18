import numpy as np

# AND Gate
def AND(x1, x2):
    # w : weight, theta : threshold (임계값)
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta :
        return 0
    elif tmp > theta :
        return 1

# AND Gate Overloading
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7 # replace from -(theta) to b
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1
    
# NAND Gate
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와는 w와 b만 다름
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

# OR Gate
def OR(x1, x2) :
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 # why -0.2..?
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

x = np.array([0, 1]) # input
w = np.array([0.5, 0.5]) # weight
b = -0.7 # bias

print(w*x)
print(np.sum(w*x)) 
print(np.sum(w*x) + b) 
print(AND(1, 1))