from collections import defaultdict

parsed = defaultdict(list)
isQuery = False


def parseLine(s: str):
    facts = s.split(')')

    for fact in facts[:-1]:
        name, body = fact.split('(')
        inputArgs = body.split(',')

        if not isQuery:
            parsed[name].append(inputArgs)
            continue

        ans = 0

        for factArgs in parsed[name]:
            if len(factArgs) != len(inputArgs):
                continue

            isMatch, vars = True, {}
            
            for qArg, fArg in zip(inputArgs, factArgs):
                if qArg == fArg or qArg == '_':
                    pass
                elif qArg[0] == '_':
                    if qArg not in vars:
                        vars[qArg] = fArg
                    elif vars[qArg] != fArg:
                        isMatch = False
                        break
                else:
                    isMatch = False
                    break

            if isMatch:
                ans += 1

        print(ans)


while True:
    try:
        line = input()
        line = line.replace(' ', '')

        if len(line) == 0:
            isQuery = True
            continue

        parseLine(line)
    except EOFError:
        break
