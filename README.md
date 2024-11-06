# ssedata
[《无光之海》民间汉化 https://paratranz.cn/projects/12215]所用的游戏数据处理工具。

## getcsv.py
获取``paratranz``所需的``.csv``文件。

至少运行一次《无光之海》后直接运行``getcsv.py``，将在``./SSA_CSVOutput/``生成``.csv``文件。

## pack.py
将``paratranz``文件解析为``.json``文件。

将``pack.py``与``raw``置于同一目录下，使用`py.exe pack.py <版本号>`生成文件。
