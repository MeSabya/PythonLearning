from collections.abc import Iterable

def flatten_list(L):
    for item in L:
        if isinstance(item, Iterable):
            yield from flatten_list(item)
        else:
            yield item


def flatten_list_2(L):
    print("list is ", L)
    for item in L:
        if isinstance(item, Iterable):
            for v in flatten_list_2(item):
                yield v
        else:
            yield item
print(list(flatten_list([1, 2, [3, 4], [5, 6, [7]]])))
print("Flatten using approach 2")
print(list(flatten_list_2([1, 2, [3, 4], [5, 6, [7]]])))