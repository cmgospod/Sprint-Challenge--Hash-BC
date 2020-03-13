#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    current = 0
    for weight in weights:
        hash_table_insert(ht, weight, current)
        current += 1
    for weight in weights:
        zero = hash_table_retrieve(ht, limit-weight)
        if zero is not None:
            one = hash_table_retrieve(ht, weight)
            if zero == one != None:
                for test in weights:
                    if test == weight:
                        one = weights.index(test)
            return (zero, one)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
