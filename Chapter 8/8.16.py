my_list = list();

for i in range(0,4):
    x = float(input("Enter weight %d: "%(i+1)))
    my_list.append(x)

print ("Weights: ",my_list)

sum = 0.0
for i in range(0,4):
   sum = sum + my_list[i]

print ("Average weight: ",(sum/4.0))

max = my_list[0]
for i in range(1,4):
   if(max < my_list[i]):
       max = my_list[i]

print ("Max weight: ",max)

index = int(input("Enter a list index location(0 - 3) : "))
print ("Weight in pound :", my_list[index])
print ("Weight in kilogram : ", (my_list[index]/2.2))

my_list.sort()

print ("Sorted list: ", my_list)
