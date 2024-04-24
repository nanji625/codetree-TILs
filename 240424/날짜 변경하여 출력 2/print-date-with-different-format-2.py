import sys

# mm, dd, yyyy = map(int, sys.stdin.readline().split('-'))

date = sys.stdin.readline().split('-')
mm = date[0]
dd = date[1]
yyyy = date[2]

print('{2}.{0}.{1}'.format(mm, dd, yyyy))