def sum_distance(from_num, to_num):
    # Меняем значения местами, если from_num больше to_num
    if from_num > to_num:
        from_num, to_num = to_num, from_num

    # Суммируем все числа от from_num до to_num включительно
    total = 0
    for num in range(from_num, to_num + 1):
        total += num

    return total
print('Расстояние теперь:' + sum_distance(5, 1))
