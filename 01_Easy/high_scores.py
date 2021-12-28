"""
Your task is to write methods that return the highest score from the list,
the last added score and the three highest scores.
"""
# Manage a game player's High Score list.
def latest(scores):
    return scores.pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores,reverse=True)[:3]
