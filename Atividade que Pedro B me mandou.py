def factorial(n):
    j = 1
    while n>1:
        j*=n
        n-=1
    return j
def perm(n, args):
    res = factorial(n)
    for i in args:
        res/=factorial(i)
    return res
def inicio():
    n = int(input('Qual o número de elementos? '))
    p = map(int,input('Digite o número de elementos repetidos, em uma linha apenas, separados por espaço. \n Por exemplo: 1 2 5 7 \n ').split())
    print(perm(n,p))
inicio()


A = [1,2,3,4]
A = map(lambda x: x*2, A)
for i in A:
print(A)

# w3schools.com/python/python_lambda.asp