def insert_in_sorted_order(stack, element):

    if not stack or stack[-1] <= element:
        stack.append(element)
    else:

        temp = stack.pop()
        insert_in_sorted_order(stack, element)

        stack.append(temp)

def sort_stack(stack):

    if len(stack) > 1:

        temp = stack.pop()
        sort_stack(stack)

        insert_in_sorted_order(stack, temp)

stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)