from idlelib.idle_test.test_colorizer import source

'''
Verifying the integrity of the input code
'''

score_function = None
winning_function = None


def check_winning_method(string=None):
    try:
        if not string:
            with open("../game_logic/winning_method.py", "r") as o:
                exec(o.read(), globals())
        else:
            exec(string, globals())
    except:
        return False
    winning_function = winning_method
    print(winning_function())
    # if not test_valid_code_winning_method():
    #     return False
    # if not test_valid_return_winning_method():
    #     return False

    return True


def check_score_method(string=None):
    try:
        if not string:
            with open("../game_logic/score_method.py", "r") as o:
                exec(o.read(), globals())
        else:
            exec(string, globals())
    except:
        return False
    score_function = score_method
    print(score_function())
    # if not test_valid_code_score_method():
    #     return False
    # if not test_valid_return_score_method():
    #     return False

    return True


def test_magic():
    with open("../game_logic/score_method.py", "r") as o:
        print(o.read())


def test_magic2():
    print(score_method())


def test_valid_return_score_method():
    return_value = score_function()
    print(return_value)
    if type(return_value) == float or type(return_value) == int:
        return True

    return False


def test_valid_return_winning_method():
    return_value = score_function()
    if type(return_value) == bool:
        return True

    return False


# not tested
def test_valid_code_score_method():
    try:
        print(winning_function())
    except:
        return False

    return True


# not tested
def test_valid_code_winning_method():
    try:
        print(winning_function())
    except:
        return False

    return True
