rod = list[int]

def hanoi_solver(n_disks: int):
    # CREATE PUZZLE
    first: rod = list(range(n_disks,0,-1))
    second: rod = []
    third: rod = []

    initial_state = [state_snapshot(first, second, third)]
    movements = solve_hanoi(n_disks, first, second, third)

    states = initial_state + movements
    return format_state(states)

def solve_hanoi(n_disks, starting: rod, middle: rod, goal: rod) -> list[list[rod]]:
    states = []
    if n_disks > 1:
        middle_states = solve_hanoi(n_disks - 1, starting, goal, middle)
        states += [[state[0], state[2], state[1]] for state in middle_states]

    disk = starting.pop()
    goal.append(disk)
    states.append(state_snapshot(starting, middle, goal))
    if n_disks > 1:
        final_states = solve_hanoi(n_disks - 1, middle, starting, goal)
        states += [[state[1], state[0], state[2]] for state in final_states]
    return states

def state_snapshot(starting: rod, middle: rod, goal: rod) -> list[rod]:
    return [list(starting), list(middle), list(goal)]

def format_state(states: list[list[rod]]) -> str:
    return '\n'.join([f'{line[0]} {line[1]} {line[2]}' for line in states])

print(hanoi_solver(3))

print(hanoi_solver(2))

