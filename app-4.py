# >> pip install switchlang
from switchlang import switch

def action_1():
    print('ACTION 1')

def action_2():
    print('ACTION 2')

def default_action():
    print('DEFAULT ACTION')

if __name__ == '__main__':
    option = int(input("Enter an option number:\n"))
    with switch(option) as s:
        s.case(1, action_1)
        s.case(2, action_2)
        s.default(default_action)
