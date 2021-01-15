def check_winning_method(code):
    return True


def check_score_method(code):
    return True



def test_magic():
    with open("../game_logic/score_method.py","r") as o:
        print(o.read())

def test_magic2():
    from game_logic import score_method
    print(score_method.score_method())