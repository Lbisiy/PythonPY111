from task_Stack import Stack


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    stack = Stack()
    left_bracket = "("
    right_bracket = ")"

    for elem in brackets_row:
        if elem == left_bracket:
            stack.push(elem)

        else:
            if len(stack) >= 1 and elem == right_bracket:
                stack.pop()

            else:
                return False

    if len(stack) == 0:
        return True

    return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
