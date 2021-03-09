def solution(word, pages):
    l = len(word)
    urls = []
    basic = []
    out = [[] for _ in range(len(pages))]
    out_link = [[] for _ in range(len(pages))]
    out_score = [[] for _ in range(len(pages))]

    for i in range(len(pages)):
        for j in range(len(pages[i])):
            # urls 찾기
            if pages[i][j:j+23] == '<meta property="og:url"':
                for k in range(j+23,len(pages[i])):
                    if pages[i][k:k+8] == 'https://':
                        for z in range(k+9,len(pages[i])):
                            if pages[i][z:z+1] == '"':
                                urls.append(pages[i][k-1:z+1])
                                break
                        break

            # 기본점수 및 외부링크 찾기
            if pages[i][j:j+6] == '<body>':
                basic_score = 0
                for k in range(j+7,len(pages[i])):
                    if pages[i][k:k+7] == '</body>':
                        basic.append(basic_score)
                        break
                    if pages[i][k:k+l].lower() == word.lower() and not pages[i][k:k+l+1].isalpha() and not pages[i][k-1:k].isalpha():
                        basic_score += 1
                    if pages[i][k:k+8] == '<a href=':
                        for z in range(k+9,len(pages[i])):
                            if pages[i][z:z+1] == '"':
                                out[i].append(pages[i][k+8:z+1])
                                break
                break

    # 해당 페이지로 링크 걸린 페이지 찾기
    for i in range(len(out)):
        for link in out[i]:
            idx = 0
            for url in urls:
                if url == link:
                    out_link[idx].append(i)
                else:
                    idx += 1

    # 기본점수 + 링크점수
    for i in range(len(out_score)):
        score = basic[i]
        for link in out_link[i]:
            score += basic[link] / len(out[link])
        out_score[i].append(score)

    return out_score.index(max(out_score))

print(solution('blind',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi',["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))