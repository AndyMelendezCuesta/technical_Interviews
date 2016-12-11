#Question1

def get_hash(string):
    primes26 = [5, 71, 79, 19, 2, 83, 31, 43, 11, 53, 37, 23, 41,
                3, 13, 73, 101, 17, 29, 7, 59, 47, 61, 97, 89, 67]
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    hash_table = {}
    for i, letter in enumerate(alphabet):
        hash_table[letter] = primes26[i]
    hash_number = 0
    for letter in list(string):
        hash_number *= hash_table[letter]
    return hash_number


def question1(s, t):
    if s == t:
        return True
    elif s == '' or t == '':
        return False
    else:
        t_hash_number = get_hash(t)
        for i in range(len(s) - len(t)):
            s_hash_number = get_hash(s[i:i+len(t)])
            if s_hash_number == t_hash_number:
                return True
        return False
        
print 'Test Cases for Question 1:'

print question1('', '')
# Should print True

print question1('', 'a')
# Should print False

print question1('a', '')
# Should print False

print question1('udacity', 'udacity')
# Should print True

print question1('udacity', 'ad')
# Should print True

print question1('abcdefghijklmnopqrstuvwxyz', 'udacity')
# Should print True

#Question2

def question2(a):
    if len(a) <= 1:
        return a

    longest = ""
    for i in range(len(a)):
        for j in range(0, i):
            substring = a[j:i+1]
            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring
    if len(longest) == 0:
        return a[0]
    return longest

print 'Test Cases for Question 2:'

print question2('a')
# Should print 'a'

print question2('')
# Should print ''

print question2('abc')
# Should print 'a'

print question2('aba')
# Should print 'aba'

print question2('abcba')
# Should print 'abcba'

print question2("forgeeksskeegfor")
# Should print 'geeksskeeg'

print question2("bqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektskcqcpeqdwwucymgvyrekts"
                "wenfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoirmcjrhqcyzvekzqlx"
                "gddjowzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjrmwqaqsdcgycdupy"
                "kppiyhwrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnzudfweormatjyc"
                "ujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihaqwertyuiopabcdefahpyyphafedcbapoiuy"
                "trewqzudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhciharmwqaqsdcgycdupy"
                "kppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnndjqdrkljawzasriouuiqkcwwqsxifbndjmypr"
                "dozhwaoibpqrthpcjphgsjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgm"
                "ehycdvxdorpepmvcynfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoirm"
                "cjrhqcyzvekzqlxgddjbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektskcq"
                "cpeqdwwucymgvyrektswe")
# Should print 'qwertyuiopabcdefahpyyphafedcbapoiuytrewq'

#Question3
def question3(G):
    if len(G) < 1:
        return G
    nodes = set(G.keys())
    mst = {}
    start = G.keys()[0]
    mst[start] = []

    while len(mst.keys()) < len(nodes):
        min_w = float('inf')
        min_edge = None
        for node in mst.keys():
            edges = [(weight, vertex) for (vertex, weight) in G[node] if vertex not in mst.keys()]
            if len(edges) > 0:
                w, v = min(edges)
                if w < min_w:
                    min_w = w
                    min_edge = (node, v)
        mst[min_edge[0]].append((min_edge[1], min_w))
        mst[min_edge[1]] = [(min_edge[0], min_w)]
    return mst


print 'Test Cases for Question 3:'

print question3({})
# Should print {}

print question3({'A': []})
# Should print {'A': []}

print question3({'A': [('B', 3), ('E', 1)],
                 'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
                 'C': [('B', 9), ('D', 3), ('E', 7)],
                 'D': [('B', 2), ('C', 3)],
                 'E': [('A', 1), ('B', 2), ('C', 7)]})
# Should print
# {'A': [('E', 1)],
#  'C': [('D', 3)],
#  'B': [('E', 2), ('D', 2)],
#  'E': [('A', 1), ('B', 2)],
#  'D': [('B', 2), ('C', 3)]}

print question3({'A': [('B', 7), ('D', 5)],
                 'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
                 'C': [('B', 8), ('E', 5)],
                 'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
                 'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
                 'F': [('D', 6), ('E', 8),  ('G', 11)],
                 'G': [('E', 9), ('F', 11)]})
# Should print
# {'A': [('D', 5), ('B', 7)],
#  'C': [('E', 5)],
#  'B': [('A', 7), ('E', 7)],
#  'E': [('B', 7), ('C', 5), ('G', 9)],
#  'D': [('A', 5), ('F', 6)],
#  'G': [('E', 9)],
#  'F': [('D', 6)]}


#Question4

def question4(T, r, n1, n2):
    if len(T) == 0:
        return T
    elif len(T) == 1:
        return r
    a1 = None
    parent1 = []
    while a1 != r:
        for a in range(len(T)):
            if T[a][n1] == 1:
                a1 = a
                n1 = a1
                parent1.append(a1)
    a2 = None
    parent2 = []
    while a2 != r:
        for a in range(len(T)):
            if T[a][n2] == 1:
                a2 = a
                n2 = a2
                parent2.append(a2)
    for a1 in parent1:
        for a2 in parent2:
            if a1 == a2:
                return a1
                
print 'Test Cases for Question 4:'

print question4([],
                None,
                None,
                None)
# Should print []
print question4([[0]],
                0,
                0,
                0)
# Should print 0
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4)
# Should print 3
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                1,
                0,
                6)
# Should print 2

#Question5

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    if ll:
        length = 1
        node = ll
        while node.next:
            node = node.next
            length += 1
        if m < length:
            n = length - m
            i = 0
            node = ll
            while i < n:
                node = node.next
                i += 1
        else:
            return None
    else:
        node = ll
    return node.data
    

e0 = Node(None)
print question5(e0, 1)
# Should print None

e0 = Node(0)
print question5(e0, 4)
# Should print None

e0 = Node(0)
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e0.next = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
print question5(e0, 8)
# Should print None

e0 = Node(0)
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
e7 = Node(7)
e8 = Node(8)
e0.next = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8
print question5(e0, 3)
# Should print 6
