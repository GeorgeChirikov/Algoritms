from assigments.chapter_4.PushNPopStack import Stack


def check_balance(input_string):
    # Map of opening to closing brackets
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    pairs_count = 0

    for index, char in enumerate(input_string):
        if char in bracket_map:  # Opening bracket
            stack.push((char, index))
        elif char in bracket_map.values():  # Closing bracket
            if stack._size == 0:
                return f"Match error at position {index}"  # Closing bracket before an opening one
            top, position = stack.pop()
            if bracket_map[top] != char:
                return f"Match error at position {index}"  # Mismatched pair
            pairs_count += 1

    # After loop, check if stack still has unmatched opening brackets
    if not stack._size ==0:
        _, position = stack.peek()
        return f"Match error at position {position}"

    return f"Ok - {pairs_count}"  # If no errors, return success message



# Test cases

print(check_balance("a(b)c[d]e{f}g"))  # Ok - 3

