num=int(input('Enter a number:'))
if num%2==0:
    rev=0
    temp=num
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
        if(rev==temp):
            print('The given number is a palindrome')
        else:
            print('The given number is not a palindrome')
else:
    def fact(num):
        if num==1:
            return num
        else:
            return num*fact(num-1)
    print('The factorial of',num,'is',fact(num))
    count=0
    n=fact(num)
    while(n>0):
        n=n//10
        count=count+1
        print('The number of digits is the factorial of a number is',count)