# Solving problems in statistics

import math
from utils import probability
from utils.testing import test_equal, test_close
import utils.counting as C

list1 = [1,2,3,4]
list2 = [1,6,3,4]
list3 = [1,2,5,4]
list3 = [1,2,3,8]

list4 = [2,4,6,8]
if __name__ == "__main__":

    print("\nSOME PROBABILITY PROBLEMS\n")

    
    # Question 2
    print("Q: Find the probability of getting 3 heads when you toss 10 fair coins.")
    p_3_heads = C.combinations(10, 2) / 2**10
    print("A: The probability is {}".format(p_3_heads))
    expected_p_3_heads = 0.1171875
    test_close(p_3_heads, expected_p_3_heads)
    print("")