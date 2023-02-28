# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:00:41 2023

@author: Usuario
"""

print("hola mundo")

N = 1000
primos = []
sieve = [1] * N

i = 2;
while i * i < N:
    if sieve[i] == 1:
        for j in range(i + i, N, i):
            sieve[j] = 0
    i += 1
    
for i in range(2, N):
    if sieve[i] == 1:
        primos.append(i)
print(primos)
