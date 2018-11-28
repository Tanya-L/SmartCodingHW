# Question 1
# Design a function within a Python script that takes in a
# list of numbers, for example [1,2,3,4,5] and returns another
# list with each number multiplied
# by 2.
# One possible idea/solution looks like:
#            def multiply_by_two(a_list):
#                values_to_return = []
#                # put your code and logic here
#                return values_to_return
# Running your code:
# If you want to try out answers, you can print (in the same file), example:
#            x = [1,3,5]
#            print(multiply_by_two(x))


def times2(x):
    return x * 2


def multiply_by_two1(y):
    return list(map(times2, y))


def multiply_by_two2(y):
    return [i * 2 for i in y]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# test
print(multiply_by_two1(a))
print(multiply_by_two2(a))
