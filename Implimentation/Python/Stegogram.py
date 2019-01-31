#python

from PIL import Image
import math
from scipy import stats
import numpy as np
import random

def chisqrcdf(x, n):
    return stats.chi2.cdf(x,n)

def fitness(A, colors):
    # VV Offset for different sectors.
    global pixels
    B = [pixels[i] for i in A]
    counts = np.zeros(colors)
    for h in range(len(B)):
        counts[B[h]] += 1
    hist = np.zeros((128,2))
    for n in range(colors//2):
        hist[n][0] = -1*counts[2*n]
        hist[n][1] = (counts[2*n] + counts[2*n - 1])/2
    k = colors//2
    m = 1
    while hist[m][1] < 5:
        hist[m+1] += hist[m]
        hist[m] = [1,-1]
#        print(hist[m],hist[m+1])
        m += 1
        k -= 1
    for l in range((colors//2)-k+1,colors//2):
        if hist[l][1] < 5:
            print(hist[l])
            hist[l] += hist[l - 1] # this looks wrong?
            print(hist[l])
            hist[l - 1] = [1, -1]
            k -= 1
#            print(hist[l - 1], hist[l], k)
    sum = 0 
    for q in range(colors//2):
        sum += ((hist[q][0] + hist[q][1])**2)/hist[q][1]
#        print(sum)
    return 1 - chisqrcdf(sum, k-1)

class Solution:

    def __init__(self, sol_size,colors):
        self.colors = colors
        self.sol_size = sol_size
        self.values = [[0] * sol_size] * 4
        self.fit_val = [0] * 4
        for i in range(4):
        # VV Change to shuffle
            for j in range(sol_size):
                a = random.randint(0,sol_size)
                if not a in self.values[i]:
                    self.values[i][j] = a
            self.fit_val[i] = fitness(self.values[i], colors)

    def __eq__(self, other):
        ret = 1
        for i in range(4):
            ret *= int(self.fit_val[i] == other.fit_val[i])
        return ret

    def mix_solutions(self, other):
        if self is other:
            return self
        print("stating mix")
        ret = Solution(self.sol_size, self.colors)
        for i in range(4):
            print("i : ", i)
            if self.fit_val[i] > other.fit_val[i]:
                best = self
                worst = other
            else :
                best = other
                worst = self
            k = 0
            for j in range(self.sol_size):
                if worst.values[i][j] in best.values[i]:
                    ret.values[i][k] = worst.values[i][j]
                    k += 1
            print("K0 = ",k)
            upper_lim = (self.sol_size - k)*(best.fit_val[i]/worst.fit_val[i])
            while k < upper_lim:
                for l in range(self.sol_size):
                    if not best.values[i][l] in ret.values[i]:
                        ret.values[i][k] = best.values[i][l]
                        k += 1
            print("K1 = ", k)
            l = 0
            while k < self.sol_size and l < len(worst.values[i]):
                if not worst.values[i][l] in ret.values[i]:
                    ret.values[i][k] = worst.values[i][l]
                    k += 1
                l += 1

            print("K2 = ", k)
            while k < self.sol_size:
                b = int(random.random() * self.sol_size)
                if not b in ret.values[i]:
                    ret.values[i][k] = b
                    k += 1
            print("K3 = ", k, self.sol_size)            
            a = int(random.random() * 400)
            if a  <  4:
                b = int(random.random() * self.sol_size)
                if not b in ret.values[i]:
                    ret.values[i][b - a] = b 

            ret.fit_val[i] = fitness(ret.values[i], self.colors)
            print(ret.fit_val[i])
        print("finished mix")
        return ret

if __name__ == '__main__':
    img = Image.open("stego06_0512.png")
    global pixels
    pixels = list(img.getdata()) # pixel values of the picture
    
    sideLength =  len(pixels)**.5 # side length of the image
    
    if sideLength != int(sideLength):
        raise Exception('THIS IS NOT A SQUARE, WHAT DO I DO WITH THIS??')
    
    colors = 256 # number of possible values a pixel can have
    
    sol_size = len(pixels)//8 # length of a solution

    solutions = [Solution(sol_size,colors) for x in range(100)]
    print("created base solutions")
    new_solutions = []
    print("mixing solutions")
    i = 0
    for sol1 in solutions:
        for sol2 in solutions:
            i += 1
            if i % 10 == 0:
                print(i)
            new_solutions.append(sol1.mix_solutions(sol2))
    new_solutions.sort(key=lambda x: sum(x.fit_val))
    print((new_solutions[0].fit_val), (new_solutions[-1].fit_val), new_solutions[0] == new_solutions[-1])
#    new_solutions = new_solutions[:9*len(new_solutions)//10]
    