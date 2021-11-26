word = input() + ' запретил букву'
alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
       'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(len(alf)):
    word = word.strip()
    if alf[i] in word:
        print(word, alf[i])
        word = word.replace(alf[i], '')
        word = word.replace('  ', ' ')
    if len(word) < 1:
        break