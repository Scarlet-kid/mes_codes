def buildMat(row: int, column: int) -> list:
    mat = []
    for lig in range(0, row):
        mat.append([None] * column)
    return mat
# Bon code