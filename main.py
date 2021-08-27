from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def main():
    time = datetime.now()
    print(time)
    print(calculate_salary())
    print(get_employees())


if __name__ == '__main__':
    main()