import sys, os, time, statistics
from threading import Timer
from tkinter import *


# globals
path_to_experiment_folder = "C:\\Documents and Settings\\Admin\\Рабочий стол\\Experiments\\Nastia PhD"
timer_started = False
training_pattern = ["lrlrlrlr", "rlrrlrll"]
training_type = ["hand", "leg"]
shifted_training_pattern = training_pattern[0]
current_input = ''
global_idx = 0
input_idx = 0
train_type_idx = 0

current_delays = []
previous_delays = []
current_milli_time = lambda: int(round(time.time() * 1000))
tmp_time = 0

def succeed_to_train():
    global global_idx, train_type_idx, path_to_experiment_folder, current_delays, training_pattern, shifted_training_pattern, timer_started
    timer_started = False
    subject_id = sys.argv[1]
    if not os.path.exists(path_to_experiment_folder+'/logs/'+subject_id):
        os.makedirs(path_to_experiment_folder+'/logs/'+subject_id)
    
    if global_idx == 0:
        if train_type_idx == 0:
            mode = 'w'
            prefix = 'simple_seq_arm'
        else:
            mode = 'a'
            prefix = 'simple_seq_leg'
        
    else:
        mode = 'a'
        if train_type_idx == 0:
            prefix = 'hard_seq_arm'
        else:
            prefix = 'hard_seq_leg'
    
    file = open(path_to_experiment_folder+'/logs/'+subject_id+'/'+subject_id+'_trained_freq',mode)
    file.write(prefix+' = '+statistics.mean(current_delays)+'\n')
    file.close()
    
    if global_idx == 1 and train_type_idx == 1:
        sys.exit() # terminate the script. This is the end...
    elif global_idx == 0 and train_type_idx == 1:
        global_idx = 1    
        train_type_idx = 0
    elif train_type_idx == 0:
        train_type_idx = 1
    else:
        train_type_idx = 0
            
    reset_input()
    w.config(text="Press "+training_pattern[global_idx]+" by "+training_type[train_type_idx])
    shifted_training_pattern = training_pattern[global_idx]

def keyPress(e):
    sym = e.keysym
    time = current_milli_time() 
    if  sym == 'Escape':
        root.quit()
    elif sym == 'Shift_L' or sym == '5':
        handleInput('l', time)
    elif sym == 'Shift_R' or sym == '6':
        handleInput('r', time)
        
def handleInput(rl, time):
    global current_input, global_idx, training_pattern, tmp_time, previous_delays, current_delays, shifted_training_pattern, input_idx, timer_started, exit_timer  
    if len(current_input) < 8:        
        current_input += rl
        if current_input != training_pattern[global_idx][:len(current_input)]:
            reset_input()
        else:
            if len(current_input) == 1:
                tmp_time = time
            elif len(current_input) == 2:
                delta = time-tmp_time
                tmp_time = time
                if delta > 2000:    # drop all if it last more than 2 sec from prev input
                    reset_input()
                    handleInput(rl, time)
                    return
                current_delays.append(delta)
                previous_delays.append(delta)
            else:
                delta = time-tmp_time
                tmp_time = time
                if delta > 2000:
                    reset_input()
                    handleInput(rl, time)
                    return
                current_delays.append(delta)
                previous_delays.append(delta)
    else:
        current_input = current_input[1:] + rl
        shifted_training_pattern = shifted_training_pattern[-1] + shifted_training_pattern[:-1]
        if shifted_training_pattern == current_input:
            delta = time-tmp_time
            tmp_time = time
            if delta > 2000:
                reset_input()
                handleInput(rl, time)
                return
            previous_delays = current_delays
            current_delays = current_delays[1:]
            current_delays.append(delta)
            input_idx+=1
        else: 
            reset_input()
            return
    
    if len(current_input) != 0 and input_idx == 4:
        input_idx = 0
        if(uniform_input()):
            if not timer_started:
                exit_timer = Timer(20.0, succeed_to_train)
                exit_timer.start()
                timer_started = True
        else:
            if timer_started:
                exit_timer.cancel()
                del exit_timer
                timer_started = False
            
def reset_input():
    global timer_started, exit_timer, current_input, current_delays, previous_delays, shifted_training_pattern, training_pattern, global_idx, input_idx
    if timer_started:
        exit_timer.cancel()
        del exit_timer
        timer_started = False
    
    current_input = ''
    current_delays = previous_delays = []
    shifted_training_pattern = training_pattern[global_idx]
    input_idx = 0
    
def uniform_input():
    global current_delays, previous_delays
    mu1 = statistics.mean(previous_delays)
    mu2 = statistics.mean(current_delays)
    two_sigma1 = 2*statistics.stdev(previous_delays)
    print ("unif check: " + str(mu1-two_sigma1) + " <= " + str(mu2) + " <= " + str(mu1+two_sigma1) + " answer is: " + str(mu1-two_sigma1 <= mu2 <= mu1+two_sigma1))
    return mu1-two_sigma1 <= mu2 <= mu1+two_sigma1

# main 
exit_timer = Timer(20.0, succeed_to_train)

root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Key>", keyPress)
w = Label(root, text="Press "+training_pattern[global_idx]+" by "+training_type[train_type_idx], bg="black", fg="white", width=root.winfo_screenwidth(), height=root.winfo_screenheight(), font=("Helvetica", 40))
w.pack()
 
root.mainloop()

