import random
import copy

# 해당 숫자를 보드에 넣을 수 있는지 확인
# 행, 열, 3x3 박스 중복 모두 검사

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_r, start_c = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == num:
                return False
    return True

# 가능한 정답 개수 세기 (정답이 1개인지 확인)
def count_solutions(board):
    count = [0]
    def backtrack():
        if count[0] > 1:
            return
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            backtrack()
                            board[r][c] = 0
                    return
        count[0] += 1
    backtrack()
    return count[0]

# 정답 보드 생성 (백트래킹)
def fill_board(board):
    nums = list(range(1, 10))
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if fill_board(board):
                            return True
                        board[r][c] = 0
                return False
    return True

# 유일한 정답을 갖는 퍼즐 생성
def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    puzzle = copy.deepcopy(board)
    blanks = 40
    while blanks > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if puzzle[r][c] == 0:
            continue
        backup = puzzle[r][c]
        puzzle[r][c] = 0
        temp = copy.deepcopy(puzzle)
        if count_solutions(temp) != 1:
            puzzle[r][c] = backup
        blanks -= 1
    return puzzle, board

# 보드 출력 함수
def print_board(board):
    print()  # 보기 좋게 위에 줄바꿈 추가
    for i, row in enumerate(board):
        line = ""
        for j, num in enumerate(row):
            symbol = str(num) if num != 0 else "."
            line += symbol + " "
            if (j + 1) % 3 == 0 and j < 8:
                line += "| "
        print(line)
        if (i + 1) % 3 == 0 and i < 8:
            print("------+-------+------")
    print()

# 게임 실행 함수
def play_game():
    puzzle, solution = generate_sudoku()
    current = copy.deepcopy(puzzle)
    wrong = 0

    print("=== WELCOME TO SUDOKU ===\n")

    while True:
        print_board(current)

        if current == solution:
            print("CLEAR! YOU WIN!")
            break

        if wrong >= 3:
            print("GAME OVER!")
            print("The correct solution was:\n")
            print_board(solution)
            break

        try:
            r = int(input("Enter row (1-9): ")) - 1
            c = int(input("Enter column (1-9): ")) - 1
            n = int(input("Enter number (1-9): "))

            print()  # 입력 직후 한 줄 띄우기

            if not (0 <= r < 9 and 0 <= c < 9 and 1 <= n <= 9):
                print("Invalid range. Please enter numbers from 1 to 9.")
                continue

            if puzzle[r][c] != 0:
                print("You cannot change this cell.")
                continue

            if is_valid(current, r, c, n) and solution[r][c] == n:
                current[r][c] = n
            else:
                wrong += 1
                print(f"WRONG NUMBER! ({wrong}/3)\n")

        except ValueError:
            print("Invalid input. Please enter integers only.\n")

    again = input("Play again? (y/n): ").lower()
    if again == 'y':
        play_game()

# 시작
if __name__ == "__main__":
    play_game()
