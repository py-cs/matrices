class Matrix:
    def __init__(self, size=None, n=""):
        self.ok = True
        if size:
            (self.rows, self.columns) = size
        else:
            rows, columns = input("Enter size of " + n + "matrix:").split()
            self.rows, self.columns = int(rows), int(columns)
            self.size = (self.rows, self.columns)
            print("Enter " + n + "matrix")
            self.elements = [[num(e) for e in input().split()] for _ in range(self.rows)]

    def column(self, i):
        return list([self.elements[j][i] for j in range(self.rows)])

    def __str__(self):
        if not self.ok:
            return "The operation cannot be performed."
        return "The result is:\n" + "\n".join([' '.join([f"{round(x, 3):>7}"
                                                         for x in row]) for row in self.elements])

    def const_multi(self, const):
        self.elements = [[const * e for e in row] for row in self.elements]
        return self

    def add(self, add_m):
        if self.size == add_m.size:
            for r in range(self.rows):
                for c in range(self.columns):
                    self.elements[r][c] += add_m.elements[r][c]
            return self
        else:
            self.ok = False

    def multiply(self, mult_m):
        if self.columns == mult_m.rows:
            tmp = []
            for r in range(self.rows):
                row = []
                for c in range(mult_m.columns):
                    row.append(sum(map(lambda x, y: x * y, self.elements[r], mult_m.column(c))))
                tmp.append(row)
            self.elements = tmp
            return self
        else:
            self.ok = False

    def transp_main(self):
        self.elements = [[x for x in self.column(i)] for i in range(self.columns)]
        return self

    def transp_side(self):
        self.elements = [[x for x in reversed(self.column(i - 1))] for i in range(self.columns, 0, -1)]
        return self

    def transp_vertical(self):
        self.elements = [reversed(row) for row in self.elements]
        return self

    def transp_horisontal(self):
        self.elements = [row for row in reversed(self.elements)]
        return self

    def minor(self, row, column):
        m_minor = Matrix(size=(self.rows - 1, self.columns - 1))
        m_minor.elements = [self.elements[r][:column] + self.elements[r][column + 1:]
                            for r in range(len(self.elements)) if r != row]
        return m_minor

    def cofactor(self, row, column):
        return (-1) ** (row + column) * self.minor(row, column).determinant()

    def determinant(self):
        if self.rows == self.columns:
            if len(self.elements) == 1:
                return self.elements[0][0]
            return sum(map(lambda i: self.elements[0][i] * self.cofactor(0, i), [i for i in range(self.rows)]))
        else:
            self.ok = False

    def inverse(self):
        if self.rows == self.columns and self.determinant():
            d = self.determinant()
            self.elements = [[self.cofactor(r, c) for c in range(self.columns)] for r in range(self.rows)]
            self.transp_main().const_multi(1 / d)
            return self
        else:
            self.ok = False


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


while True:
    print('1. Add matrices\n2. Multiply matrix by a constant\n'
          '3. Multiply matrices\n4. Transpose matrix\n'
          '5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    choice = int(input("Your choice: "))

    if choice == 0:
        break
    elif choice == 1:
        print(Matrix(n="first ").add(Matrix(n="second ")))
    elif choice == 2:
        print(Matrix().const_multi(int(input("Enter constant:"))))
    elif choice == 3:
        print(Matrix(n="first ").multiply(Matrix(n="second ")))
    elif choice == 4:
        print('1. Main diagonal\n2. Side diagonal\n'
              '3. Vertical line\n4. Horizontal line\n0. Exit')
        choice = int(input("Your choice: "))
        if choice == 1:
            print(Matrix().transp_main())
        elif choice == 2:
            print(Matrix().transp_side())
        elif choice == 3:
            print(Matrix().transp_vertical())
        else:
            print(Matrix().transp_horisontal())
    elif choice == 5:
        print(f"The result is:\n{Matrix().determinant()}")
    elif choice == 6:
        print(Matrix().inverse())
    print()
