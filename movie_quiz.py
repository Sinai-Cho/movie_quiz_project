# 영화 퀴즈 게임

# 문제 생성 
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, quiz_number):
        print()
        print("[문제", quiz_number, "]", self.question)

        for i in range(4):
            print(str(i + 1) + ".", self.choices[i])

    def check_answer(self, user_answer):
        return user_answer == self.answer






# 파이선 실행 후 등장하는 첫 화면

def show_menu():
    print()
    print("=" * 40)
    print("영화 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 퀴즈 점수 확인")
    print("5. 프로그램 종료")
    print("=" * 40)


def get_number(message, minimum, maximum):
    while True:
        user_input = input(message).strip()

        if user_input == "":
            print("아무것도 입력하지 않았습니다. 다시 입력하세요.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print("숫자로 입력하세요.")
            continue

        if number < minimum or number > maximum:
            print(minimum, "부터", maximum, "사이의 숫자를 입력하세요.")
            continue

        return number


while True:
    show_menu()

    menu = get_number(
        "메뉴 번호를 입력하세요: ",
        1,
        5
    )

    if menu == 1:
        print("퀴즈 풀기 기능은 아직 준비 중입니다.")

    elif menu == 2:
        print("퀴즈 추가 기능은 아직 준비 중입니다.")

    elif menu == 3:
        print("퀴즈 목록 기능은 아직 준비 중입니다.")

    elif menu == 4:
        print("점수 확인 기능은 아직 준비 중입니다.")

    elif menu == 5:
        print("프로그램을 종료합니다.")
        break