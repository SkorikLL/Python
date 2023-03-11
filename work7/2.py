def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print(*[x for x in nums])

print_operation_table(lambda x,y: x*y, 5, 5)