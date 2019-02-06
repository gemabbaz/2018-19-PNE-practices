def count_bases(seq):
    """Counting the number of As in the string"""
    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0
    for b in seq:
        if b == 'A':
            result_a += 1
        elif b == 'C':
            result_c += 1
        elif b == 'T':
            result_t += 1
        elif b == 'G':
            result_g += 1

    return dict(A=result_a, C=result_c, G=result_g, T=result_t)