# a basic/simple quiz app 

# code only runs in terminal 



def quiz_questions():
        print('\nThere are 3 questions in this section. Answer all.\n')
        #global add 
        #add = 0
        question1 = {1 : '1). What is the full meaning of USA?'}
        question2 = {2 : '2). What is the full meaning of AI?'}
        question3 = {3 : '3). Which company created the smart phone?'}
        print(question1.get(1)) # get question 1 
        global answers1 # access this variable anywhere in this code
        answers1 = {'A' : 'A. United States of America',
                   'B' : 'B. United State of Americans',
                   'C' : 'C. United Staff of Amies'}
        print(answers1.get('A'))
        print(answers1.get('B'))
        print(answers1.get('C'))
        print() # leave a space between the questions
        print(question2.get(2)) # get question 2
        global answers2 # access this variable anywhere in this code
        answers2 = {'A' : 'A. Artificial Innocent',
                    'B' : 'B. Artificial Intellectual',
                    'C' : 'C. Artificial Intelligence'}
        print(answers2.get('A'))
        print(answers2.get('B'))
        print(answers2.get('C'))
        print() # leave a space between the questions
        global answers3 # access this variable anywhere in this code
        print(question3.get(3)) # get question 3
        answers3 = {'A' : 'A. Apple',
                   'B' : 'B. Samsung',
                   'C' : 'C. Nokia'}
        print(answers3.get('A'))
        print(answers3.get('B'))
        print(answers3.get('C'))
       
        

quiz_questions()

# choosing answers 
def choose_answers(): 
        # answers for question 1
        calculate_score = 0
        global correct_answers
        correct_answers = { 
                'Q1' : 'A', 
                'Q2' : 'C', 
                'Q3' : 'A',
        } 
        global choose_answer1
        print()
        choose_answer1 = input('Choose an answer for question 1: ').title().strip()
        if choose_answer1 == correct_answers.get('Q1'):
                print('Correct')
                calculate_score += 1 

        elif choose_answer1 != correct_answers.get('Q1'):
                print('Wrong')
                calculate_score += 0
        
        #return calculate_score  
        
        

        global choose_answer2
        choose_answer2 = input('Choose an answer for question 2: ').title().strip()
        if choose_answer2 == correct_answers.get('Q2'):
                print('Correct')
                calculate_score += 1 
        elif choose_answer1 != correct_answers.get('Q2'):
                print('Wrong')
                calculate_score += 0
        
        global choose_answer3
        choose_answer3 = input('Choose an answer for question 3: ').title().strip()
        if choose_answer3 == correct_answers.get('Q3'):
                print('Correct')
                calculate_score += 1 
        elif choose_answer3 != correct_answers.get('Q3'):
                print('Wrong')
                calculate_score += 0
        

        
        return calculate_score

results = choose_answers()
print(F'\nYour score is: {results}/3')



























































 