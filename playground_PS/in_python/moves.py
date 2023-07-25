import random

int_min = -1000
int_max = 1000
sample_size = 100

stack_a = random.choices(range(int_min, int_max + 1), k=sample_size)
stack_b = []

# for use cases
total_moves = 0
sorted_stack = sorted(stack_a)

def sa():
    global stack_a, total_moves
    stack_a[0], stack_a[1] = stack_a[1], stack_a[0]
    print("sa")
    total_moves += 1


def sb():
    global stack_b, total_moves
    stack_b[0], stack_b[1] = stack_b[1], stack_b[0]
    print("sb")
    total_moves += 1


def pa():
    global stack_a, stack_b, total_moves
    stack_a.insert(0, stack_b[0])
    stack_b.pop(0)
    print("pa")
    total_moves += 1


def pb():
    global stack_a, stack_b, total_moves
    stack_b.insert(0, stack_a[0])
    stack_a.pop(0)
    print("pb")
    total_moves += 1


def ra():
    global stack_a, total_moves
    stack_a = stack_a[1:] + [stack_a[0]]
    print("ra")
    total_moves += 1


def rb():
    global stack_b, total_moves
    stack_b = stack_b[1:] + [stack_b[0]]
    print("rb")
    total_moves += 1


def rra():
    global stack_a, total_moves
    stack_a = [stack_a[-1]] + stack_a[:-1]
    print("rra")
    total_moves += 1


def rrb():
    global stack_b, total_moves
    stack_b = [stack_b[-1]] + stack_b[:-1]
    print("rrb")
    total_moves += 1