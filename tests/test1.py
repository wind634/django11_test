from django.db import connection


x = [1, 2, 3]

y = [4, 5, 6]
#
# z = [7, 8, 9]

xyz = zip(x, y)
# print(list(xyz))
print(dict(xyz))
