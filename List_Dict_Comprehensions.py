[num/2 for num in range (10) if num %2 ==0]#list comprehensions

[num /2 if num %2 == 0 else 0 for num in range(10)]

pos_neg={num: -num for num in range(9)}#dict
print(pos_neg)


# [OUTPUT for ITERATOR VARIABLE in ITERABLE ]

# [OUTPUT + CONDITIONAL ON OUTPUT for ITERATOR in ITERABLE + CONDITIONAL IN ITERABLE]1