from typing import List, Iterator, Tuple

Rod = List[int]
State = Tuple[Rod, Rod, Rod]
Move = Tuple[int, int]

def hanoi_solver(n_disks: int) -> str:
    states = simulate_hanoi(n_disks)
    return format_states(states)

def simulate_hanoi(n_disks: int) -> List[State]:
    rods: List[Rod] = [
        list(range(n_disks, 0, -1)),
        [],
        []
    ]

    states: List[State] = [snapshot(rods)]

    for src, dst in hanoi_moves(n_disks, 0, 1, 2):
        disk = rods[src].pop()
        rods[dst].append(disk)
        states.append(snapshot(rods))

    return states


def hanoi_moves(n: int, src: int, aux: int, dst: int) -> Iterator[Move]:
    if n == 0:
        return
    yield from hanoi_moves(n - 1, src, dst, aux)
    yield src, dst
    yield from hanoi_moves(n - 1, aux, src, dst)

def snapshot(rods: List[Rod]) -> State:
    return tuple(list(r) for r in rods)

def format_states(states: List[State]) -> str:
    return "\n".join(
        f"{a} {b} {c}" for a, b, c in states
    )

print(hanoi_solver(3))