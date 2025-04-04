"""com"""
class Node:
    """işlem"""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"

    def comp(self):
        """compile etme"""
        left = int(self.left) if isinstance(self.left, int) else self.left.comp()
        right = int(self.right) if isinstance(self.right, int) else self.right.comp()
        match self.op:
            case '+': return left + right
            case '-': return left - right
            case '*': return left * right
            case '/': return 0 if right == 0 else (left / right)
            case '^': return left ** right
class Token:
    """temel tokenları temsil eder, T(değer, tip)."""
    def __init__(self, value, typ):
        self.value = value
        self.typ = typ  # 'int', 'op', 'paren'
    def __repr__(self):
        return f"T({self.value}, {self.typ})"

def tokenizer(s: str):
    """string ifadeleri tokenlara ayırır"""
    tok = []
    s = s.strip()

    i = 0
    while i < len(s):
        if s[i].isdigit():
            # Sayılar
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            tok.append(Token(num, "int"))

        elif s[i] in "+-*/^":
            # operatör
            tok.append(Token(s[i], "op"))
            i += 1

        elif s[i] in "()":
            # Parantez
            tok.append(Token(s[i], "paren"))
            i += 1

        else:
            # Geçersiz karakterleri atlama
            i += 1

    return tok


def factor(s):
    """Tek sayı veya parantez içindeki ifade"""
    if s and s[0].value == "(":
        res, s = expr(s[1:])
        return res, s[1:]  # Kapatma parantezini atla
    elif s and s[0].typ == "int":
        return s[0].value, s[1:]
    else:
        return 0, s  # Geçersiz durumda 0 döndür

def term(s):
    """Çarpma ve bölme"""
    res, s = factor(s)
    while s and s[0].value in "*/":
        op = s[0].value
        n, s = factor(s[1:])
        res = Node(res, op, n)
    return res, s

def expr(s):
    """Toplama ve çıkarma"""
    res, s = term(s)
    while s and s[0].value in "+-":
        op = s[0].value
        n, s = term(s[1:])
        res = Node(res, op, n)
    return res, s
print("'ctrl + z' ile çıkış yapabilirsiniz")
while True:
    a=input(">>> ")
    a=tokenizer(a)
    a=expr(a)
    print(a[0].comp())
