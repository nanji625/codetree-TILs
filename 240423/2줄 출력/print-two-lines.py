print('Hello\nWorld')

# python3에서 print 함수를 사용하면, 기본으로 줄바꿈이 됩니다.

# 코드는 기본적으로 위에서부터 아래 방향으로 순차적으로 실행되기 때문에, 다음 코드를 실행하게 되면 출력 결과가 다음과 같이 2줄에 걸쳐 나오게 됩니다.

# python3 코드
# print("Hello World")
# print("Python is Fun")
# 출력결과
# Hello World
# Python is Fun
# 그러면 print를 한 번만 이용하여 해결할 수는 없을까요?

# \n 문자를 이용하면 가능합니다. \n 문자는 new line을 의미하는 문자로, 이는 한 줄을 띈다는 것을 특수문자이기 때문에, 다음과 같이 문자열 출력시 해당 문자를 사용하게 되면 한 줄이 띄어지게 됩니다.

# python3 코드
# print("Hello World\nPython is Fun")
# 출력결과
# Hello World
# Python is Fun
# 2줄 출력을 하는 또 다른 방법이 있습니다. 바로 다음과 같이 """ 혹은 '''를 이용하는 것입니다. 큰 따옴표나 작은 따옴표를 연속으로 3개 사용하는 경우에는, 여러 줄에 해당하는 문자열을 한번에 담을 수 있습니다.

# python3 코드
# print("""Hello World
# Python is Fun""")
# 출력결과
# Hello World
# Python is Fun
# 다만 여기서 주의해야 할 점은, 다음과 같이 코드를 작성하게 되면 맨 위 줄과 맨 아래 줄에도 한 줄씩 띄어지기 때문에 예상과 다른 결과가 나오게 된다는 것입니다. 따옴표 3개를 사용하여 여러 줄을 한번에 묶어 출력하는 경우에는 꼭 상단에서 처럼 위아래 여백 없이 작성을 해줘야합니다.

# print("""
# Hello World
# Python is Fun
# """)
# 출력결과
# -> 처음 한 줄 띄어짐
# Hello World
# Python is Fun
# -> 마지막 줄도 띄어짐