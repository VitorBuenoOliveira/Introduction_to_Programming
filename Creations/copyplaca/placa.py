import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext(
    image='placa.jpg',
)

for result in results:
    print(f'{results} - {results[0]}')