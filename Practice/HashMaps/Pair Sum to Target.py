def pair_sum_to_target(input_list, target):
    # TODO: Write pair sum to target function
    d = {k: i for i, k in enumerate(input_list)}
    for i, j in enumerate(input_list):
        r = target-j
        l = d.get(r)
        if l:
            return i, l
    return -1, -1
