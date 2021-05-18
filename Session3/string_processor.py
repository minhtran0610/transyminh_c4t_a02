class StringProcessor:
    def __init__(self):
        self.stack = []

    def reverse(self, a):
        return (str(a)[::-1])

    def process_sequence(self, b):
        temp = []
        li = []
        result = ""
        for v in b:
            if v == "*":
                letter = temp.pop()
                li.append(letter)
            else:
                temp.append(v)
        for i in range(len(li)):
            result += str(li[i])
        return result

    def binary_string(self, dec_int):
        s = ""
        mid = dec_int
        r = 0
        if mid == 0:
            s = "0"
        while mid > 0:
            r = mid % 2
            mid = mid // 2
            s += str(r)
        return StringProcessor.reverse(self,s)

    def is_balanced(self, s):
        balanced = True
        wait = []
        for v in s:
            if v == "(" or v == "[" or v == "{":
                wait.append(v)
            elif v ==  ")" or v == "]" or v == "}":
                if len(wait) == 0:
                    balanced = False
                    break
                else:
                    if wait[len(wait)-1] == "(" and v == ")":
                        wait.pop()
                    elif wait[len(wait)-1] == "{" and v == "}":
                        wait.pop()
                    elif wait[len(wait)-1] == "[" and v == "]":
                        wait.pop()
                    else:
                        balanced = False
                        break
            else:
                pass
        if balanced and len(wait) > 0:
            balanced = False
        else:
            pass
        return balanced
