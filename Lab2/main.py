import csv
import faker
import random

fake = faker.Faker()
positions = ('Developer', 'Manager', 'Admin', 'Assistant', 'Analytic')
departments = ('Develop', 'QA', 'Maintenance', 'DevOps', 'EndUser service')


class Employee:
    """Represented single Employee object"""
    fio: str
    Position: str
    Department: str
    Estimate: float
    Salary: int

    def __init__(self):
        """Constructor"""
        self.fio = fake.name()
        self.Position = positions[random.randrange(0, 5, 1)]
        self.Department = departments[random.randrange(0, 5, 1)]
        self.Estimate = random.randrange(0, 5)
        self.Salary = random.randrange(50000, 150000, 100)


def get_report(employees_list: list) -> dict:
    """
    Gets list of employees and calculates metrics for every department as a dictionary record
    :param employees_list: list of employees to parse
    :return: dictionary with information about department metrics
    """
    report: dict = dict()
    for employ in employees_list:
        if employ.Department not in report.keys():
            report.update({employ.Department: [employ.Department, 0, employ.Salary, employ.Salary, 0.0]})
        temp: list = report[employ.Department]
        temp = calculate_stats(temp, employ)
        report.update({employ.Department: temp})
    for k in report:
        report[k][4] /= report[k][1]
        report[k][4] = round(report[k][4], 2)
    return report


def calculate_stats(dep_stats: list, employ: Employee) -> list:
    """
    Recalculate stats for department according with employee information
    :param dep_stats: list with department stats to recalculate
    :param employ: current employee
    :return: recalculated stats for department
    """
    dep_stats[1] += 1
    if dep_stats[2] > employ.Salary:
        dep_stats[2] = employ.Salary
    if dep_stats[3] < employ.Salary:
        dep_stats[3] = employ.Salary
    dep_stats[4] = (dep_stats[4] + employ.Salary)
    return dep_stats


def create_fake_data(size: int) -> list:
    """
    Generate Employee list of specified size
    :param size: size of the list
    :return: list of employees
    """
    temp: list = list()
    for _ in range(size):
        new_employ = Employee()
        temp.append(new_employ)
    return temp


def csv_writer(data: dict, path: str, fieldnames: list):
    """
    Write selected data to CSV file by specified path
    :param fieldnames: headers of csv file
    :param data: data to write in file
    :param path: path to save file
    """
    with open(path, 'w', newline='') as output:
        writer = csv.writer(output, delimiter=' ', dialect='excel')
        writer.writerow(fieldnames)
        for row in data:
            writer.writerow(data[row])


def get_departments():
    """Prints list of departments"""
    for dep in departments:
        print(dep)


def chooser(var_list: list) -> str:
    """
    Just checks if variant is valid and return it
    :param var_list: variants of selection
    :return: selected variant
    """
    print('Select option: ')
    print(var_list)
    choose = input('Choose one:')
    while choose not in var_list:
        print('incorrect option')
        choose = input('Choose one:')
    return choose


if __name__ == '__main__':
    variants = ['Departs', 'Create report', 'Save to CSV']
    headers = ['Department', 'Employees count', 'Minimal Salary', 'Maximal Salary', 'Average salary']
    report_dict: dict = dict()
    employee_list = create_fake_data(100)
    ch = chooser(variants)
    if ch == variants[0]:
        get_departments()
        ch = chooser(variants)
    if ch == variants[1]:
        report_dict = get_report(employee_list)
        for r in report_dict:
            print(report_dict[r])
        ch = chooser(variants)
    if ch == variants[2]:
        csv_writer(report_dict, 'C:/Users/zenv9/OneDrive/Desktop/tmp/output.csv', headers)
        print('That`s All Folks!')
        exit(0)
