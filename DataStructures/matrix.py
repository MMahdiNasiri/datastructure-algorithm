from numpy import array, reshape, append, insert

a = array([['Ali', 18, 20], ['Shadi', 11, 18],
           ['Kazem', 15, 21], ['Karim', 11, 20],
           ['Zari', 18, 17]])

print(a.flatten())

m = reshape(a, (5, 3))
print(m)

b = append(a, [['Saleh', 12, 15]], 0)
print('b: ', b)

c = insert(b, 3, [4, 5, 6, 7, 8], axis=1)
print('c: ', c)

