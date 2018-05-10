
import queue
sample = ['opz', 'ij', 'abc', 'def', 'gh', 'kl', 'mn', 'prs', 'tuv', 'wxy']

class Node:
    def __init__(self):
        self.child = dict()
        self.level = 0
        self.count_leaf = 0
def convert_word_to_digit(word):
    digits = ""
    for w in word:
        for i_s in range(len(sample)):
            if sample[i_s].find(w) != -1:
                digits += str(i_s)
    return digits

def add_word(root, digits):
    temp = root
    for digit in digits:
        if digit in temp.child:
            temp = temp.child[digit]
        else:
            temp.child[digit] = Node()
            level = temp.level
            temp = temp.child[digit]
            temp.level = level + 1
    temp.count_leaf += 1

def find_word(root, digits):
    index = []
    temp = root
    for digit in digits:
        if digit not in temp.child:
            return False
        temp = temp.child[digit]
        if isWord(temp):
            index.append(temp.level)
        if isEmpty(temp):
            break
    return index

def isWord(node):
    return node.count_leaf != 0

def isEmpty(node):
    return len(node.child) == 0

def DFS(root, digits):
    q = queue.Queue()
    q.put(root)
    stack = list()
    res = []
    index = 0
    while not q.empty():
        top = q.get()
        for child in top.child:
            if child == digits[index]:
                temp = child
                stack.append(top.child[child])
                index += 1
                while len(stack) > 0:
                    current = stack.pop()
                    for ch_current in current.child:
                        if ch_current == digits[index]:
                            temp += ch_current
                            if current.child[ch_current].count_leaf > 0:
                                res.append(temp)
                            stack.append(current.child[ch_current])
                            index = index + 1 if index < len(digits) - 1 else index
            else:
                q.put(top.child[child])
    return res

while True:
    num = input().strip()
    if num[0] == "-":
        break
    root = Node()
    n = len(num)
    d = int(input().strip())
    words = dict()
    for _ in range(d):
        word = input().strip()
        di = convert_word_to_digit(word)
        words.setdefault(di, word)
        add_word(root, di)
    for an in DFS(root, num):
        print(an)