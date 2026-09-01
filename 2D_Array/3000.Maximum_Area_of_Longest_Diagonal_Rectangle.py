def areaOfMaxDiagonal(dimensions):
        n = len(dimensions)
        diagonal = []

        for i in range(n):
            l = dimensions[i][0]
            w = dimensions[i][1]

            dia = (l * l) + (w * w)
            diagonal.append(dia)

        max_diagonal = max(diagonal)
        
        max_area = 0

        for i in range(n):
            if diagonal[i] == max_diagonal:
                l = dimensions[i][0]
                w = dimensions[i][1]

                area = l * w

                if area > max_area:
                    max_area = area

        return max_area

print(areaOfMaxDiagonal(dimensions = [[9,3],[8,6]]))
print(areaOfMaxDiagonal(dimensions = [[3,4],[4,3]]))