#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    unlocked_boxes = {0}  # Start with the first box unlocked
    keys = set(boxes[0])  # Start with keys found in the first box

    # Loop until we can't find any new boxes to unlock
    while True:
        new_keys = keys.copy()

        # Try to unlock more boxes
        for key in keys:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                new_keys.update(boxes[key])

        # If no new boxes can be unlocked, break the loop
        if new_keys == keys:
            break

        keys = new_keys

    # Check if we unlocked all the boxes
    return len(unlocked_boxes) == len(boxes)
