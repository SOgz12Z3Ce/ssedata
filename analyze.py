import os
import json

source_path = 'source/' # 'Sunless Sea/'
files = [   # 包含需翻译文本的文件
    'encyclopaedia/Associations.json',
    'encyclopaedia/CombatAttacks.json',
    'encyclopaedia/CombatItems.json',
    'encyclopaedia/SpawnedEntities.json',
    'encyclopaedia/Tutorials.json',
    'entities/areas.json',
    'entities/events.json',
    'entities/exchanges.json',
    'entities/qualities.json',
    'geography/Tiles.json',
]
datas = []

# 加载文件
for file in files:
    path = os.path.join(source_path, file)
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    print(f'[INFO] Success to load:{path}')
    datas.append(data)

# 处理数据
for data in datas:
    pass