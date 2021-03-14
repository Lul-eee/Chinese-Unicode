import random
import string
import sys
from cjktable import *
num = int(sys.argv[1])
result = ''.join(random.choice(uni_chinese) for _ in range(num))
with open('output.rtf', 'w') as f:
    print(result, file=f)
