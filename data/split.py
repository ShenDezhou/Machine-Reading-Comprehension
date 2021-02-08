import json
import random

ratio = 0.9
with open('train.json','r',encoding='utf-8') as f:
    with open('train_train.json', 'w', encoding='utf-8') as f_train:
        with open('train_val.json', 'w', encoding='utf-8') as f_validation:
            all_items = json.load(f)
            train_list = []
            valid_list = []
            train_id = random.sample(range(len(all_items)), k=int(len(all_items) * ratio))
            for i in range(len(all_items)):
                if i in train_id:
                    train_list.append(all_items[i])
                else:
                    valid_list.append(all_items[i])
            json.dump(train_list, f_train, ensure_ascii=False,indent=4)
            json.dump(valid_list, f_validation, ensure_ascii=False, indent=4)
print('FIN')
