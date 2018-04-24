import functools
def nested_sum():
        total = 0
        list_a=[1,[2,7],4,[5,3]]
        for i in list_a:
                if(isinstance(i,list)):
                        total = total + functools.reduce((lambda x,y: x+y) ,i)
                else:
                        total+=i
        print(total)
nested_sum()

