import subprocess
from random import shuffle

arr = [i for i in range(1, 262144 + 1)]
shuffle(arr)

data = "262144\n"+" ".join(map(str, arr))
subprocess.run("pbcopy", universal_newlines=True, input=data)
