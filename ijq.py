import sys
import json

from pygments import highlight, lexers, formatters


def find_jsons(s: str, ignore_simple=True):
    def pipe(i, j):
        if not ignore_simple or (("[" in s[i:j]) or ("{" in s[i:j])):
            yield i, j

    ind = 0
    while ind < len(s):
        try:
            json.loads(s[ind:])
        except json.JSONDecodeError as err:
            if err.msg == "Extra data":
                yield from pipe(ind, ind + err.pos)
            ind += err.pos + 1
        else:
            return (yield from pipe(ind, len(s)))


def pretty_json(obj: dict, no_color: bool):
    obj = json.dumps(obj, indent=4, ensure_ascii=False, sort_keys=True)
    if no_color:
        return obj
    else:
        return highlight(obj, lexers.JsonLexer(), formatters.TerminalFormatter())


def ijq(s="", ignore_simple=True, no_color=False):
    s, lj, res = (s or sys.stdin.read()), 0, ""
    for i, j in find_jsons(s, ignore_simple):
        if lj < i:
            yield s[lj:i]
        yield pretty_json(json.loads(s[i:j]), no_color=no_color)
        lj = j
    yield s[lj:]


def main():
    ignore_simple = "--no-ignore-simple" not in sys.argv
    no_color = "--no-color" in sys.argv
    print("\n".join(ijq(ignore_simple=ignore_simple, no_color=no_color)))
