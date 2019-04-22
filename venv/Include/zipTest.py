a=[1,2,3]
b=[4,5,6]
c=[7,8,9,10]
zip_a_b = zip(a,b)
print(zip_a_b)
zip_a_c = zip(a,c)
print(zip_a_c)
zip_b_c = zip(b,c)
print(zip_b_c)
print(zip(*zip_a_b))