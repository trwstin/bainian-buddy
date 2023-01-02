import random

# 40+ phrases
phrases = { '新年快乐':'Happy New Year!',
            '大吉大利':'Good luck and big profit!',
            '吉星高照':'May your lucky star shine bright!',
            '吉祥如意':'Good luck and happiness to you!',
            '万事如意':'May all go well with you!',
            '心想事成':'May your dreams come true!',
            '一帆风顺':'Wish you smooth sailing journeys and experiences!',
            '年年有余':'Wish you abundance year after year!',
            '财源广进':'Wish you fortune and wealth in abudance!',
            '财源滚滚':'May profits pour in from all sides!',
            '招财进宝':'Usher in wealth and prosperity!',
            '金玉满堂':'May treasures fill your home!',
            '生意兴隆':'May your business prosper!',
            '步步高升':'May you continue growing taller!',
            '升官发财':'May you be promoted and gain wealth!',
            '事业有成':'Wish you success in your career!',
            '工作顺利':'Wish you a smooth experience at work!',
            '大展宏图':'May your grand ambitions come to fruition!',
            '平步青云':'May your career improve rapidly!',
            '飞黄腾达':'May you find rapid success in your career!',
            '马到成功':'May you receive rapid success!',
            '龙马精神':'Wish you a vigorous spirit!',
            '身体健康':'Wish you good health!',
            '岁岁平安':'May you continue to live peacefully!',
            '学习进步':'May your grades improve!',
            '学业有成':'May your find success in your studies!',
            '金榜提名':'Wish you top grades in major examinations!',
            '阖家幸福':'May your family be blessed!',
            '恭贺新禧':'Happy New Year!',
            '笑口常开':'May your life be filled with laughter!',
            '一本萬利':'May you receive big profits from investments!',
            '五福临门':'May the Five Blessings descend upon you!',
            '福寿双全':'Wish you both prosperity and longevity!',
            '出入平安':'Wish you peace wherever you go!',
            '愈来愈靓':'May you get prettier and prettier!',
            '天赐良缘':'May heaven help you find your soulmate!',
            '锦绣前程':'Wish you a bright future!',
            '寿比南山':'Wish you longevity of the mountains!',
            '前途无量':'May your future be limitless!',
            '前途似锦':'May your future be infinitely bright!',
            '突飞猛进':'May your career advance by leaps and bounds!'
}

# return random phrase
def choose_phrase(original):
    lst = list(dict.keys(phrases))
    lst.remove(original)
    new = random.choice(lst)
    return new

# return translation of phrase
def translate(phrase):
    return phrases.get(phrase)