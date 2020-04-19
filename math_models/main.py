import math
from matplotlib import pyplot


def main():
    result_table = {'x1': [], 'x2': [], 'p1': [], 'p4': []}
    branch_points = {'x1': [], 'x2': [], 'p1': [], 'p4': []}
    x1 = 0.1
    h = 0.01
    p2 = 1.5
    p3 = 3.0
    p5 = 0.01

    while x1 < 1.305:  # x1 = [0.1; 1.3]; h = 0.01
        constant = (p5 + x1 ** p3) / (1 + x1 ** p3)
        constant_2 = (1 + x1 ** p3) ** 2
        a = (p3 * x1 ** p3 * (p5 - 1)) / (constant_2 * constant) + 1
        b = (p3 * x1 ** (p3 + 1) * (p5 - 1)) / (constant_2 * constant) * (p2 - 2) - 2 * x1 + 2 * x1 * p2
        c = x1 ** 2 - x1 ** 2 * p2 - ((p2 - 1) * p3 * x1 ** (p3 + 2) * (p5 - 1)) / (constant_2 * constant)
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0.0:
            p4_1 = (-b + math.sqrt(discriminant)) / (2 * a)
            p4_2 = (-b - math.sqrt(discriminant)) / (2 * a)
            if p4_1 > 0.0:
                deem_variables(p4_1, x1, p2, constant, result_table, branch_points)
            if p4_2 > 0.0:
                deem_variables(p4_2, x1, p2, constant, result_table, branch_points)

        x1 += h

    print('x1     x2         p1          p4')
    number = len(result_table['x1'])
    for i in range(number):
        print(round(result_table['x1'][i], 2), round(result_table['x2'][i], 6),
              round(result_table['p1'][i], 6), round(result_table['p4'][i], 6), sep='   ')

    branch_point_number = len(branch_points['x1'])
    print('\nКоличество точек ветвления =', branch_point_number)

    pyplot.xlabel('p4')
    pyplot.ylabel('p1')
    pyplot.plot(result_table['p4'], result_table['p1'], '.')
    pyplot.xlim(0, 20)
    pyplot.ylim(0, 20)
    pyplot.show()


def deem_variables(p4, x1, p2, constant, result_table, branch_points):
    x2 = (x1 * p2) / (p4 - x1)
    if x2 > 0.0:
        p1 = (x1 * (1 + x2)) / constant
        if p1 > 0.0:
            if x1 - p4 == 0 and x1 * x2 == 0:
                branch_points['x1'].append(x1)
                branch_points['x2'].append(x2)
                branch_points['p1'].append(p1)
                branch_points['p4'].append(p4)
            else:
                result_table['x1'].append(x1)
                result_table['x2'].append(x2)
                result_table['p1'].append(p1)
                result_table['p4'].append(p4)


if __name__ == '__main__':
    main()
