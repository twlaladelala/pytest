class Employer():
    def __init__(self, no, name):
        self.name = name
        self.no = no

    def get_salary(self):
        pass


class Manager(Employer):
    def get_salary(self):
        return 15000


class Programmer(Employer):
    def __init__(self, no, name):
        super().__init__(no, name)
        self.working_hour = 0

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employer):
    def __init__(self, no, name):
        super().__init__(no, name)
        self.sales = 0

    def get_salary(self):
        return 1800 + 0.05 * self.sales


def main():
    emps = [
        Manager(1122, '田伟'),
        Programmer(1133, '田伟1'),
        Programmer(1144, '田伟2'),
        Salesman(1155, '田伟3'),
        Salesman(1166, '田伟4'),
        Programmer(1177, '田伟5'),
        Salesman(1188, '田伟6')
    ]
    for emp in emps:
        if type(emp) == Programmer:
            emp.working_hour = int(input(f'请输入{emp.name}的工作时长：'))

        print(f'{emp.name}本月工资：{emp.get_salary()}元')


if __name__ == '__main__':
    main()
