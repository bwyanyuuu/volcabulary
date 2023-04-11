import random
# c = input("your text: ")
c = '''allow drop cheat chat lovely pot case sure catch polite common hunt heat hit glasses rise if whether thought though yo direction arrow key paint strange officer office police study excit farther if might graw beaf way borrow face heart bore language invite taste joy bake wake become better except compete everything below fill group move movie vegetable with without lettuce lead-led-led from during rest up to hide just experience bother ever train limit post perfect there is trick however chart secret cheate cheat
space online election shape America Asia Europe Africa Australia candidate deal following number add ad advertisment prize broud both lend-lent-lent borrow cigarette trip broke however rich hill only also beside become choice actually quiet quite called main  mean difficult traffic each close mind kind carefully against lose-lost-lost as industry exciting besides serve service thought through though reason role instead few sample simple value'''
cc = '''never mind
a few
nether nor
either or
after all
right away
frist of all
as a result
take part'''
li = c.split(' ') + cc.split('\n')
maxlen = len(li)
i = 0
while len(li) > 0:
    x = random.randint(0, len(li)-1)
    print(li[x])
    li.remove(li[x])
    i += 1
    input('')
        
print('finish.')
