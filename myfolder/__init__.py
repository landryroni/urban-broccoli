def subtraction(a,b):
    return a-b


def union_probability(pa,pb,p_intersection):
    '''Compute the probability of P(A or B) given P(A),P(B), P(A and B)'''
    return pa + pb - p_intersection