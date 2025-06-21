import heapq

import heapq

def merge_k_lists(lists):
    """
    Merge k sorted lists into a single sorted list using a min-heap.

    Parameters:
        lists: A list of k sorted integer lists.

    Returns:
        List[int]: A single merged and sorted list.

    Raises:
        ValueError: If any list is not a list of integers.
    """
    # Validate input
    if not isinstance(lists, list):
        raise ValueError("Input must be a list of lists.")

    for sublist in lists:
        if not isinstance(sublist, list):
            raise ValueError("Each element in the input must be a list.")
        if not all(isinstance(x, int) for x in sublist):
            raise ValueError("Each sublist must contain only integers.")

    merged = []
    min_heap = []

    # Initialize heap with the first element of each list
    for i, sublist in enumerate(lists):
        if sublist:
            heapq.heappush(min_heap, (sublist[0], i, 0))  # (value, list_index, element_index)

    # Extract the smallest item and push the next element from the same list
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        merged.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return merged


# Usage
if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted List:", merged_list)
