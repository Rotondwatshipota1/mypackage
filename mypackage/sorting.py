def bubble_sort(items):
    """ Implementation of bubble sort """
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

 def merge_sort(items):

      x = len(items)
       if not x: # length is 1
            return items
       else:
            return merge_sort(merge_sort(items[:x]), merge_sort(items[x:]))


def quick_sort(items):
        if len(items) <= 1:

            return items
        else:
            return quick_sort([x for x in items[1:]if x < items[0]])+
            [items[0]]+ quick_sort([x for x in items[1:]if x >= items[0]])
