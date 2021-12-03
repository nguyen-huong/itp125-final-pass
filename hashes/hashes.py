import hashlib
import sys

sys.stdout = open('hashes.txt', 'a')

#hexdigest()
with open("pass.txt") as h:
    for line in h:
        print(hashlib.md5(line.rstrip().encode()).hexdigest())

    sys.stdout.close()