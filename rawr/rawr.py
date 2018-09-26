import re
import sys
import json

def compile(file, keys, out):
    dictionary = {
        "d": keys,
        "c": file
    }
    with open(out, "w+") as o:
        o.write(json.dumps(dictionary))
        o.close()
def get_name(file):
    return "{}.rawr".format(file)

def repetitions(s):
   r = re.compile(r"(.{3,})\1+")
   for match in r.finditer(s):
       yield (match.group(1),
              len(match.group(0))
              /len(match.group(1)))

def parseFile(file_name):
    with open(file_name, "r") as f:
        file = f.read()
        f.close()
    keys = [None] * len(file)
    for i, r in enumerate(repetitions(file)):
        if r[0] in keys:
            ind = keys.index(r[0])
        else:
            keys[i] = r[0]
            ind = i
        file = re.sub(r[0], "[{}]".format(ind), file)
    keys = list(filter(None, keys))
    compile(file, keys, get_name(file_name))

def is_compiled(file_name):
    if file_name.endswith(".rawr") or file_name.endswith(".rawr.xd"):
        return True
    else:
        return False

def decompile(file_name):
    with open(file_name, "r") as f:
        file = f.read()
        f.close()
    file = json.loads(file)
    c = file["c"]
    d = file["d"]
    for it, i in enumerate(d):
        regex = r"\[" + re.escape(str(it)) + r"\]"
        print(i)
        c = re.sub(regex, i, c)
    file_name = ".".join(file_name.split('.')[:-1])
    print(c)
    with open(file_name, "w+") as f:
        f.write(c)
        f.close()

def main():
    print("this joke went too far already")
    if len(sys.argv) > 1:
        if is_compiled(sys.argv[1]):
            decompile(sys.argv[1])
        else:
            parseFile(sys.argv[1])
if __name__ == "__main__":
    main()
