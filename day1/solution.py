import itertools


def get_calories_list(inp):
    # split list into smaller lists, for every item containing '' (empty string)
    iterator = itertools.groupby(inp, lambda x: x == "")
    inp = [list(g) for k, g in iterator if not k]

    # sum sublists
    return [sum(map(int, x)) for x in inp]


# return highest value
def get_most_calories(inp):
    return max(get_calories_list(inp))


# return sum of top 3 values
def get_most_calories_top3(inp):
    return sum(sorted(get_calories_list(inp))[-3:])
