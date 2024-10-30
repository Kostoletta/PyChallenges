def isValid(s: str) -> bool:
    """
    This function checks if the input string has valid parentheses.
    """
    stackOpen = []
    openP = {"(": ")", "[": "]", "{": "}"}
    closeP = {")", "]", "}"}

    for p in s:
        if p in openP:
            stackOpen.append(p)
        else:
            if stackOpen and p == openP[stackOpen[-1]]:
                stackOpen.pop()
            else:
                return False
    return not stackOpen
