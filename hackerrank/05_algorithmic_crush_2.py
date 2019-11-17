
import pandas as pd

p = input()
parts = p.split()
N = int(parts[0])
M = int(parts[1])
df = pd.DataFrame([0]*N)

for i in range(M):
    z = input()
    operands = z.split()
    a = int(operands[0])
    b = int(operands[1])
    k = int(operands[2])
    
    mapping = [x for x in range(a, b+1)]
    df[df.index.isin(mapping)] += 100
    print(df)
    print()
print(int(df.max()))