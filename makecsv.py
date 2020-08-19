f=open('list.csv', 'w')

colors = ['빨강', '주황', '노랑', '초록']
fruits = ['사과', '오렌지', '바나나', '라임']

for i in range(len(colors)):
    f.write(colors[i]+','+fruits[i]+'\n')

f.close()