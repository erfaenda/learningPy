test_file = open('/home/alex/SomeTest.txt', 'w')
test_file.write('это просто тест, just test text baby:)')
#test_file.close
test_file = open('/home/alex/SomeTest.txt')
#print(test_file.read())

totestfile = open('/home/alex/SomeTest2.txt', 'w')
totestfile.write(test_file.read())
