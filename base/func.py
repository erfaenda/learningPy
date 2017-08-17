def testfunc(myname, lastname):
    print('Привет, %s %s' % (myname, lastname))

testfunc("Alex", "Vasabis")

def savemoney(zarplata, podrabotka, rashody):
    return zarplata + podrabotka - rashody

print(savemoney(28800, 100, 9843))

print(7*52)

print(savemoney(rashody=7777, zarplata=55000, podrabotka=2000))
