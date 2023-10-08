#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Return True if can be open, false if not
    """
    opened_boxes = [0]
    nOfBoxes = len(boxes)

    for keys in opened_boxes:
        for box in boxes[keys]:
            if box < nOfBoxes and box not in opened_boxes:
                opened_boxes.append(box)

    return len(opened_boxes) == nOfBoxes
