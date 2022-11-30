import matplotlib.pyplot as plt


def table1():
    data = {'Tester 1': 2, 'Tester 2': 3.5, 'Tester 3': 4,
            'Tester 4': 2.5, 'Tester 5': 3}
    testers = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(testers, values, color='blue',
            width=0.4)

    plt.xlabel("Testers of the application")
    plt.ylabel("Minutes")
    plt.title("Time to complete scenario")
    plt.show()


def table2():
    data = {'Tester 1': 2, 'Tester 2': 4, 'Tester 3': 7,
            'Tester 4': 3, 'Tester 5': 4}
    testers = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(testers, values, color='green',
            width=0.4)

    plt.xlabel("Testers of the application")
    plt.ylabel("Errors")
    plt.title("How many navigation errors were made")
    plt.show()


if __name__ == '__main__':
    table1()
    table2()
