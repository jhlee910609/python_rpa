# [ 내장함수 익히기 ]
# 1. count : 특정 문자의 개수 반환
data = "you can do it!"
print("count => " + str(data.count("o")))

# 2.find : 특정 문자의 위치 반환
print("find => " + str(data.find("do")))

# 3.upper & lower : 전체 문자열을 대/소문자로 변경
print("upper => " + data.upper() + "\nlower => " + data.lower())

# 4.replace : 특정 문자열 변환 (찾아 바꾸기 기능)
print("replace => " + data.replace(" ", "_"))

# 5.split : 특정 구분자로 문자열 분리하여 배열 형태로 반환
data_splited = data.split(" ")
print(data_splited)

# 6. join : 문자열 배열에 구분점 넣어 완성된 하나의 문자열 반환
print(", ".join(data_splited))

# 7. isDigit : 숫자로만 이뤄져 있는지
print(data.isdigit())

# 8. 문자열 포메팅
name = "junhee"
str = "My name is %s, and I'm %d years old"%(name, 29)
print(str)