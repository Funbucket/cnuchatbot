from chatbotapp.kakaojsonformat.response import *

def category():
    response_text = "😋제 1학생회관을 선택하셨습니다😋 \n\t\t\t제 1학생회관은\n 푸드코드로 운영되고 있습니다🍽\n\t🍴원하시는 식사 종류를🍴\n\t\t\t 선택해주세요"
    answer = insert_text(response_text)
    reply = make_reply("🍜라면&우동", "라면&우동")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍙간식", "간식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥩양식", "양식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥠스낵", "스낵")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥘한식", "한식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🍛일식", "일식")
    answer = insert_replies(answer, reply)
    reply = make_reply("🥟중식", "중식")
    answer = insert_replies(answer, reply)
    return answer

def ramen():
    response_text = "😋   라면&우동 메뉴입니다   😋\n\t\t 일반라면 : 2,000 \
                    \n\t\t 떡만두라면 : 2,500 \
                    \n\t\t 치즈라면 : 2,500 \
                    \n\t\t 해장라면 : 3,000 \
                    \n\t\t 가락우동 : 2,000 \
                    \n\t\t 꼬치어묵우동 : 3,000 \
                    \n\t\t 새우튀김우동 : 3,000 \
                    \n\t\t 꼬치어묵 : 1,500 \
                    \n\t\t 공기밥 : 500 "
    answer = insert_text(response_text)
    return answer

def gansik():
    response_text = "😋   간식 메뉴입니다   😋\n\t\t 고기만두 : 1,500 \
                    \n\t\t 김치만두 : 1,500 \
                    \n\t\t 떡볶이 : 2,000 \
                    \n\t\t 라볶이 : 3,000 \
                    \n\t\t 치즈라볶이 : 3,500 \
                    \n\t\t 야채김밥 : 1,800 \
                    \n\t\t 소고기김밥 : 2,500 \
                    \n\t\t 참치김밥 : 2,500 \
                    \n\t\t 돈까스김밥 : 3,000 \
                    \n\t\t 추억의도시락 : 3,000 "
    answer = insert_text(response_text)
    return answer

def america():
    response_text = "😋   양식 메뉴입니다   😋\n\t\t 돈까스 : 4,000 \
                    \n\t\t 치즈돈까스 : 4,500 \
                    \n\t\t 치킨스테이크 : 4,000 \
                    \n\t\t 새우튀김오므라이스 : 3,500 \
                    \n\t\t 불닭오므라이스 : 3,500 \
                    \n\t\t 토마토 해물 파스타 : 4,000 "

    answer = insert_text(response_text)
    return answer



def snack():
    response_text = "😋   스낵 메뉴입니다   😋\n\t\t 별리달리 알밥 : 3,900 \
                    \n\t\t 떡갈비추가 : 800 \
                    \n\t\t 수제 떡갈비 버거(단품) : 3,500 \
                    \n\t\t 수제 떡갈비 버거(세트) : 4,500 \
                    \n\t\t\t <버거+감자튀김_콜라> \
                    \n\t\t 콜라//사이다 : 600 \
                    \n\t\t 콜팝치킨 : 2,600 \
                    \n\t\t 치킨커리 샌드위치 : 3,000 \
                    \n\t\t 크리스피 치킨텐더(6PCS) : 3,700 \
                    \n\t\t 크리스피 치킨텐더(세트) : 4,700 \
                    \n\t\t\t <치킨텐더+감자튀김+음료>  \
                    \n\t\t 순살 후라이드 치킨(세트) : 8,400 \
                    \n\t\t 순살 양념치킨(세트) : 9,400  \
                    \n\t\t 순살 반반치킨(세트) : 9,400 "

    answer = insert_text(response_text)
    return answer

def korea():
    response_text = "😋   한식 메뉴입니다   😋\n\t\t 바지락된장찌개 : 4,000 \
                    \n\t\t 불고기비빔밥 : 4,700 \
                    \n\t\t 해물순두부찌개 : 4,200 \
                    \n\t\t 돈육김치찌개 : 4,200 \
                    \n\t\t 부대찌개 : 5,000 \
                    \n\t\t 뚝불고기 : 4,500 "

    answer = insert_text(response_text)
    return answer

def japan():
    response_text = "😋   일식 메뉴입니다   😋\n\t\t 치킨마요덮밥(미니우동) : 3,900 \
                    \n\t\t 제육덮밥(미니우동) : 4,200 \
                    \n\t\t 카츠돈부리(미니우동) : 4,200 \
                    \n\t\t 치킨돈부리(미니우동) : 4,200 \
                    \n\t\t 김치카츠라이스(미니우동) : 4,500 \
                    \n\t\t 카라아게카레(미니우동) : 4,700 \
                    \n\t\t 카츠카레(미니우동) : 4,700 "

    answer = insert_text(response_text)
    return answer

def china():
    response_text = "😋   중식 메뉴입니다   😋\n\t\t 옛날짜장 : 3,900 \
                    \n\t\t 짜장곱배기 : 4,500 \
                    \n\t\t 해물짬뽕 : 4,200 \
                    \n\t\t 짬뽕곱배기 : 4,700 \
                    \n\t\t 짬짜면 : 4,700 \
                    \n\t\t 짬짜면곱배기 : 5,200 \
                    \n\t\t 볶음밥 : 4,500 \
                    \n\t\t 볶음밥곱배기+소스 : 5,000 \
                    \n\t\t 탕수육 : 5,800 \
                    \n\t\t 군만두 : 3,200 \
                    \n\t\t 공기밥(중식) : 500 "
    
    answer = insert_text(response_text)
    return answer