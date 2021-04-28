from classTest import JustTest

tmpList=[1, 2, 3]

print(JustTest.class_attr) # 5 <- 객체 안찍어도 클래스 attr은 존재한다

JustTest.class_attr = 11

print(JustTest.class_attr) # 11 <- 수정 가능

print(tmpList) # [1, 2, 3]

JustTest.lst_ones_plus(tmpList) # call by ref ok

print(tmpList) # [101, 2, 3]

print("초기화 한 JustTest.class_list =", JustTest.class_list)

justTest = JustTest(setInt=10) # myint에 10 지정

# print("인스턴스인데 셀프 뺀거", justTest.inst_attr)
print("셀프 붙인건데 안붙인거를 덮어씀", justTest.instAttr)

print("스태틱 메소드로 인스턴스 필드 조작", justTest.myInt) # 100 되는구나..
