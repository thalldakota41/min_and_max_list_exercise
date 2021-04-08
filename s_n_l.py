#Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
print words.replace('day', 'month')

#Min and Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1] 
z= []
z.append("hello")
z.append("world")
print z

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
list_one = x[:len(x)/2]
print list_one
list_two = x[len(x)/2:]
print list_two
list_two.insert(0, list_one)
print list_two