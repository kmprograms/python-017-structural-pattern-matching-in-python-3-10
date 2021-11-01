from datetime import datetime

def get_age(user):
    match user:
        case {'age': {'birthdate': birthdate}}:
            year_now = datetime.now().year
            birthdate_year = datetime.strptime(birthdate, '%Y-%m-%d').year
            return year_now - birthdate_year
        case {'age': int(age)}:
            return age


if __name__ == '__main__':
    user1 = {
        'name': 'John',
        'age': 12
    }

    user2 = {
        'name': 'John',
        'age': {
            'birthdate': '2000-01-01'
        }
    }

    print(get_age(user1))
    print(get_age(user2))
