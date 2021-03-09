def solution(files):
    answer = []
    tmp = []
    for file in files:
        head, number = '', ''
        for f in file:
            if not f.isnumeric() and not number:
                head += f
            if f.isnumeric():
                number += f
            if not f.isnumeric() and number:
                break
        tmp.append([head, number, files.index(file)])
    tmp = sorted(tmp, key=lambda x : (x[0].lower(), int(x[1])))
    for i in tmp:
        answer.append(files[i[2]])
    return answer
