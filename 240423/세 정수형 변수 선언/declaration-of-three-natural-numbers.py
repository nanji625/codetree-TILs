# 변수에 담긴 값을 원하는 형식에 맞춰 출력하기 위해서는 크게 3가지 방법을 사용할 수 있습니다.


# 1. 변수 포맷(%d, %s, ...)과 %를 사용

# 다음과 같이 문자열에 해당 변수의 type에 해당하는 포맷을 적어주고,
# 맨 뒤에는 % 뒤에 변수를 나열하는 식으로 포맷을 맞출 수 있습니다.
# 2개 이상의 변수를 한 문자열에 넣기 위해서는, 소괄호()로 감싸 순서대로 변수들을 나열하면 됩니다.

# python3 코드
# a = 5
# print("A is %d" % a)

# b = "apple"
# print("B is %s" % b)

# print("A is %d and B is %s" % (a, b))

# 출력결과
# A is 5
# B is apple
# A is 5 and B is apple

# 변수 포맷은 문자열의 경우 %s를, 문자의 경우 %c를, 정수의 경우 %d, 실수의 경우 %f 등이 가능합니다.


# 2. format 함수를 이용

# format 함수를 이용하면 직접 변수의 type을 명시하지 않더라도,
# 순서 혹은 이름을 명시하여 원하는 변수를 포맷에 맞춰 넣어줄 수 있습니다.
# 숫자를 적게되는 경우에는 format 함수에 적게되는 변수에 번호를 0번부터 붙였을 때 몇 번째 값인지를 명시하는 것입니다.
# 숫자 대신 새로운 이름을 붙여 적는 것도 가능합니다.
# format을 이용하는 경우에는 꼭 문자열 내 변수를 사용할 위치에 {}로 감싸줘야 합니다.

# python3 코드
# a, b = 5, "apple"

# print("A is {0}".format(a))
# print("A is {new_a}".format(new_a=a))

# print("B is {0}".format(b))
# print("B is {new_b}".format(new_b=b))

# print("A is {0} and B is {1}".format(a, b))
# print("A is {new_a} and B is {new_b}".format(new_a=a, new_b=b))
# print("B is {1} and A is {0}".format(a, b))
# print("B is {new_b} and A is {new_a}".format(new_a=a, new_b=b))

# 출력결과
# A is 5
# A is 5
# B is apple
# B is apple
# A is 5 and B is apple
# A is 5 and B is apple
# B is apple and A is 5
# B is apple and A is 5


# 3. f 문자열 포맷을 이용

# python 3.6부터는 f 문자열 포맷을 이용할 수 있습니다.

# 변수 이름을 그대로 문자열에 쉽게 옮길 수 있는 방법으로,
# format 함수와 유사하지만 별도의 함수 이용 없이 문자열 앞에 f를 붙이고 변수 이름을 중괄호{}로 감싸면
# 원하는 변수를 해당 위치에 넣어줄 수 있게 됩니다.

# python3 코드
# a, b = 5, "apple"

# print(f"A is {a}")
# print(f"B is {b}")
# print(f"A is {a} and B is {b}")

# 출력결과
# A is 5
# B is apple
# A is 5 and B is apple

# --------------------------------------------------------------------------------------------

a = 7
b = 23

# print(f'{a} + {b} =', a+b)
# print('%d + %d ='%(a, b), a+b)
# print('{} + {} ='.format(a, b), a+b)
print('{1} + {0} ='.format(b, a), a+b)