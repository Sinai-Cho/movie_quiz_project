# 영화 퀴즈 게임

import json
import os   

#=================================================
# 문제 1개당 형태 클래스 (Class Quiz)
#=================================================
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

#=================================================       
# 기본 퀴즈 10문제
#=================================================
def make_default_quizzes():
    quizzes = [
        Quiz(
            "다음 중 봉준호 감독의 작품이 아닌 영화는?",
            ["살인의 추억", "옥자", "박쥐", "괴물"],
            3
        ),
        Quiz(
            "박찬욱 감독의 영화에 출연하지 않은 여배우는?",
            ["이정은", "이영애", "탕웨이", "손예진"],
            1
        ),
        Quiz(
            "다음 중 박찬욱 감독의 작품이 아닌 영화는?",
            ["헤어질 결심", "아가씨", "마더", "스토커"],
            3
        ),
        Quiz(
            "영화 '스타워즈' 시리즈를 최초로 만든 감독은?",
            ["스티븐 스필버그", "조지 루카스", "크리스토퍼 놀란", "피터 잭슨"],
            2
        ),
        Quiz(
            "다음 중 'MARVEL'에 속하지 않는 히어로는?",
            ["아이언맨", "헐크", "블랙팬서", "플래시"],
            4
        ),
        Quiz(
            "1000만 관객수를 넘긴 한국 영화는?",
            ["신과 함께 시리즈(죄와 벌, 인과 연)", "JSA 공동경비구역", "친구", "관상"],
            1
        ),
        Quiz(
            "한국에서 개최되는 영화제가 아닌 것은?",
            ["부산 국제영화제", "춘천 국제 음악 영화제", "전주 국제영화제", "부천 국제 판타스틱 영화제"],
            2
        ),
        Quiz(
            "다음 배우 중 일본 영화제에서 여우주연상을 받은 여배우는?",
            ["배수지", "강지영", "하연수", "심은경"],
            4
        )
    ]

    return quizzes

#=================================================
# 데이터 저장 및 불러오기 (Class DataManager)
#=================================================
class DataManager:
    def __init__(self):
        project_folder = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(project_folder, "state.json")

    def save_state(self, quizzes, best_score):
        data = {
            "quizzes": [],
            "best_score": best_score
        }

        for quiz in quizzes:
            quiz_data = {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            }

            data["quizzes"].append(quiz_data)

        try:
            file = open(
                self.file_path,
                "w",
                encoding="utf-8"
            )

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

            file.close()

            return True

        except OSError:
            print("파일 저장 중 오류가 발생했습니다.")
            return False

    def load_state(self):
        if not os.path.exists(self.file_path):
            quizzes = make_default_quizzes()
            best_score = 0

            self.save_state(
                quizzes,
                best_score
            )

            return quizzes, best_score

        try:
            file = open(
                self.file_path,
                "r",
                encoding="utf-8"
            )

            data = json.load(file)
            file.close()

            quizzes = []

            for quiz_data in data["quizzes"]:
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"]
                )

                quizzes.append(quiz)

            best_score = data["best_score"]

            return quizzes, best_score

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            OSError
        ):
            print("state.json 파일에 문제가 있습니다.")
            print("기본 퀴즈 데이터로 복구합니다.")

            quizzes = make_default_quizzes()
            best_score = 0

            self.save_state(
                quizzes,
                best_score
            )

            return quizzes, best_score

#=================================================
# 퀴즈 풀기
#=================================================
def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return 0

    score = 0

    print()
    print("영화 퀴즈를 시작합니다.")

    for i in range(len(quizzes)):
        quiz = quizzes[i]

        quiz.show(i + 1)

        user_answer = get_number(
            "정답 번호를 입력하세요: ",
            1,
            4
        )

        if quiz.check_answer(user_answer):
            print("정답입니다!")
            score = score + 1

        else:
            print("오답입니다.")
            print("정답은", quiz.answer, "번입니다.")

    print()
    print("=" * 40)
    print("퀴즈가 끝났습니다.")
    print("점수:", score, "/", len(quizzes))
    print("=" * 40)

    return score


#===================================================
# 파이선 실행 후 등장하는 첫 화면
#===================================================
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



quizzes = make_default_quizzes()

while True:
    show_menu()

    menu = get_number(
        "메뉴 번호를 입력하세요: ",
        1,
        5
    )

    if menu == 1:
        play_quiz(quizzes)

    elif menu == 2:
        print("퀴즈 추가 기능은 아직 준비 중입니다.")

    elif menu == 3:
        print("퀴즈 목록 기능은 아직 준비 중입니다.")

    elif menu == 4:
        print("점수 확인 기능은 아직 준비 중입니다.")

    elif menu == 5:
        print("프로그램을 종료합니다.")
        break