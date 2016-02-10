'''
Created on 09 june 2015 г.

@author: miroslavgoncharenko; anastsianikolaeva
'''

def invert_condition(cnd):
    return {
        '1' : '2',
        '2' : '1',
        's' : 'h',
        'h' : 's'
    }.get(cnd)

def create_cur_sb_array(arm_words, leg_words, nouns, sb_order):
    a_i = l_i = n_i = 0
    current_words = []
    for cur_val in sb_order:
        if cur_val == 'a':
            current_words += arm_words[a_i:a_i+4]
            a_i += 4
        elif cur_val == 'l':
            current_words += leg_words[l_i:l_i+4]
            l_i += 4
        elif cur_val == 'n':
            current_words += nouns[n_i:n_i+4]
            n_i += 4
    file = open("./words.tem",'wb')

    s = "array {"
    file.write(s.encode("UTF-8"))
    for caption in current_words:
        s = "text { caption = \""+caption+"\"; description = \""+caption+"\";};"
        file.write(s.encode("UTF-8"))
    s = "}word_array;"
    file.write(s.encode("UTF-8"))
    file.close()

import random, subprocess, sys, os

al         = ['a','l']
seq_type   = ['1','2']
difficulty = ['s','h']
current_design = []
random.shuffle(al)
random.shuffle(seq_type)
random.shuffle(difficulty)

current_design.append((al[0] + seq_type[0] + difficulty[0]))
for i in range(1,8):

    dead_end = (al[i%2] + invert_condition(current_design[i-1][1]) + current_design[i-1][2] in current_design) and \
    (al[i%2] + current_design[i-1][1] + invert_condition(current_design[i-1][2]) in current_design)

    if dead_end:
        new_val = al[i%2] + current_design[i-1][1] + current_design[i-1][2]
        if new_val in current_design:
            print("This should never happen")
            break
    else:
        while True:
            if random.randint(0,1) == 0:
                new_val = al[i%2] + invert_condition(current_design[i-1][1]) + current_design[i-1][2]
            else:
                new_val = al[i%2] + current_design[i-1][1] + invert_condition(current_design[i-1][2])

            if not new_val in current_design:
                break

    current_design.append(new_val)

current_design.insert(4,'n')
#print("experiment scenaries initialized\n")
#print(*current_design, sep='\n')

# arm_words = ["подумать", "провести", "получать", "мешать", "указать", "явиться", "напомнить", "защищать", "приглашать", "стучать", "прятать", "ругать", "наказать", "прикрывать", "сжимать", "увлечь", "выучить", "скрипеть", "набраться", "накормить", "угощать", \
# "уделить", "сломаться", "косить", "смешать", "взойти", "винить", "одевать", "целиться", "метить", "взбить", "чертить", "загнуть", "молоть", "взмахивать"]
#
# leg_words = ["читать", "искать", "передать", "обладать", "определять", "находить", "доказать", "выпускать", "владеть", "покачать", "трогать", "мыслить", "вкладывать", "обвинить", "раскрывать", "усилить", "твердить", "смущать", "путать", "гонять", "развить", \
# "утешать", "вешать", "расширять", "посмеяться", "тосковать", "возмутить", "задевать", "растаять", "спутать", "чинить", "клевать", "вынуждать", "залечь", "засверкать"]
#
# nouns = ["комната", "директор", "звезда", "бутылка", "кресло", "лестница", "колесо", "публикация", "бассейн", "сиденье", "учебник", "конверт", "гвоздь", "таблетка", "конфета", "простыня", "папироса", "грамота", "упаковка", "занавеска", "раковина", "отпечаток", \
# "пружина", "кошелек", "клумба", "духовка", "глобус", "баррикада", "капюшон", "компрессор", "гавань", "застежка", "парусник", "этажерка", "отвертка"]

arm_words = ["ругать","увлечь","косить","взойти","винить","метить","взбить","молоть","указать","стучать","прятать","сжимать","выучить","угощать",\
             "уделить","смешать","одевать","чертить","загнуть","подумать","провести","получать","защищать","наказать","скрипеть","целиться","оплатить","изобрести"]

leg_words = ["читать","искать","путать","гонять","вешать","отмыть","залечь","раздуть","утолить","владеть","мыслить","усилить","смущать","развить",\
            "утешать","спутать","клевать","обнести","вертеть","обладать","находить","доказать","покачать","обвинить","твердить","задевать","растаять","выпускать"]

nouns = ["куртка","кресло","гавань","колесо","клумба","звезда","глобус","гвоздь","гавань","учебник","сиденье","пружина","кошелек","конфета","конверт",\
         "комната","капюшон","бутылка","бассейн","этажерка","упаковка","таблетка","раковина","простыня","папироса","лестница","застежка","занавеска"]

total_arm_words = []
total_leg_words = []
total_nouns = []
for i in range(0,7):
    tmp = arm_words[0:12]
    random.shuffle(tmp)
    total_arm_words += tmp
    tmp = arm_words[12:24]
    random.shuffle(tmp)
    total_arm_words += tmp
    tmp = arm_words[24:]
    random.shuffle(tmp)
    total_arm_words += tmp

    tmp = leg_words[0:12]
    random.shuffle(tmp)
    total_leg_words += tmp
    tmp = leg_words[12:24]
    random.shuffle(tmp)
    total_leg_words += tmp
    tmp = leg_words[24:]
    random.shuffle(tmp)
    total_leg_words += tmp

    tmp = nouns[0:12]
    random.shuffle(tmp)
    total_nouns += tmp
    tmp = nouns[12:24]
    random.shuffle(tmp)
    total_nouns += tmp
    tmp = nouns[24:]
    random.shuffle(tmp)
    total_nouns += tmp

#print("\narmwords:\n")
#print(*total_arm_words, sep='\n')

total_experiment_sb_order = [[0 for x in range(12)] for x in range(9)] #create 2d array for holding total seq of sb

for i in range(0,9):
    sb_types = ['a','l','n']
    for k in range(0,3):
        sb_types += ['a','l','n']

    random.shuffle(sb_types)

    total_experiment_sb_order[i][0] = sb_types.pop(random.randint(0,len(sb_types)-1))
    total_experiment_sb_order[i][1] = sb_types.pop(random.randint(0,len(sb_types)-1))
    total_experiment_sb_order[i][2] = sb_types.pop(random.randint(0,len(sb_types)-1))

    #for j in range(3,36):
    j = 3
    dead_end = False
    while len(sb_types) != 0:
        if not dead_end:
            while True:
                idx = random.randint(0,len(sb_types)-1)
                tmp_sb_type = sb_types[idx]
                if not (tmp_sb_type == total_experiment_sb_order[i][j-1] and tmp_sb_type == total_experiment_sb_order[i][j-2] and
                        tmp_sb_type == total_experiment_sb_order[i][j-2]):
                    sb_types.pop(idx)
                    total_experiment_sb_order[i][j] = tmp_sb_type
                    j+=1
                    break
                else:
                    dead_end = True
                    tmp_sb_type = sb_types[0]
                    for cur_sb in sb_types[1:]:
                        dead_end = dead_end and cur_sb == tmp_sb_type
                    break
        else:
            while len(sb_types) != 0:
                while True:
                    idx = random.randint(2,j-3)
                    if total_experiment_sb_order[i][idx-2] == total_experiment_sb_order[i][idx-1] and sb_types[0] == total_experiment_sb_order[i][idx-1] or \
                    sb_types[0] == total_experiment_sb_order[i][idx] and total_experiment_sb_order[i][idx] == total_experiment_sb_order[i][idx+1]:
                        continue
                    else:
                        total_experiment_sb_order[i].insert(idx,sb_types.pop(0))
                        j+=1
                        break
            list(filter((0).__ne__, total_experiment_sb_order[i])) # delete redundant zeros from initialization

path_to_experiment_folder = "C:\\Documents and Settings\\Admin\\Рабочий стол\\Experiments\\Nastia PhD"
path_to_presentation_launcher = "C:\\Program Files\\Neurobehavioral Systems\\Presentation\\Version172100814\\PresentationLauncher.exe"
subject_id = sys.argv[1] #"subject_id"

if not os.path.exists(path_to_experiment_folder+'/logs/'+subject_id):
	os.makedirs(path_to_experiment_folder+'/logs/'+subject_id)

if not os.path.exists(path_to_experiment_folder+'/recorded_responces/'+subject_id):
	os.makedirs(path_to_experiment_folder+'/recorded_responces/'+subject_id)

#print("Start forming function calls...\n")
for i in range(0,9):
    create_cur_sb_array(total_arm_words[16*i:16*(i+1)], total_leg_words[16*i:16*(i+1)], total_nouns[16*i:16*(i+1)], total_experiment_sb_order[i])
    if current_design[i] != 'n':
        cur_al = {
            'a' : "arm",
            'l' : "leg"
        }.get(current_design[i][0])

        cur_st = {
            '1' : "on_input",
            '2' : "on_pause"
        }.get(current_design[i][1])

        cur_df = {
            's' : "simple",
            'h' : "hard"
        }.get(current_design[i][2])

        subprocess.call([path_to_presentation_launcher, '-e',path_to_experiment_folder+'\\testo.exp', '-s', path_to_experiment_folder+'\\'+cur_al+'_'+cur_st+'_'+cur_df+'_series.sce', '-n', subject_id, '-o','-l', path_to_experiment_folder+'/logs/'+
                        subject_id+'/'+subject_id+'_'+current_design[i]+'.log'])
        #print(path_to_presentation_launcher+ ' -s ' + cur_al+'_'+cur_st+'_'+cur_df+'_series.sce '+ ' -n '+ subject_id+ ' -l '+ path_to_experiment_folder+'/'+
        #                subject_id+'/'+subject_id+'_'+current_design[i]+'.log')
    else:
        subprocess.call([path_to_presentation_launcher, '-e',path_to_experiment_folder+'\\testo.exp', '-s', path_to_experiment_folder+'/no_action_series.sce', '-n', subject_id, '-o','-l', path_to_experiment_folder+'/logs/'+
                        subject_id+'/'+subject_id+'_'+current_design[i]+'.log'])
        #print(path_to_presentation_launcher+ ' -s '+ 'no_action_series.sce'+ ' -n '+ subject_id+ ' -l '+ path_to_experient_folder+'/'+
        #                subject_id+'/'+subject_id+'_'+current_design[i]+'.log')


#    subprocess.call([path_to_presentation_launcher, '-e',path_to_experiment_folder+'\\testo.exp','-s', path_to_experiment_folder+'\\arm_on_input_simple_series.sce', '-n', subject_id, '-o','-l', path_to_experiment_folder+'\\logs\\'+
#							subject_id+'\\'+subject_id+'_a1s.log'])
#print(path_to_presentation_launcher, '-e',"'"+path_to_experiment_folder+'/testo.exp'+"'",'-s', "'"+path_to_experiment_folder+'/'+'arm_on_input_simple_series.sce'+"'", '-n', subject_id, '-o','-l', "'"+path_to_experiment_folder+'/'+
#                        subject_id+'/'+subject_id+'_a1s.log'+"'")
os.remove("./words.tem")
