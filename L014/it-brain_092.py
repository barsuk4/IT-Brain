def list_depth(lst):
    if not isinstance(lst, list):
        return 0
    max_depth = 1
    for item in lst:
        max_depth = max(max_depth, 1 + list_depth(item))
    return max_depth

def print_formatted_list(lst, indent_symbol="→"):
    depth = list_depth(lst)

    def helper_print_list(l, current_depth=0):
        indent = indent_symbol * current_depth
        if not isinstance(l, list):
            print(indent + str(l))
            return
        for item in l:
            if isinstance(item, list):
                helper_print_list(item, current_depth + 1)
            else:
                print(indent + str(item))

    helper_print_list(lst)

# Тестові дані:
test_data = [
    [1, 2, 3, 4],
    [1, [2, 3], 4],
    [1, [2, [3, 4]], 5],
    [1, [2, [3, [4, 5]]]],
    [],
    [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
]

for test in test_data:
    print("List:")
    print_formatted_list(test)
    print("-" * 50)  # Розділювач між списками
