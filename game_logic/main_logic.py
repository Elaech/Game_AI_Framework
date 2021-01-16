from idlelib.idle_test.test_colorizer import source

'''
Verifying the integrity of the input code
'''

score_function = None
winning_function = None


def check_winning_method(string=None):
    global winning_function
    try:
        if not string:
            with open("../game_logic/winning_method.py", "r") as o:
                exec(o.read(), globals())
        else:
            exec(string, globals())
    except:
        return False
    winning_function = winning_method

    if not test_valid_code_winning_method():
        return False
    if not test_valid_return_winning_method():
        return False

    return True


def check_score_method(string=None):
    global score_function
    try:
        if not string:
            with open("../game_logic/score_method.py", "r") as o:
                exec(o.read(), globals())
        else:
            exec(string, globals())
    except:
        return False
    score_function = score_method

    if not test_valid_code_score_method():
        return False
    if not test_valid_return_score_method():
        return False

    return True


def test_magic():
    with open("../game_logic/score_method.py", "r") as o:
        print(o.read())


def test_magic2():
    print(score_method())


def test_valid_return_score_method():
    return_value = score_function()
    if type(return_value) == float or type(return_value) == int:
        print("Score method: valid return")
        return True

    print("Score method error: return value not int nor float")
    return False


def test_valid_return_winning_method():
    return_value = winning_function()
    if type(return_value) == bool:
        print("Win condition: valid return")
        return True

    print("Win condition error: return value not bool")
    return False


def test_valid_code_score_method():
    try:
        a = score_function()
    except Exception as e:
        print("Score method error: "+str(e))
        return False

    print("Score method: valid code")
    return True


def test_valid_code_winning_method():
    try:
        a = winning_function()
    except Exception as e:
        print("Win condition error: " +str(e))
        return False

    print("Win condition: valid code")
    return True
