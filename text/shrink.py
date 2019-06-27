from talon.voice import Context, Str

# from ..utils import alternatives

ctx = Context("shrink")


def shrink_word(m):
    # Str(shrink_map[" ".join(m["shrink.words"])])(None)
    Str(shrink_map[m[1]])(None)


shrink_map = {
    "administrator": "admin",
    "administrators": "admins",
    "allocate": "alloc",
    "alternate": "alt",
    "apartment": "apt",
    "application": "app",
    "applications": "apps",
    "architecture": "arch",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "authentic": "auth",
    "authenticate": "auth",
    "authentication": "auth",
    "author": "auth",
    "binary": "bin",
    "boolean": "bool",
    "button": "btn",
    "calculate": "calc",
    "call": "col",
    "car": "char",
    "care": "char",
    "certificate": "cert",
    "character": "char",
    "column": "col",
    "command": "cmd",
    "compute": "cmp",
    "concatenate": "concat",
    "configuration": "config",
    "configure": "config",
    "constant": "const",
    "context": "ctx",
    "control": "ctrl",
    "define": "def",
    "delete": "del",
    "descending": "desc",
    "destination": "dest",
    "develop": "dev",
    "developer": "dev",
    "development": "dev",
    "dictionary": "dict",
    "difference": "diff",
    "directory": "dir",
    "distribute": "dist",
    "divider": "div",
    "document": "doc",
    "environment": "env",
    "environments": "envs",
    "error": "err",
    "execute": "exec",
    "extend": "ext",
    "extension": "ext",
    "favorite": "fav",
    "format": "fmt",
    "frequency": "freq",
    "function": "func",
    "image": "img",
    "imager": "int",
    "incorporate": "inc",
    "increment": "inc",
    "initialize": "init",
    "integer": "int",
    "iterate": "iter",
    "jason": "json",
    "language": "lang",
    "large": "lg",
    "latitude": "lat",
    "length": "len",
    "library": "lib",
    "locate": "loc",
    "location": "loc",
    "longitude": "lng",
    "medium": "md",
    "message": "msg",
    "minimum": "min",
    "miscellaneous": "misc",
    "navigate": "nav",
    "navigation": "nav",
    "number": "num",
    "object": "obj",
    "option": "opt",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "position": "pos",
    "previous": "prev",
    "production": "prod",
    "project": "proj",
    "pseudo": "sudo",
    "random": "rand",
    "reference": "ref",
    "references": "refs",
    "repeat": "rep",
    "request": "req",
    "result": "res",
    "revision": "rev",
    "sequence": "seq",
    "source": "src",
    "squareroot": "sqrt",
    "standard": "std",
    "standing": "stdin",
    "standout": "stdout",
    "string": "str",
    "system": "sys",
    "temporary": "tmp",
    "text": "txt",
    "thanks": "thx",
    "universal": "uuid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    "yaml": "yml",
    # months,
    "january": "jan",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "june": "jun",
    "july": "jul",
    "august": "aug",
    "september": "sept",
    "october": "oct",
    "november": "nov",
    "december": "dec",
}


def alternatives(options):
    return " (" + " | ".join(sorted(map(str, options))) + ")"


ctx.keymap({"shrink" + alternatives(shrink_map.keys()): shrink_word})
# ctx.keymap({"shrink {shrink.words}": shrink_word})
# ctx.set_list("words", shrink_map.keys())
