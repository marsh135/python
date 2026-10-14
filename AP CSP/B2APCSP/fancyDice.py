import random
from collections import Counter
dice={
    1:
    """
     -------  
    |       |
    |   *   |
    |       |
     -------
    """,
    2:
    """
     -------  
    |     * |
    |       |
    | *     |
     -------
    """,
    3:"""
     -------  
    |     * |
    |   *   |
    | *     |
     -------
    """,
    4:"""
     -------  
    | *   * |
    |       |
    | *   * |
     -------
    """,
    5:"""
     -------  
    | *   * |
    |   *   |
    | *   * |
     -------
    """,
    6:"""
     -------  
    | *   * |
    | *   * |
    | *   * |
     -------
    """
}
rolls = []
for i in range(50):
    n = random.randint(1,6)
    rolls.append(n)
    print(dice[n], end="")

counts = Counter(rolls)
sortedCounts = {face: counts[face] for face in sorted(counts)}
print(sortedCounts)