'''Complete each functions below so that the test cases pass.
Your solutions should use  map and filter functions,
and not fo  loops or list comprehensions. '''


def evens(n):

    return list(filter(lambda n: n % 2 == 0, range(n + 1)))

    '''
    Returns a list of even numbers from 0 to n inclusive.

    >>> evens(10)
    [0, 2, 4, 6, 8, 10]
    >>> evens(11)
    [0, 2, 4, 6, 8, 10]
    >>> evens(0)
    [0]
    >>> evens(1)
    [0]
    >>> evens(-1)
    []
    '''


def threes(n):
    nums = range(n + 1)
    xs = filter(lambda num: str(3) in str(num), nums)
    return list(xs)
    '''
    Returns a list of all numbers from 0 to n inclusive that
    contain the digit 3.

    >>> threes(2)
    []
    >>> threes(3)
    [3]
    >>> threes(10)
    [3]
    >>> threes(20)
    [3, 13]
    >>> threes(50)
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''


def small_words(text):
    text = text.split()
    xs = filter(lambda y: len(y) < 5, text)
    return list(xs)
    '''
    Returns a list of all words in the input text that are less than
    5 characters long.

    HINT:
    Recall that text.split() converts the text variable into a list of words.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''


def squares(n):
    xs = map(lambda n: n * n, range(n + 1))
    xs = list(xs)
    return (xs)
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''


def lengths(strings):
    x = map(lambda t: len(t), strings)
    xs = list(x)
    return (xs)
    '''
    Given a list of strings, returns a list of
    the lengths of the corresponding strings.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4, 2, 1, 4]
    '''
