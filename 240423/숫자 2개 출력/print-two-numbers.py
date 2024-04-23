print(3, end = ' ')
print(5)

# 2개의 값을 공백을 사이에 두고 출력하기 위해서는 다음과 같이 print 함수에 2개의 값을 ,를 사이에 두고 넣어주면 됩니다.

# python3 코드
# print(3, 5)

# 출력결과
# 3 5

# 만약 공백을 사이에 두고 출력하고 싶은게 아니라면, 구분자로 사용할 값을 sep를 이용하여 직접 설정해 줄 수 있습니다. sep 설정이 따로 없을 때는 자동으로 공백으로 설정됩니다.

# print(3, 5)                  -> 3 5
# print(3, 5, sep=":")         -> 3:5
# print(3, 5, sep=" ")         -> 3 5

# 만약 다음과 같이 코드를 작성하면 결과가 어떻게 될까요?
# 2개의 숫자가 공백을 사이에 두고 나오는 것이 아닌, 줄 단위로 나오게 될 것입니다.

# python3 코드
# print(3)
# print(5)

# 출력결과
# 3
# 5

# 그렇다면 위의 경우처럼 print 함수를 2번 사용하되, 공백을 사이에 두고 출력할 수 있는 방법은 없는 걸까요?

# 방법이 있습니다. 바로 print 함수 실행시마다 자동으로 new line으로 넘어가는 것을 막으면 됩니다.

# print 함수를 이용할 때 새로운 줄로 이동하는 이유는 실은 end라는 값에 \n문자가 기본으로 들어가있기 때문입니다. 따라서 다음과 같이 첫 번째 print 함수의 end라는 값을 공백을 의미하는 ' ' 문자로 변경해주면, 첫 번째 print함수에 있는 값을 실행한 후 \n에 해당하는 줄바꿈을 진행하는 것이 아닌 ' '를 출력하게 되므로 공백을 대신 출력해주게 됩니다. 따라서 공백을 사이에 두고 2개의 값이 출력됩니다.

# python3 코드
# print(3, end=" ")
# print(5)
# 출력결과
# 3 5