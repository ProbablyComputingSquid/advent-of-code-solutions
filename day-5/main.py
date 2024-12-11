f = open("day-5/input.txt").read().splitlines()


rules = f[:f.index('')]
rules = [x.split("|") for x in rules]
#print(rules)
ruledict = {}
for rule in rules:
    if rule[0] not in ruledict:
        ruledict[rule[0]] = [rule[1]]
    else:
        ruledict[rule[0]].append(rule[1])
#print(ruledict)
updates = f[f.index('')+1:]

updates = [x.split(",") for x in updates]
count = 0

for update in updates: # for each update
    caught = False
    for page in update: # for each page in updates
        if page in ruledict.keys(): # if the page is in the dict validate it
            #print("page", page, "is in the dict")
            # validation of the page
            for key, pagerule in ruledict.items(): # for each rule
                if key != page:
                    continue
                
                for item in pagerule: # iterate through each item in the ruleset for the page
                    
                    try:
                        if update.index(key) <= update.index(item):
                            # this is correct
                            None
                        else:
                            #print("incorrect")
                            caught = True
                    except ValueError:
                        None
    if caught:
        print("page", update, "is incorrect")
    else:
        count += int(update[len(update) // 2])

print(count)

        