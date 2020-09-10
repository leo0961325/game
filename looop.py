for i in range (1,10) :
    for j in range(1,10) :
        print(i ,"x", j ,"=", i*j)




height = 5
stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('o' * stars)) #sum 5格
    stars += 2 #每層加兩個樹
print((' ' * height) + '|')