from enum import Enum

questions = [
    "\nWhat are the chances of you taking an entrance exam at UE?", # 0
    "\nDoes COE-COD accreditation matter to you?", # 1
    "\nDoes PACUCOA accreditation matter to you?", # 2
    "\nHow confident are you about passing the UE entrance exam?", # 3
    "\nAre you interested in taking an Engineering course at UE?", # 4
    "\nDoes your mother currently have an occupation?", # 5
    "\nDoes your father currently have an occupation?" # 6
]

consider = [
    "\n\nYou Extremely consider UE as a university.", #0
    "\n\nYou have High considerations for UE as a university.", #1
    "\n\nYou are neutral about considering UE as a university", #2
    "\n\nYou moderately consider UE as a university.", #3
    "\n\nYou did not consider UE as a university at all", #4
    "\n\nYou have slight considerations about UE as a university at all" #5
]

categorical_choices = """
6: Extremely likely
5: Very likely
4: Likely
3: Undecided
2: Unlikely
1: Very unlikely
"""

binary_choices = """
[Y/y] for Yes
[N/n] for No
"""
