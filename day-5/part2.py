f = open("day-5/input.txt").read().splitlines()
#f = open("day-5/testcase.txt").read().splitlines()

rules = f[:f.index('')]
rules = [x.split("|") for x in rules]

ruledict = {}
for rule in rules:
    if rule[0] not in ruledict:
        ruledict[rule[0]] = [rule[1]]
    else:
        ruledict[rule[0]].append(rule[1])

updates = f[f.index('')+1:]

updates = [x.split(",") for x in updates]
count = 0
def validate(update):
    for page in update: # for each page in updates
        if page in ruledict.keys(): # if the page is in the dict validate it
            # validation of the page
            for key, pagerule in ruledict.items(): # for each rule
                if key != page:
                    continue
                for item in pagerule: # iterate through each item in the ruleset for the page
                    try:
                        if update.index(key) > update.index(item):
                            return False
                    except ValueError:
                        None
    return True
def fixIncorrect(update):
    while(not validate(update)):
        for page in update: # for each page in updates
            if page in ruledict.keys(): # if the page is in the dict validate it
                # validation of the page
                for key, pagerule in ruledict.items(): # for each rule
                    if key != page:
                        continue
                    for item in pagerule: # iterate through each item in the ruleset for the page
                        try:
                            if update.index(key) > update.index(item):
                                update[update.index(key)], update[update.index(item)] = update[update.index(item)], update[update.index(key)]
                        except ValueError:
                            None
    return update
incorrect = []
for update in updates: # for each update
    valid = False
    valid = validate(update)
    if not valid:
        #print("page", update, "is incorrect")
        incorrect.append(update)
    else:
        count += int(update[len(update) // 2])

fixed = []
for inc in incorrect:
    fixed.append(fixIncorrect(inc))

print(fixed)

mid_sum = sum([int(x[len(x) // 2]) for x in fixed])
print(mid_sum)
#print(count)

        