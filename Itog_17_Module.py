stroka = input ("Введите целые числа через пробел => ")
chislo = int(input("Введите любое число => "))

def is_int (str):
    str = str.replace(" ", "")
    try:
        int (str)
        return True
    except ValueError:
        return False

if " " not in stroka:
    print("Между числами нет пробелов, введите целые числа через пробел => ")
    stroka = input()
if not is_int (stroka):
    print ("Введеные значения не соответствуют условию. Перезапустите программу!")
else:
    stroka = stroka.split()

s_stroka = [int(strk) for strk in stroka]

def merge_sort (L):
    if len (L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge (left, right)

def merge (left, right):
    ryd_spisok = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ryd_spisok.append(left[i])
            i += 1
        else:
            ryd_spisok.append(right[j])
            j += 1

    while i < len(left):
        ryd_spisok.append(left[i])
        i += 1

    while j < len(right):
        ryd_spisok.append(right[j])
        j += 1
    return ryd_spisok

s_stroka = merge_sort(s_stroka)

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
       return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(f"Упорядоченный список: {s_stroka}")

if not binary_search(s_stroka, chislo, 0, len(s_stroka)):
    idx = min(s_stroka, key=lambda x: (abs(x - chislo), x))
    ind = s_stroka.index(idx)
    max_ind = ind + 1
    min_ind = ind - 1
    if idx < chislo:
        print(f"""В списке нет введенного числа 
Ближайшее меньшее число: {idx}, его индекс: {ind}
Ближайшее большее число: {s_stroka[max_ind]} его индекс: {max_ind}""")
    elif min_ind < 0:
        print(f"""В списке нет введенного числа
Ближайшее большее число: {idx}, его индекс: {s_stroka.index(idx)}
В списке нет меньшего числа""")
    elif idx > chislo:
        print(f"""В списке нет введенного числа
Ближайшее большее число: {idx}, его индекс: {s_stroka.index(idx)}
Ближайшее меньшее число: {s_stroka[min_ind]} его индекс: {min_ind}""")
    elif s_stroka.index(idx) == 0:
        print(f"Индекс введенного числа: {s_stroka.index(idx)}")
else:
    print(f"Индекс введенного числа: {binary_search(s_stroka, chislo, 0, len(s_stroka))}")
