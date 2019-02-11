#tipos primitivos
#int 5 , 8 , 15, 16 
#float 5.2 , 8.7 , -15.221 , 5.0
#bool True , False
#str 'olá' '7.5' 'car' 'machine'

n1 = str(input('Digite um valor '))
n2 = str(input('Digite segundo numero'))
s = n1 + n2
#print('a soma entre ', n1 ,'e' , n2, 'vale', s)

print('a soma entre {} e {} vale {}'.format(n1,n2, s))