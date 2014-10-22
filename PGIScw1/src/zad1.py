
def Fizz_buzz(n):
    for i in xrange(1,n+1):
        if i%3==0 and i%5!=0:
            print "Fizz,",
        elif i%5==0 and i%3!=0:
            print "Buzz,",
        elif i%5==0 and i%3==0:
            print "Fizz Buzz,",
        else:
            print str(i)+",",
Fizz_buzz(19)
