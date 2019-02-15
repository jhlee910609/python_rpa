# [ 내장함수 익히기 ]
# 1. count : 특정 문자의 개수 반환
data = "you can do it"
print("count => " + str(data.count("o")))

# 2. find : 특정 문자의 위치 반환
print("find => " + str(data.find("do")))

# 3. upper & lower : 전체 문자열을 대/소문자로 변경
print("upper => " + data.upper() + "\nlower => " + data.lower())

# 4. replace : 특정 문자열 변환 (찾아 바꾸기 기능)
print("replace => ")