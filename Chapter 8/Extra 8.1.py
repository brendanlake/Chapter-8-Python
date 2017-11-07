alist = {}
for i in range (1,13):
    m = int(input('Enter Month #:'.format(i)))
    r = int(input('Enter Rainfall for said Month:'.format(i)))

    if m < 1 or m > 12:
        print('Enter a vaild month')
        break
    else:
        alist[r] = m
print('Rainfall')
for r,m in alist.items():
    print('Month: {}, Rain: {}'.format(m,r))

for r in alist:
    my_list = r
    my_list = [ int(r) for r in alist]
summ = (sum(my_list))
max_r = 0
for r in alist:
    if (r > max_r):
        max_r = r

min_r = 1
for r in alist:
    if (r < min_r):
        min_r = r
            

average = sum(my_list)/12
print('Total Rainfall:',summ)
print('Average Rainfall:',average)
print('Highest Rainfall:',max_r)
print('Lowest Rainfall:',min_r)
