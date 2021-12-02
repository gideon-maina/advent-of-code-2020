# coding: utf-8
def sum_of_yes_answers(group_answers_file: str) -> int:
    answers = []
    
    with open(group_answers_file) as fh:
        contents = fh.read().splitlines()
        answer = collections.Counter()
        # Start at 1 in enumerate to also include the last line
        for index, line in enumerate(contents, start = 1):
            append = False 
            if line:
                to_add = collections.Counter(line)
                answer.update(to_add)
            elif not line:
                append = True
            if append or index == len(contents):
                answers.append(answer)
                # Reset answer
                answer = collections.Counter()
    # now since we have the answers get the sum
    sum_of_counts = 0
    for a in answers:
        questions = len(a.keys())
        sum_of_counts += questions
    return sum_of_counts
    
def sum_of_yes_answers_part_2(group_answers_file: str) -> int:
    answers = collections.defaultdict(list)
    
    with open(group_answers_file) as fh:
        contents = fh.read().splitlines()
        answer = collections.Counter()
        ans_index = 0
        # Start at 1 in enumerate to also include the last line
        for index, line in enumerate(contents, start = 1):
            append = False 
            if line:
                to_add = collections.Counter(line)
                answers[ans_index].append(to_add)
            elif not line:
                append = True
            if append or index == len(contents):
                ans_index += 1
    # now since we have the answers get the sum
    sum_of_counts = 0
    
    for key,value in answers.items():
        check_set = set(value[0])
        if len(value) > 1:
            for index, person in enumerate(value):
                if index == 0:
                    check_set = set(person.keys())
                else:
                    # Intersect the previous questions with this persons questions
                    check_set = check_set.intersection(person.keys())
        sum_of_counts += len(check_set)
    return sum_of_counts
    
