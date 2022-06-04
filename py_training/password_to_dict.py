from pprint import pprint

def passwd_to_dict(filename):
    users = {}
    with open(filename,'r') as f:
        for line in f:
            user_info =line.split(':')
            users.update({user_info[0]: user_info[2]})
    return users




pprint(passwd_to_dict('F1750_exercises/py/data/passwd.cfg'),sort_dicts=False)