def isPerfect(a):
    dummy=a
    summ=0
    for i in range(1,dummy//2+1):
        if dummy%i==0:
            summ+=i
    if summ==a:
        return True
    else:
        return False
if __name__=='__main__':
    ll=int(input('Enter lower limit='))
    up=int(input('Enter Upper limit='))
    for a in range(ll,up+1):
        if isPerfect(a):
            print(a,' ',end='')