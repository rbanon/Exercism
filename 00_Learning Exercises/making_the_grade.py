"""
Making the Grade
"""
# Create the function round_scores() that takes a list of student_scores.
# This function should consume the input list and return a new list with all the scores converted to ints.
# The order of the scores in the resulting list is not important.
def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(x) for x in student_scores]

# Create the function count_failed_students() that takes a list of student_scores.
# This function should count up the number of students who don't have passing scores
# and return that count as an integer.
# A student needs a score greater than 40 to achieve a passing grade on the exam.
def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return len([x for x in student_scores if x <= 40])

# Create the function above_threshold() taking student_scores (a list of grades),
# and threshold (the "top score" threshold) as parameters.
# This function should return a list of all scores that are >= to threshold.
def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [x for x in student_scores if x >= threshold]

# Create the function letter_grades() that takes the "highest" score on the exam as a parameter,
# and returns a list of lower score thresholds for each "American style" grade interval: ["D", "C", "B", "A"].
def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    return list(range(41, highest, (highest - 40) // 4))

# Create the function student_ranking() with parameters student_scores and student_names.
# Match each student name on the student_names list with their score from the student_scores list.
# You can assume each argument list will be sorted from highest score(er) to lowest score(er).
# The function should return a list of strings with the format <rank>. <student name>: <student score>.
def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    return [f"{n}. {student_name}: {student_score}" for n, (student_score, student_name) in enumerate(zip(student_scores, student_names), 1)]

#Create the function perfect_score() with parameter student_info.
# student_info is a list of lists containing the name and score of each student:
def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    # Why not [x for x in student_info if x[1] == 100 ]
    for student in student_info:
        if student[1] == 100:
            return student
    return []
