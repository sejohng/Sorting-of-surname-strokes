stroke_dict = {}

with open('Unihan_IRGSources.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('U+'):
            parts = line.strip().split('\t')
            if 'kTotalStrokes' in parts[1]:
                char = chr(int(parts[0][2:], 16))
                stroke_count = int(parts[2].split()[0])  # 只取第一个数字
                stroke_dict[char] = stroke_count

# 定义排序函数
def get_strokes(name):
    # 使用 stroke_dict 来确定姓名的笔画数
    # 如果某个字符不在字典中，我们默认其笔画数为0
    surname_strokes = stroke_dict.get(name[0], 0)
    name_strokes = sum([stroke_dict.get(char, 0) for char in name[1:]])  # 除姓之外的部分
    
    # 返回的是一个元组，首先考虑姓的笔画数，然后考虑名的笔画数
    return (surname_strokes, name_strokes)

# 读取名单中的姓名
with open('test.txt', 'r', encoding='utf-8') as file:
    names = [line.strip() for line in file.readlines() if line.strip()]
    
# 使用排序函数对姓名进行排序
sorted_names = sorted(names, key=get_strokes)

# 输出排序后的结果
for name in sorted_names:
    print(name)
    