# **\<LeetCode Progress\>**
릿코드 프로필 링크: https://leetcode.com/u/dahyun12/

<img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/score1.png" width="300">
<img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/score2.png" width="400">

---
---

# **\<Final Project\>**  
## Topic: Sudoku Game with Python

---

### 프로젝트 개요

파이썬을 이용하여 만든 콘솔 기반 스도쿠 게임

프로그램은 0이 포함된 임의의 9×9 스도쿠 보드를 생성하고,  
그 보드가 스도쿠로서 해답이 **존재하며 유일한지**를 검사한 뒤 사용자에게 퍼즐로 제공한다.  
사용자는 **행, 열, 숫자 (1~9)**를 입력하여 빈칸을 채우며 문제를 해결한다.

---

### 게임 규칙

- **1~9의 정수**로 행, 열, 값을 입력한다.  
- **미리 채워진 칸은 수정할 수 없다.**  
- 틀린 입력을 **3회** 하면 게임이 종료되고, 정답이 출력된다.  
- 모든 빈칸을 올바르게 채우면 **승리 메시지**가 출력된다.  
- 게임 종료 후에는 **다시 시작할 수 있다.**

---

### 코드 구조 및 기능 설명

## `is_valid(board, row, col, num)`
- 주어진 숫자 `num`을 `board[row][col]`에 넣을 수 있는지 검사한다.
- 같은 행/열/3×3 구역에 `num`이 이미 존재하면 False를 반환한다.
- num이 유효하면 `True`를 반환한다.

## `count_solutions(board)`
- 현재 보드 상태에서 가능한 **정답의 개수**를 백트래킹으로 계산한다.
- 두 개 이상의 해답이 생기면 더 이상 탐색하지 않고 조기 종료한다.
- **유일한 해**가 있는 퍼즐만 제공하기 위해 사용된다.

## `fill_board(board)`
- 완성된 정답 보드를 만드는 백트래킹 함수
- 숫자 1~9를 무작위 순서로 넣으며 가능한 보드를 완성한다.
- `random.shuffle()`을 사용해서 숫자 순서를 매번 섞기 때문에 다양한 보드가 생성된다.

## `generate_sudoku()`
- **전체 게임의 핵심**으로, 사용자가 풀게 될 **퍼즐 보드**를 생성한다.
- 우선 `fill_board`로 완성된 보드를 만들고,  
  일부 칸을 비우면서 그 상태가 여전히 **유일한 해를 갖는지** 확인한다.
- 무작위로 최대 40칸 정도를 비운운다.
- 최종적으로 `(퍼즐, 정답)` 형태의 튜플을 반환한다.

## `print_board(board)`
- 현재 보드를 보기 쉽게 출력한다.
- 3×3 블록 구역마다 `|`와 `------+-------+------`로 시각적 구분선을 넣어 가독성을 높인다.
- 빈칸은 `.`으로 출력된다.

## `play_game()`
- 실제 게임을 진행하는 **메인 함수**
- 퍼즐을 출력하고 사용자 입력을 받아 검증하며,  
  정답과 일치하는 경우만 보드에 반영된다.
- 오답을 3회 입력하면 게임이 종료되고 정답이 출력된다.
- 퍼즐을 모두 맞히면 축하 메시지 출력 후, 다시 시작 여부를 묻는는다.

---

### 실행 예시

- 시작 화면
  게임이 시작되면 사용자는 행, 열, 값을 입력해 스도쿠 보드를 채울 수 있다.
  올바른 값을 입력하면 해당 값이 추가된 상태의 보드가 출력되고, 다시 사용자는 행, 열, 값을 입력할 수 있다.
  
  <img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/sudoku.%EC%8B%9C%EC%9E%91%ED%99%94%EB%A9%B4.png" width="250"/>

- 잘못 입력 시
  잘못된 값을 입력 시 "WRONG NUMBER!"이라는 출력과 함께 실수 횟수를 표시한다:(n/3)
  이는 틀린 값을 3회 입력할 경우 게임이 오버되는 규칙을 표시하는 것이다.
  또한 스도쿠 보드가 **입력값을 추가하기 않고** 다시 출력되어 사용자는 행, 열, 값을 입력할 수 있다.

   <img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/sudoku.wrongnum.png" width="230"/>

  만약 숫자를 입력할 수 없는 행, 열을 고르거나 1-9 사이의 값을 입력하지 않을 경우에는
  "You cannot change this cell.", "Invalid range. Please enter numbers from 1 to 9."와 같은 메시지가 출력되며
  다시 입력 기회가 생긴다.

- 게임 종료
  잘못된 값을 3회 입력하여 기회가 소진되면 게임 오버된다.
  
  <img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/sudoku.%EA%B2%8C%EC%9E%84%EC%98%A4%EB%B2%84.png" width="250"/>

 만약 모든 빈칸을 올바른 숫자로 채우고, 잘못된 값을 입력한 횟수가 3회 미만이면 게임이 클리어된다.

<img src="https://github.com/dahyun12/final_project_2024131017DahyunKang/blob/main/sudoku.%ED%81%B4%EB%A6%AC%EC%96%B4.png" width="250"/>
 
---

### 한계 및 고찰

- 정답이 유일한 퍼즐을 생성하기는 하지만, 코드 효율성 및 퍼즐 생성 속도를 더 개선할 여지가 있다.
- GUI(그래픽 인터페이스)가 없기 때문에 직관적으로 보기에는 어려울 수 있다.
- 난이도 조절 기능이 없어, 매번 랜덤으로 만들어진 퍼즐을 그대로 풀어야 한다.
