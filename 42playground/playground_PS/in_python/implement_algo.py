from moves import *


def get_min_max_odd():
    odd = sorted([x for x in stack_a if x % 2 == 1])
    return (odd[0], odd[len(odd) - 1])


def get_min_max_even():
    even = sorted([x for x in stack_a if x % 2 == 0])
    return (even[0], even[len(even) - 1])


def print_stacks():
    print("STACK A ", stack_a)
    print("STACK B ", stack_b)


def check_stack_sorted(stack):
    return all(stack[i] <= stack[i+1] for i in range(len(stack)-1))


def send_up(val):
    global stack_a
    while stack_a[0] != val:
        ra()
    pb()


def send_down(val):
    global stack_a
    while stack_a[0] != val:
        rra()
    pb()

# if we are sending the min when the value in odd it can stay on top of the stack
# if we find the stack B is 1, 3, 9 and we have to send max_value, we send it to B and rotate it
#
def pause():
    global stack_a, stack_b


def send_evens(min_even, max_even):
    global stack_a
    min_index = stack_a.index(min_even)
    max_index = stack_a.index(max_even)

    min_cost = min_index if min_index < len(
        stack_a) - min_index else len(stack_a) - min_index
    max_cost = max_index if max_index < len(
        stack_a) - max_index else len(stack_a) - max_index

    if min_cost <= max_cost:
        val = min_even
        use_index = min_index
    else:
        val = max_even
        use_index = max_index
    if stack_a.index(val) < len(stack_a) - use_index:
        send_up(val)
    else:
        send_down(val)


def send_odds(min_odds, max_odds):
    global stack_a
    min_index = stack_a.index(min_odds)
    max_index = stack_a.index(max_odds)

    min_cost = min_index if min_index < len(
        stack_a) - min_index else len(stack_a) - min_index
    max_cost = max_index if max_index < len(
        stack_a) - max_index else len(stack_a) - max_index

    if min_cost <= max_cost:
        val = min_odds
        use_index = min_index
    else:
        val = max_odds
        use_index = max_index
    if stack_a.index(val) < len(stack_a) - use_index:
        send_up(val)
    else:
        send_down(val)
    # rb()


def main():
    global stack_a, stack_b, total_moves
    print_stacks()
    print("STACK A COUNT", len(stack_a))

    min_even, max_even = get_min_max_even()
    min_odd, max_odd = get_min_max_odd()

    even_count = len(list(filter(lambda x: x % 2 == 0, stack_a)))
    odd_count = len(list(filter(lambda x: x % 2 != 0, stack_a)))

    while odd_count != 0:
        try:
            min_odd, max_odd = get_min_max_odd()
        except TypeError:
            break
        send_odds(min_odd, max_odd)
        odd_count -= 1

    while even_count != 0:
        try:
            min_even, max_even = get_min_max_even()
        except TypeError:
            break
        send_evens(min_even, max_even)
        even_count -= 1


    while even_count != 0:
        try:
            min_even, max_even = get_min_max_even()
        except TypeError:
            break
        send_evens(min_even, max_even)
        even_count -= 1

    print("First")
    print_stacks()

    b_len = len(stack_b) - 1
    while (b_len >= 0):
        if stack_b[0] > stack_b[b_len]:
            pa()
        else:
            rrb()
            pa()
        b_len -= 1

    print("Second")
    print_stacks()

    if check_stack_sorted(stack_a):
        print("WTF")
    print("SORTED STACK A : ", sorted(stack_a))

    print("TOTAL MOVES: ", total_moves)


if __name__ == "__main__":
    main()
