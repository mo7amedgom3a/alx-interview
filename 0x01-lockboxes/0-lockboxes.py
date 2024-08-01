def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False
    
    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    # Use a queue to explore boxes
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)
    return all(opened)
