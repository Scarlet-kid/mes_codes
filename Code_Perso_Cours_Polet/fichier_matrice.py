"""from code_builtMat import buildMat

mat = buildMat(4,10)
with open ('mat.txt', 'w+') as f:
    for i in range(0,len(mat)):
        for j in range(0, len(mat[i])):
            f.write(str(mat[i][j]) + "\t")
        f.write("\n")"""

mat = []
with open ("essai.txt", "r") as f:
    for li in f:
        s = li.strip("\n\r")
        l = s.split(";")
        mat.append(l)

print(mat)