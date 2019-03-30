import random
import math
import time

'''
6 digit pin from 0 to 9 can be entered but 1st digit should not be 0, otherwise encryption goes wrong 
Speed is based on random prime chosen, bigger prime means slower. 
Whole encryption and decryption process takes 1min max, tested on computer with i7-8750H processor.
There are 60 primes in file, 60 choose 2 = 1770 possibilities
We can lower number of digits in pin if its too slow'''


def encrypt(message):
    '''takes message as a string, returns encrypted form followed by
     public key as a tuple (n,e) then private key d'''
    prime_list = []

    with open('prime_numbers.txt','r') as f:
        for line in f:
            prime_list.extend(map(int,line.split()))
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    while q == p:
        q = random.choice(prime_list)
    
    n = q*p
    totient = (q-1)*(p-1)
    e = 2
    
    while math.gcd(totient, e) != 1 and  0 < e < totient:
        e += 1
    print(str(p) +'im p')
    print(str(q) +'im q')
    print(str(n)+'im n')
    print(str(totient) +'im totient')
    print(str(e)+'im e')
    d = 1
    while 0 < d < totient and d * e % totient != 1:
        d += 1
    print(str(d)+'im d')
    c = power(int(message),e) % n
    print(str(c) + "im encrypted")
    return c, n, d

def decrypt(encrypted, public, private):
    decrypted = str(power(encrypted,private) % public)
    print(decrypted+'im decrypted')
    return decrypted

def power(num,exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        return power(num**2,exp/2)
    elif exp % 2 == 1:
        return num * power(num**2,(exp-1)/2)


if __name__ == '__main__':
    highest = 0
    for i in range(100):
        start = time.time()
        message = '123'
        c, n ,d = encrypt(message)
        enc = time.time()
        print("Encryption took " + str(enc-start) + 's')
        print('Answer: '+decrypt(c,n,d))
        end = time.time()
        print("This took " + str(end-start))
        if end-start > highest:
            highest=end-start
        print('Highest time:')
        print(highest)
