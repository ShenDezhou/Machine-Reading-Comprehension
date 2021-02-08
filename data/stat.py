import json

import numpy

ranges = range(20)
ratio = 0.9
with open('train.json','r',encoding='utf-8') as f:
    all_items = json.load(f)
    questions = [len(item['Content']) for item in all_items]
    stats = [numpy.percentile(questions, i*5) for i in ranges]
    print('cl:', stats)
    all_q = []
    all_o = []
    for item in all_items:
        for q in item["Questions"]:
            all_q.append(len(q["Question"]))
            all_o.extend(q['Choices'])

    stats = [numpy.percentile(all_q, i * 5) for i in ranges]
    print('ql:', stats)
    all_o = [len(l) for l in all_o]
    stats = [numpy.percentile(all_o, i * 5) for i in ranges]
    print('ol:', stats)

    #questions = [len(item['Questions']) for item in all_items]


print('FIN')
