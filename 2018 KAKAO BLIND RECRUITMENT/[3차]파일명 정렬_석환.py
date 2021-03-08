def solution(files):
    answer = []
    new = []
    for file in files:
        head, number = '', ''
        idx = 0
        for i in range(len(file)):
            if not file[i].isnumeric():
                head += file[i]
            else:
                idx = i
                break
        for j in range(idx,len(file)):
            idx = j+1
            if file[j].isnumeric():
                number += file[j]
            else:
                idx = j
                break
        tail = file[idx:]
        new.append((head,number,tail))
    new.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for s in new:
        answer.append("".join(s))

    return answer

print(solution(["img010","img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))