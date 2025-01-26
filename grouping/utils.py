import random

def create_groups(foreign_count, japanese_count):
    groups = []
    colors = ['赤-red-', '青-blue-', '黄-yellow-', 'オレンジ-orange-', '紫-purple-', '黒-black-', 'ピンク-pink-', '緑-green-']

    total_people = foreign_count + japanese_count
    group_size = 5

    foreign_in_group = 1
    for i in range(total_people // group_size):
        group_foreigners = random.randint(1,2)
        #1～2人の外国人をランダムに配置
        group_japanese = group_size - group_foreigners
        groups.append({
            'group_number': i + 1,
            'foreigners': group_foreigners,
            'japanese': group_japanese,
            'color': colors[i % len(colors)],
        })

    return groups