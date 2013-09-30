import re

def reg(n):
    pv1 = re.compile(r'(^|[#\s])bar($|[\s\.])')
    p = re.compile(r'([\s#]bar)\.domain\.(?:([a-zA-Z]{1,}($|\s)))')
    if p.search(n):
        n = p.sub(r"\1.donemain.\2", n)
        n = pv1.sub(r"\1baz\2", n)
        return n
    else:
        return False
