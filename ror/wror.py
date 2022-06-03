import ror.letter as letter
import re

def upper(c):
    return c[0].upper() + c[1:]

def word(rs):
    rm = ""
    i = 0
    while i < len(rs):
        try:
            e, mov = char(rs[i], i, rs)
            rm += e
            i += mov
        except ValueError:
            raise NameError(f"has non-russian alphabet at {i}")
    return rm

symbols = ["-", "_", "."]

def char(c, i=0, rs=""):
    assert(rs == "" or rs[i] == c)
    up = c.isupper()
    c = c.lower()
    if c in symbols:
        e = c
    elif c in letter.cons:
        e = letter.cons[c]
    elif c in letter.vows:
        if (i == len(rs) - 2 and rs[i:] == "ий"):
            return "y", 2
        if (i == len(rs) - 2 and rs[i:] == "ые"):
            return "ye", 2
        if (i == len(rs) - 2 and rs[i:] == "ый"):
            return "y", 2
        elif c == "е":
            e = "e" if (
                i != 0
                and rs[i-1].lower() in letter.cons) else "ye"
        else:
            e = letter.vows[c]
    elif c in letter.semi:
        e = letter.semi[c]
    elif c in letter.mods:
        e = letter.mods[c] if (
            i != len(rs) - 1
            and rs[i+1].lower() in letter.vows
            and rs[i+1].lower() not in letter.iotated_vows) else ""
    else:
        raise ValueError()
    return (upper(e) if up else e), 1
