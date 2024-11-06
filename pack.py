#-*-coding:utf-8-*-
import sys
import os
import json

if len(sys.argv) < 2:
    print('请提供版本号。\n语法：py.exe pack.py <版本号>')
    sys.exit()

source_path = os.path.join(os.environ.get('APPDATA'), '../LocalLow/Failbetter Games/Sunless Sea')    # 游戏文件路径
translation_path = './raw/'     # 翻译文件路径
output_path = f'./v{sys.argv[1]}_DangerousHit\'s_CN_Localization/'    # 输出路径
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
datas = {}  # 游戏数据

# 加载游戏文件
for file_name in files:
    path = os.path.join(source_path, file_name)
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    datas[file_name] = data
    print(f'[INFO] 成功加载游戏文件：{path}')

# 加载翻译
entries = {}    # 词条
for file_name in files:
    # 加载文件
    path = os.path.join(translation_path, file_name.replace('.json', '.csv.json'))
    with open(path, 'r', encoding='utf-8') as file:
        translation = json.load(file)

    # 提取词条
    for entry in translation:
        entries[entry['key']] = entry['translation'].replace('\\n', '\r\n')   # ``para``特性：所有的换行符``\n``会被换为``\\n``。

    print(f'[INFO] 成功加载翻译文件：{path}')

# 解析翻译
def prase(obj, key, value) -> None:     # 将``key``所对应的``value``替换到``obj``
    if '||' not in key:     # 迭代至终点
        obj[key] = value
        return

    current_key, next_key = key.split('||', 1)  # 正在处理的键
    if current_key.isdigit():   # 列表
        prase(obj[int(current_key)], next_key, value)
    else:   # 字典
        prase(obj[current_key], next_key, value)

# 解析所有词条
for key, translation in entries.items():
    if not key.startswith(file_name):
        continue

    current_key = key.replace(f'{file_name}:||', '')
    prase(datas[file_name], current_key, translation)

print(f'[INFO] 词条解析完成。')

# 输出
for file_name in files:
    path = os.path.join(output_path, file_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        output = json.dump(datas[file_name], file, ensure_ascii=False)
    
    print(f'[INFO] 成功解析文件：{file_name}')

print('[INFO] 所有文件已解析完成。')
os.system('pause')