#-*-coding:utf-8-*-
import os
import json

source_path = os.path.join(os.environ.get('APPDATA'), '../LocalLow/Failbetter Games/Sunless Sea')    # 游戏文件路径
output_path = './SSA_CSVOutput/'    # 输出路径
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
text_keys = [   # 包含需翻译文本的键
    'AvailableAt',
    'ButtonText',
    'ChangeDescriptionText',
    'Description',
    'HumanName',
    'Label',
    'LevelDescriptionText',
    'MoveMessage',
    'Name',
    'Teaser',
    'Tooltip'
]
datas = {}  # 游戏数据

# 加载文件
for file_name in files:
    path = os.path.join(source_path, file_name)
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    datas[file_name] = data
    print(f'[INFO] 成功加载文件：{path}')

# 解析数据
def prase(entry_key, obj) -> None:  # 解析数据内容为条目
    if isinstance(obj, dict):
        for key, value in obj.items():
            current_entry_key = f'{entry_key}||{key}'   # 正在处理之值的键
            if key in text_keys and value is not None:
                entries[current_entry_key] = value
            prase(current_entry_key, value)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            current_entry_key = f'{entry_key}||{index}'     # 正在处理之值的键
            prase(current_entry_key, value)

for file_name, data in datas.items():
    # 解析
    entries = {}    # 词条
    prase(f'{file_name}:', data)

    output = ''
    for key, text in entries.items():
        output = output + f'{key},"{text.replace('"', '""').replace('\r\n', '\\n')}",""\n'  # 此游戏使用``\r\n``充当换行符

    # 输出
    path = os.path.join(output_path, file_name).replace('.json', '.csv')    # 输出路径
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(output)

    print(f'[INFO] 成功解析文件：{file_name}')

print('[INFO] 所有文件已解析完成。')
os.system('pause')