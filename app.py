print("=== 소비 성향 진단과 마케팅 전략 추천 ===")
print("각 질문에 '1'(구매한다) 또는 '2'(3초 이상 고민한다)를 입력하세요.\n")

# 1. 질문들을 담은 [리스트]
questions = [
    "1. 쇼핑 중 마음에 드는 물건이 있다면?",
    "2. 신상 과자가 나왔다는 소식을 들었다면?",
    "3. 필요하진 않지만 마음에 드는 물건을 발견했다면?"
]

score = 0

# 2. 리스트의 질문을 하나씩 꺼내는 [for 반복문]
for q in questions:
    print(q)
    answer = input("선택 (1. 구매한다 / 2. 3초 이상 고민한다): ")
    
    # 3. 1번 선택 시 점수를 누적하는 [if 조건문]
    if answer == "1":
        score += 1
    print()

# 4. 누적된 점수에 따라 결과를 판별하는 [if / elif / else 조건문]
if score == 3:
    tendency = "즉흥적·트렌드 추구형"
    keywords = ["#충동구매", "#신상러버", "#감성소비"]
    strategy = "한정판 출시, 타임 세일, SNS 바이럴 마케팅을 통해 구매 욕구를 즉각 자극하세요."
elif score == 2:
    tendency = "감성적·균형 추구형"
    keywords = ["#가심비", "#트렌드민감", "#합리적감성"]
    strategy = "매력적인 브랜드 스토리와 함께 '첫 구매 할인 쿠폰'으로 마지막 고민을 해결해 주세요."
elif score == 1:
    tendency = "신중한·실용주의형"
    keywords = ["#가성비", "#리뷰중시", "#계획소비"]
    strategy = "실제 구매자의 상세 리뷰, 스펙 비교표, 환불 보장 제도를 강조하여 신뢰를 주세요."
else:
    tendency = "철저한·절약형"
    keywords = ["#무지출챌린지", "#필수재중심", "#초합리주의"]
    strategy = "1+1 묶음 구성, 포인트 적립, 유지비 절감 등 실질적이고 확실한 금전적 이득을 제시하세요."

print("=" * 40)
print(f"총점: {score}점")
print(f"소비 성향: {tendency}")
print(f"추천 키워드: {', '.join(keywords)}")
print(f"마케팅 전략: {strategy}")
print("=" * 40)
