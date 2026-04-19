""" -wsl
python3 make_input.py ./[DIR] [NUM]
"""

import random
import sys
import os

if len(sys.argv) < 3:
    print("Usage: python make_input.py <output_dir> <count> [seed]")
    sys.exit(1)

out_dir = sys.argv[1] + "/input"
count = int(sys.argv[2])
if len(sys.argv) > 3:
    random.seed(int(sys.argv[3]))

os.makedirs(out_dir, exist_ok=True)
"""
for i in range(1, count + 1):
    lim = 10**(int(i/50)+2);
    a = random.randint(1, lim)
    b = random.randint(1, lim)
    c = random.randint(1, lim)
    with open(os.path.join(out_dir, f"{i}.txt"), "w") as f:
        f.write(f"{a} {b} {c}\n")
"""
for i in range(1, count + 1):
    n = i;
    with open(os.path.join(out_dir, f"{i}.txt"), "w") as f:
        f.write(f"{n}\n")

print(f"Generated {count} files in {out_dir}")