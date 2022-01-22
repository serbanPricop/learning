import re

# s = 'django'
# print(s[0],s[-1],s[:4],s[1:4],s[-1:-3],s[::-1])

# l = [3,7,[1,4,'hello']]
# l[2][2] = 'goodbye'
# print(l)

# d1 = {'simple_key':'hello'}
# d2 = {'k1':{'k2':'hello'}}
# d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# d1_value = d1['simple_key']
# d2_value = d2['k1']['k2']
# d3_value = d3['k1'][0]['nest_key'][1]
# print(d1_value,d2_value,d3_value)

# mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
# x=set(mylist)
# print(x)

# print("Hello my dog's name is {name} and he is {age} years old".format(name='Sammy',age=4))


# myPairs = [('a',2),('b',4),('c',6)]
# for tup1, tup2 in myPairs:
#     print(tup1+'1')

# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
#             return True
#     return False


# # arrayCheck([1, 1, 2, 3, 1])
# print(arrayCheck([1, 1, 2, 3, 1]))

# def stringBits(str):
#     return str[::2]

# print(stringBits('Hi'))

# def endOther(a,b):
#     a = a.lower()
#     b = b.lower()
#     return a[-len(b):] == b or b[-len(a):] == a

# print(endOther('Hiabcv', 'abcv'))

# def doubleChar(str):
#     result = ''
#     for i in range(len(str)):
#         result += str[i] * 2
#     return result

# print(doubleChar('Hi-There'))

# def fix_teen(num):
#     if((num in range(13,20)) and (num != 15) and (num != 16)):
#         return 0
#     return num

# def no_teen_sum(a,b,c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)

# print(no_teen_sum(2, 1, 14))

# def count_evens(nums):
#     count = 0
#     for item in nums:
#         if(item%2 == 0):
#             count +=1
#     return count

# print(count_evens([1, 3, 5])) 

paterns = ['term1','term2']

text = 'This is a text with term1'

for pattern in paterns:

    if re.search(pattern,text):
        match = re.search(pattern, text)
        print(match.end())
    else:
        print('No match')

print(id(text))


