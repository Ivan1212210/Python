# TODO решите задачу
def task() -> float:
    f = open('input.json', 'r')
    a = f.readlines()
    sum_ = 0
    first = 0
    second = 0
    for i in range(len(a)):
        if a[i].find("score") != -1:
            first = float(a[i][((a[i].find("score"))+8):len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            second = float(a[i][((a[i].find("weight")) + 9):len(a[i]) - 1])
        if first * second != 0:
            sum_ += first * second
            first = 0
            second = 0
    f.close()
    return round(sum_, 3)


print(task())
