név = input('Hogy hívnak? ')
datum = input('milyen évet írunk? ')
kor = input('És hány éves vagy? ') 
kor = int(kor) 
datum = int(datum)
születési_év = datum - kor
print(név,', ön ', születési_év, '-ban/ben született.', sep='')