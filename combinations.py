from itertools import permutations
import json

# function to get unique values
def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list
 
all = [''.join(x) for x in permutations("000000")] + [''.join(x) for x in permutations("000002")]
all += [''.join(x) for x in permutations("000022")] + [''.join(x) for x in permutations("000222")]
all += [''.join(x) for x in permutations("002222")] + [''.join(x) for x in permutations("022222")]
all += [''.join(x) for x in permutations("222222")]

    

all.sort()

unique = unique(all)

unique.sort()

unique.remove("000000")

unique.remove("000002")
unique.remove("000020")
unique.remove("000022")

unique.remove("000200")
unique.remove("000202")
unique.remove("000220")
unique.remove("000222")

unique.remove("002000")
unique.remove("002002")
unique.remove("002020")
unique.remove("002022")


unique.remove("002200")
unique.remove("002202")
unique.remove("002220")
unique.remove("002222")

print(json.dumps(unique))
