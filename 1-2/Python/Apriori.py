from apriori_python import apriori

transactions= [['Тетрадь', 'Ручка', 'Краски'],
               ['Тетрадь', 'Ручка', 'кисть'],
               ['Краски', 'Ручка', 'Ластик']]

freqItemSet, rules = apriori(transactions, minSup=0.5, minConf=0.5)
print(rules)
