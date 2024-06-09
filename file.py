# data = input()
# number = 5 if data == "five" else 0
# print(number)
'''
for i in range(2,25,3):
    for l in range(1,i,2):
        print(l)
'''

# count = 0
# word = 'Hello World!!'
# for i in word:
#     if i == "l":
#         count +=1
# print('Count', count)

i = 5
while i<=16:
    print(i)
    i +=2

isHIScar = True
while isHIScar:
    if input("Enter data: ") == 'Stop':
        isHIScar = False