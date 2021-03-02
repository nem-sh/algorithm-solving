n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    ans = []

    for i in range(n):
        num = arr1[i]
        num2 = arr2[i]
        new = ''
        new2 = ''
        while len(new) != n and len(new2) != n:
            a = num % 2
            num //= 2
            new = str(a) + new
            a2 = num2 % 2
            num2 //= 2
            new2 = str(a2) + new2
        arr1[i] = new
        arr2[i] = new2

    for i in range(n):
        ans.append("")
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                ans[i] = ans[i] + "#"
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                ans[i] = ans[i] + " "

    return ans

print(solution(n,arr1,arr2))