import random

class Tic_Tac_Toe:
 
    # 게임판 생성
    def __init__(self):
        # 현재 클래스 전역에서 사용하려면 앞에 self. 붙여준다
        self.board = []

    # 게임판 초기화
    def create_board(self):
        # 빈 칸은 * asterisk로 표기
        for i in range(3):
            # 하나의 행 생성
            row = []
            for j in range(3):
                # "*"로 채운 3개의 칸 만들기
                row.append("*")
            self.board.append(row)

    # 첫 플레이어 선택
    def select_first_player(self):
        # 무작위로 둘 중에 하나를 선택
        if random.randint(0,1) == 0 : 
        #range(0,3) 범위는 0,1,2를 의미하는데 반해,
        #randint(0,3) 범위는 0,1,2,3이므로 주의
            return 'X'
        else:
            return "O"

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row-1][col-1] = player

    # 승리 상태 확인
    def is_winner(self, player) :
        n = len(self.board)

        # 행 확인
        for i in range(n) :
            win = True
            for j in range(n):
                if self.board[i][j] != player :
                    win = False
                    break
            if win == True:
                return win

        # 열 확인 
        for i in range(n) :
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win

        # 오른쪽 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player :
                win = False
                break
        if win == True:
            return win

        return False

        # 왼쪽 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][n-i-1] != player :
                win = False
                break
        if win == True:
            return win

        return False
 

    #잔여 빈칸 여부 확인
    def is_board_full(self):
        # 한 칸씩 확인 후, 빈 칸을 의미하는 "*"가 있으면 False 반환
        for row in self.board :
            for item in row:
                if item == "*":
                    return False
        return True

    # 플레이어 변경
    def next_player(self, player):
        if player == "O":
            return "X"
        else :
            return "O"

        # return "X" if player == "O" else "O"

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board : 
            for item in row:
                print(item, end= " ")
            print()

    # 게임 시작
    def start(self):

        # 새 게임판 생성
        self.create_board()
        self.show_board()

        # 첫 플레이어 선택
        player = self.select_first_player()

        # 게임 루프 시작
        while True :

            # 다음 플레이어 안내
            if player == "X" :
                print("컴퓨터 차례입니다.")
            else:
                print("사용자 차례입니다.")


            # 현재 게임판 상태 출력
            self.show_board()

            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == "X":
                while True:
                    row, col = random.randint(1,3), random.randint(1,3)
                    if self.board[row-1][col-1] == "*":
                        break

                print("컴퓨터가 행 "+ str(row)+", 열 "+ str(col) +"을/를 선택했습니다.")
                print()
            else :
                # map 함수 : 1. 리스트 각각의 요소에 함수를 적용해주는 역할
                # 2. input으로 입력받은 위칫값에 (정수로 바꾸는 함수인) int 함수 적용
                # 3. map(뒤에 리스트에 적용할 함수, 리스트)
                # 4. 마무리 : 어떤 형태로 만들어 주어야 하는지 명시해야 한다 (list함수 적용)

                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요: ").split()))
                print("사용자가 행 "+ str(row)+", 열 "+ str(col) +"을/를 선택했습니다.")
                print()

            # row, col 입력값이 0, 0인 경우 게임 종료
            if row == 0 and col == 0 :
                break
           
            # 입력된 위치 표시
            self.mark_spot(row, col, player)
            self.show_board()

            # 현재 플레이어가 이겼는지 확인
            if self.is_winner(player) == True :
                # 1. 승리 상황 메소드(is_winner) 값이 True인지 확인
                # 2. 승리자에 맞는 메시지 출력
                # 3. 상황종료
                if player == "X":
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break

            # 게임판 가득참 확인
            if self.is_board_full() == True:
                print("무승부입니다. 다시 도전하세요.")
                break

            # 플레이어 변경
            player = self.next_player(player)

        # 최종 게임판 출력
        print()
        self.show_board()


# 게임 생성
TTT = Tic_Tac_Toe()

# 게임 시작
TTT.start()
