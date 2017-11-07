def enter_rainfall():
    for month in months:
        rain = float(input('Enter the total rainfall for %s (in inches): ' % month))
        rainfall.append(rain)
def statistics():
    print('Total rainfall: %.1f inches' % sum(rainfall))
    print('Average monthly rainfall %.1f inches' % (sum(rainfall) / 12))
    print('%s had the most rainfall with %.1f inches.' % (months[rainfall.index(max(rainfall))], max(rainfall)))
    print('%s had the least rainfall with %.1f inches.' % (months[rainfall.index(min(rainfall))], min(rainfall)))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
months.extend(['August', 'September', 'October', 'Novermber', 'December'])
rainfall = []

enter_rainfall()
statistics()

