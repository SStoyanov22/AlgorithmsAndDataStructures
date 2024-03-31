def eval_parentheses(parantheses_string: str) -> int:
    """
    The function is given a non-empty balanced parentheses string. Each opening '(' has a corresponding closing ')'.
    Compute the total score based on the following rules:
        Substring s == () has score 1, so "()" should return 1
        Substring s1s2 has total score as score of s1 plus score of s2, so "()()" should return 1 + 1 = 2
        Substring (s) has total score as two times score of s, so "(())" should return 2 * 1 = 2
    Return the total score as an integer.
    :param parantheses_string: non-empty balanced parentheses string
    :return: total score as an integer
    Examples:
    >>> eval_parentheses("()")
    1
    >>> eval_parentheses("(())")
    2
    >>> eval_parentheses("()()")
    2
    >>> eval_parentheses("((())())")
    6
    >>> eval_parentheses("(()(()))")
    6
    >>> eval_parentheses("()(())")
    3
    >>> eval_parentheses("()((()))")
    5
    """
    eval = pow = 0
    for left,right in zip(parantheses_string, parantheses_string[1:]):
        if left + right == '()': eval += 2 ** pow
        pow += 1 if left == '(' else -1
    return eval

if __name__ == "__main__":
    import doctest

    doctest.testmod()