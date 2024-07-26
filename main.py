from array import *
def print_hi(name):

    print(f'Hi, {name}')
a1= array('f',[24,23,435,456,0,234,234])
print(type(a1))
print(sorted(a1))
print(a1[1])
for i in range(len(a1)):
    print(i,a1[i-1])
if __name__ == '__main__':
    print_hi('PyCharm')


