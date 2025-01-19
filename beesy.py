from collections import deque

def move(position, direction, n):
    row, col = position
    if direction == 'up':
        row = (row - 1) % n
    elif direction == 'down':
        row = (row + 1) % n
    elif direction == 'left':
        col = (col - 1) % n
    elif direction == 'right':
        col = (col + 1) % n
    return row, col

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def main():
    n = int(input())
    matrix = []
    bee_position = None

    for i in range(n):
        row = list(input().strip())
        if 'B' in row:
            bee_position = (i, row.index('B'))
        matrix.append(row)

    commands = deque()
    while True:
        try:
            command = input().strip()
            if not command:
                break
            commands.append(command)
        except EOFError:
            break

    energy = 15
    collected_nectar = 0
    energy_restored = False

    while commands:
        command = commands.popleft()
        matrix[bee_position[0]][bee_position[1]] = '-'
        bee_position = move(bee_position, command, n)
        energy -= 1

        row, col = bee_position
        cell = matrix[row][col]

        if cell == 'H':
            if collected_nectar >= 30:
                print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            else:
                print("Beesy did not manage to collect enough nectar.")
            matrix[row][col] = 'B'
            print_matrix(matrix)
            return
        elif cell.isdigit():
            collected_nectar += int(cell)
            matrix[row][col] = '-'

        matrix[row][col] = 'B'

        if energy == 0:
            if collected_nectar >= 30 and not energy_restored:
                energy_restored = True
                energy = collected_nectar - 30
                collected_nectar = 30
            else:
                print("This is the end! Beesy ran out of energy.")
                print_matrix(matrix)
                return

    if energy == 0:
        print("This is the end! Beesy ran out of energy.")
    else:
        print_matrix(matrix)

if __name__ == "__main__":
    main()
