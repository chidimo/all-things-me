
import sys
print('=======Welcome to the shell========')
print('  --' * 10)
i = 0
for line in sys.stdin:
    print('line {:<2} ====: {}'.format(i, line))
    i += 1
    print('Done')
    print('{} lines were read'.format(i))