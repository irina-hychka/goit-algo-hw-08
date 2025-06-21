import heapq

def calc_min_cost(cables):
    """
    Calculate the minimal total cost to connect all cables optimally.

    Parameters:
        cables: List of cable lengths.

    Returns:
        int: Minimal total cost to connect all cables.

    Raises:
        ValueError: If any cable length is negative or not an integer.
    """
    if not all(isinstance(cable, int) and cable >= 0 for cable in cables):
        raise ValueError("All cable lengths must be non-negative integers.")

    if not cables:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        merged = first + second
        total_cost += merged
        heapq.heappush(cables, merged)

    return total_cost

# Usage
if __name__ == "__main__": 
    cables = [2, 3, 2, 6]

    try:
        cost = calc_min_cost(cables)
        print("Minimum total connection cost:", cost)
    except ValueError as e:
        print("Error:", e)
