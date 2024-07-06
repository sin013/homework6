MyDict = {'Говард': 1890, "Стивен": 1942, 'Артур': 1859}
print(MyDict)
print(MyDict.get('Говард'))
print(MyDict.get('Александр'))
MyDict['Виктор'] = 1802
MyDict['Федор'] = 1803
a = MyDict.pop('Артур')
print(a)
print(MyDict)
MySet = {'утка', 1875, True, 'утка', 1875, False,(1,2,3,)}
print(MySet)
MySet.update({'кряква',1235})
MySet.remove("утка")
print(MySet)