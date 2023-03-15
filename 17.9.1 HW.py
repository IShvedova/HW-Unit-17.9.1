#сортировка
def sort_list(list):
    for i in range(len(list)):
        min_ind = i
        for j in range(i + 1, len(list)):
            if list[min_ind] > list[j]:
                min_ind = j
        list[i], list[min_ind] = list[min_ind], list[i]
    return list
#бинарный поиск
def binary_search(y, x):
    left = 0
    right = len(y) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if y[mid] < x:
            left = mid + 1
        elif y[mid] > x:
            right = mid - 1
        else:
            return mid
    return left
#ввод чисел, проверка, сортировка

def main():
    user_input = input("Введите последовательность чисел через пробел: ")
    try:
        num_list = [int(num) for num in user_input.split()]
    except ValueError:
        print("Ошибка ввода! Введены не только числа! ")
        return
    user_num = input("Введите любое число: ")
    try:
        user_num = int(user_num)
    except ValueError:
        print("Ошибка ввода! Введено не число! ")
        return
    sorted_list = sort_list(num_list)
    print('Введенные числа отсортированы:', sorted_list)
    pos = binary_search(sorted_list, user_num)
    if pos == len(sorted_list):
        print("Введенное число больше всех чисел в последовательности")
    elif sorted_list[pos] == user_num:
        print(f"Введенное число расположено на позиции {pos}")
    else:
        print(f"Введенное число находится между позициями {pos - 1} и {pos}")


if __name__ == '__main__':
    main()

