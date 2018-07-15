# 输入输出
#age = input('enter your age:')
#print('age is:', age)
#print('Hi, id:%s, your age is:%d' % (str(2), int(age)))

#print('%2d-%02d' % (3, 1))
#print('%.2f' % 3.1415926)
#print('Hi, {0}, 收益为 {1:.1f}%'.format('gojay', 17.125))
#print(r'test\nte\'\'st')
#print('''line1
#line2
#line3''')
#print('9/3=',9/3)
#print('10//3=', 10//3)



"""
# 条件判断
age = input("enter age:")
if int(age) >= 18:
	print('adult:', age)
elif int(age) >=12:
	print('teenager:', age)
else:
	print('child:', age)

# 循环
# for...in
sum = 0
# for x in [1 , 2, 3]:
# 	sum += x
for x in range(101):
	sum += x
print(sum)

#while
sum = 0
n = 99
while n > 0:
	sum += n
	n = n - 2
print(sum)
"""


"""
# list: 有序
books = ['JAVA', 'PYTHON', 'PHP']
books.append('JS')
books.insert(1, 'AI')
books.pop() #删除末尾元素
books.pop(1) #删除第i元素
print(books)
print(len(books))
print(books[-1]) #倒数i元素
L = ['Apple', 123, True]
s = ['python', 'java', ['html', 'css'], L]
print(s)

# tuple: 不可变
t = (1, 2) 
t0 = ()
t1 = (1,)
t3 = ('a', 'b', ['A', 'B'])
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)
"""

# dictionary: 索引
books = {'java': 100, 'python': 90, 'php': 80}
books['asp'] = 70
print(books)
print(books['python'])
print('python' in books) #key是否存在
print(books.get('js', -1)) #key不存在返回-1
print(books.get('asp', -1))
books.pop('asp')