

"""
#O(n^2)
for node in range(graph) #O(n)
    #O(n)
    -do a depth first search on each node until we reach the sink node  
    once we have possible paths for each node to sink node 
 
    #O(n^2)
    -if there are any paths, i.e there is more than one node then: 
        -get associated letters in graph_letters with path, 
        the letters will be stringed together according to the route
        in each path. So, if nodes 2->3->4 correlated to 
        a,b,c. Then we would get the string 'abc'
        
        #O(n^2)
        -while each word has at least one letter check if word is a 
        palindrome. for each loop we will cut the last letter off
        of each word and check for palindrome. The idea behind this
        is that since we are getting words associated to paths in our 
        dfs we need to make sure we check for potential palindromes
        in the word. So for example, hannahtgt is not a palindrome
        but if you keep cutting off the end eventually you get 
        hannah, which is a palindrome
 
    #O(n)
    -if there are any palindromes then 
        filter out any empty values and then 
        return the length of the longest palindrome. 
 
    -else return none

"""
"""
I ned to go down a branch until i hit a sink
so for example s->o->n->y->h->t and then s->o->d->a->h->t etc. Once I have hit the end for each node I will add all possible paths to a list and then check if any
are palindromes and all sub parts of that path. So check if sonyht is a palindrome and then check sonyh, then sony, etc until I get through the word. If any fit
the condition to be a palindrome, exluding one letter words, then I will add it to the list of palindromes. I will repeate this for each node in the graph and then 
return the lognest palindroms length
"""
#O(n^2)
def length_of_largest_palindrome(graph_letters, graph_connectiong):
    result = find_largest_palindrome(graph_letters, graph_connectiong) #O(n^2)
    if(result):
        return len(result) #O(1)
    return 0

#O(n^2)
def find_largest_palindrome(graph_letters, graph_connectiong):
    list_of_palindromes = []
    #from 46-55 should be O(n^2)
    for node in range(len(graph_connectiong)):#O(n)
        paths = dfs(graph_connectiong, [node], [], node) #O(n)
        if (paths):
            possible_palindromes = get_letters(graph_letters, paths) #O(n^2)
            "found how to get the max string from https://www.geeksforgeeks.org/python-longest-string-in-list/"
            #from 51-54 should be O(n^2)
            while len(max(possible_palindromes, key = len)) > 0: #(n)
                list_of_palindromes.append(check_for_palindrome(possible_palindromes)) #O(n)
                for index, word in enumerate(possible_palindromes): #O(n)
                    possible_palindromes[index] = word[:-1]
    if(len(list_of_palindromes)) > 0:
        "found filter funciton at https://www.geeksforgeeks.org/python-remove-none-values-from-list/"
        list_of_palindromes = list(filter(None, list_of_palindromes)) #O(n)
        return max(list_of_palindromes, key = len)
    return None


def dfs(graph_connectiong, stack, component, node):
    if len(graph_connectiong[node]) == 0:
        return component.append(stack)
    else:
        for child in graph_connectiong[node]:
            stack.append(child)
            dfs(graph_connectiong, list(stack), component, child)
            stack.pop()
    return component

def get_letters(graph_letters, paths): #O(n^2)
    list_of_words = []
    indavidual_word = ""
    for node in range(len(paths)): #O(n)
        list_of_words.append(indavidual_word)
        indavidual_word = ""
        for path_child in paths[node]: #O(n)
            indavidual_word += graph_letters[path_child][0]
    list_of_words.append(indavidual_word)
    return list_of_words[1:]

def check_for_palindrome(possible_palindromes): #O(n)
    node = 0
    list_of_palindromes = []
    while node < len(possible_palindromes): #O(n)
        foward_word = possible_palindromes[node]
        reversed_word = ''.join(reversed(possible_palindromes[node]))
        if len(foward_word) > 1 and foward_word == reversed_word:
            list_of_palindromes.append(foward_word)
        node += 1
    if len(list_of_palindromes) > 0:
        return max(list_of_palindromes)
    return None



def test_length_of_largest_palindrome():
    graph_letters = [
        ['S'], #0
        ['H'], #1
        ['O'], #2
        ['A'], #3
        ['N'], #4
        ['D'], #5
        ['E'], #6
        ['N'], #7
        ['N'], #8
        ['T'], #9
        ['A'], #10
        ['O'], #11
        ['H'], #12
        ['T'] #13
    ]

    graph_connectiong = [
        [1,2,6],
        [3],
        [4,5],
        [4,6,8],
        [7,9],
        [4,7,10],
        [7,9],
        [10,13],
        [9,11],
        [11,12],
        [9,12],
        [13],
        [13],
        []
    ]

    assert length_of_largest_palindrome(graph_letters, graph_connectiong) == 6

    
    graph_letters =[
        ['S'], #0
        ['H'], #1
        ['O'], #2
        ['A'], #3
        ['N'], #4
        ['D'], #5
        ['E'], #6
        ['N'], #7
        ['N'], #8
        ['T'], #9
        ['A'], #10
    ]
    
    graph_connectiong = [
        [1, 2], #0
        [3, 9, 10], #1
        [4,5], #2
        [6,8], #3
        [8], #4
        [], #5
        [7], #6
        [], #7
        [], #8
        [], #9
        [], #10
    ]

    assert length_of_largest_palindrome(graph_letters, graph_connectiong) == 2


def test_find_largest_palindrome():
    graph_letters = [
        ['S'], #0
        ['H'], #1
        ['O'], #2
        ['A'], #3
        ['N'], #4
        ['D'], #5
        ['E'], #6
        ['N'], #7
        ['N'], #8
        ['T'], #9
        ['A'], #10
        ['O'], #11
        ['H'], #12
        ['T'] #13
    ]

    graph_connectiong = [
        [1,2,6],
        [3],
        [4,5],
        [4,6,8],
        [7,9],
        [4,7,10],
        [7,9],
        [10,13],
        [9,11],
        [11,12],
        [9,12],
        [13],
        [13],
        []
    ]

    assert find_largest_palindrome(graph_letters, graph_connectiong) == "HANNAH"

    
    graph_letters =[
        ['S'], #0
        ['H'], #1
        ['O'], #2
        ['A'], #3
        ['N'], #4
        ['D'], #5
        ['E'], #6
        ['N'], #7
        ['N'], #8
        ['T'], #9
        ['A'], #10
    ]
    
    graph_connectiong = [
        [1, 2], #0
        [3, 9, 10], #1
        [4,5], #2
        [6,8], #3
        [8], #4
        [], #5
        [7], #6
        [], #7
        [], #8
        [], #9
        [], #10
    ]

    assert find_largest_palindrome(graph_letters, graph_connectiong) == 'NN'

def test_dpf():
    graph_connectiong = [
        [1, 2], #0
        [3, 9, 10], #1
        [4,5], #2
        [6,8], #3
        [], #4
        [], #5
        [7], #6
        [], #7
        [], #8
        [], #9
        [], #10
    ]

    assert dfs(graph_connectiong, [0], [], 0) == [
        [0,1,3,6,7], 
        [0,1,3,8],
        [0,1,9],
        [0,1,10],
        [0,2,4],
        [0,2,5]
        ]

    graph_connectiong = [
        [1, 2], #0
        [3, 9, 10], #1
        [4,5], #2
        [6,8], #3
        [8], #4
        [], #5
        [7], #6
        [], #7
        [], #8
        [], #9
        [], #10
    ]

    assert dfs(graph_connectiong, [0], [], 0) == [
        [0,1,3,6,7], 
        [0,1,3,8],
        [0,1,9],
        [0,1,10],
        [0,2,4,8],
        [0,2,5]
        ]

def test_get_words():
    graph_letters =[
        ['S'], #0
        ['H'], #1
        ['O'], #2
        ['A'], #3
        ['N'], #4
        ['D'], #5
        ['E'], #6
        ['N'], #7
        ['N'], #8
        ['T'], #9
        ['A'], #10
    ]
    
    paths = [
        [0,1,3,6,7], 
        [0,1,3,8],
        [0,1,9],
        [0,1,10],
        [0,2,4,8],
        [0,2,5]
    ]

    assert get_letters(graph_letters, paths) == [
        'SHAEN',
        'SHAN',
        'SHT',
        'SHA',
        'SONN',
        'SOD'
    ]

def test_check_for_palindrome():
    possible_palindromes = [
        'SHAEN',
        'SHAN',
        'SHT',
        'SHA',
        'SONN',
        'SOD'
    ]

    assert check_for_palindrome(possible_palindromes) == None

    possible_palindromes = [
    'HANTH',
    'HAETH',
    'HANTH',
    'HANNAH',
    'HAH'
    ]

    assert check_for_palindrome(possible_palindromes) == "HANNAH"
