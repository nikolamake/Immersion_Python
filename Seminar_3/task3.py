 # В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр
# символов. За основу возьмите любую статью из википедии или
# из документации к языку.

text = 'Большая часть работы программистов связана с написанием исходного кода, тестированием \
и отладкой программ на одном из языков программирования. Исходные тексты и исполняемые файлы \
программ являются объектами авторского права и являются интеллектуальной собственностью их \
авторов и правообладателей Различные языки программирования поддерживают различные стили \
программирования парадигмы программирования . Выбор нужного языка программирования для \
некоторых частей алгоритма позволяет сократить время написания программы и решить задачу \
описания алгоритма наиболее эффективно. Разные языки требуют от программиста различного \
уровня внимания к деталям при реализации алгоритма, результатом чего часто бывает компромисс \
между простотой и производительностью (или между «временем программиста» и \
«временем пользователя»).Единственный язык, напрямую выполняемый ЭВМ — это машинный язык \
(также называемый машинным кодом и языком машинных команд). Изначально все программы \
писались в машинном коде, но сейчас этого практически уже не делается. Вместо этого \
программисты пишут исходный код на том или ином языке программирования, затем, используя \
компилятор, транслируют его в один или несколько этапов в машинный код, готовый к исполнению \
на целевом процессоре, или в промежуточное представление, которое может быть исполнено \
специальным интерпретатором — виртуальной машиной. Но это справедливо только для языков \
высокого уровня. Если требуется полный низкоуровневый контроль над системой на уровне \
машинных команд и отдельных ячеек памяти, программы пишут на языке ассемблера, \
инструкции которого преобразуются один к одному в соответствующие инструкции машинного языка \
целевого процессора ЭВМ (по этой причине трансляторы с языков ассемблера получаются \
В некоторых языках вместо машинного кода генерируется интерпретируемый двоичный код \
«виртуальной машины», также называемый байт-кодом (byte-code). Такой подход применяется \
в Forth, некоторых реализациях Lisp, Java, Perl, Python, языках для .NET Framework.'

word_list = text.lower()
char_remov = [',', '.', '«', '»', '(', ')', '—', '-']
for char in char_remov:
    word_list = word_list.replace(char, ' ')
word_list_spl = word_list.split()

tuple_counts = dict()
for word in word_list_spl:
    if word in tuple_counts:
        tuple_counts[word] += 1
    else:
        tuple_counts[word] = 1

sort_counts = dict(sorted(tuple_counts.items(), key=lambda x: x[1], reverse=True))

print(list(sort_counts.items())[:10])

