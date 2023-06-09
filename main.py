from cmath import sqrt
import sys 
import math

def F(n):
    return (((1+sqrt(5))/2)**(n)-((1-sqrt(5))/2)**(n))/(sqrt(5))

for i in range(int(sys.argv[1])):
    print(F(i))
