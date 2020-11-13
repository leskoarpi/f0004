név = input('Hogy hívnak? ')

kor = input('És hány éves vagy? ') 
kor = int(kor) 

erettsegi_év = 18 - kor
print(név,', ön ', erettsegi_év, ' év múlva fog érettségizni ', sep='')