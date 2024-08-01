#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if not boxes:
        return False
    box_count = len(boxes)
    if box_count == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box < box_count and box not in keys:
                keys.append(box)
    return len(keys) == box_count
