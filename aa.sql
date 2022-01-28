
# Need to check assumption is input or output. 
#input:  what types of element could be in the list
# output: do we need to formate as integer or float or number of digits.

l = [1,2,None, '3',"\u0030",'-4']

cnt = 0
sumn = 0

for i in range(len(l)):
    if type(l[i])==int or type(l[i])==float or (type(l[i]) == str and l[i].isnumeric):
        cnt+=1
        sumn += int(l[i])
   
print (round(sumn/cnt,2))




#2. 给定一个Budget INT， 和 price_list 最多可以买几本书
budget = 30

price = [1,2,3,4]

#print(budget//min(price))

price = sorted(price)  # O（nlogn) quick sort
cnt = 0
total = 0

for i in range(len(price)):
    total +=price[i]
    if total <=budget:
        cnt +=1
    else:
        break
        #print(cnt)  # 这里不能直接return，因为会有corner case price总和低于budget
    
print(cnt)




#3. Book edition, 给定一个list
# ["PYTHON", "PYTHON 2ND EDITION", 'PY', 'PY 2ND', 'sql','sql 2.0'] 
# 返回所有 开头包含其他书的 book 这个就是["PYTHON 2ND EDITION"]

# 
book_name = ["PYTHON",  "PYTHON 2ND EDITION", "SQL", "SQL Tracie 2", "SQL_2"]

b = sorted(book_name) #nlog(n)

parent = b[0].lower()
result =[]
for i in range(1,len(b)):
    if b[i].lower().startswith(parent):
        result.append(b[i])
    else:
        parent = b[i].lower()

print(result)



# 4. Nth highest Price, return the book id （是hashmap，key时bookid，val是price吗？）
# given a dictionary, return the key-value with n_high‍‍‍‍‍‌‍‍‍‍‌‍‍‌‍‌est_value

d = {'abc':1, 'ad': 2.5, 'python': 12.5,'sql':7.5, 'java': 7.5}
n = 2

price_book = []
for k, v in d.items():
    price_book.append((v,k))

s = sorted(price_book, key = lambda x:(-x[0],x[1])) 
# when price equals and need to return the lower bookid alphabetically.

print(s[n-1][1])
