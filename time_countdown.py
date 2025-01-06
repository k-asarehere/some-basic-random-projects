# a countdown project(app)

import time 

def countdown(t):
    while t : 
        mins , secs = divmod(t,60)
        timer_format = f'{mins:02d}:{secs:02d}'
        print(timer_format, end='\r')
        time.sleep(1)
        t -= 1 
    print('Countdown done!')

countdown_num = int(input('Enter a number to countdown: '))
countdown(countdown_num)
