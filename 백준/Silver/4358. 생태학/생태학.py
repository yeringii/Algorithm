import sys

#입력 처리
count = 0
tree = {}

for line in sys.stdin:
    tree_name = line.strip()
    #입력 없을 시
    if not tree_name:
        break
    if tree_name not in tree:
        tree[tree_name] = 1
    else:
        tree[tree_name] += 1
    count += 1

#사전 순 정렬
sorted_tree = sorted(tree.keys())

for tree_name in sorted_tree:
    #백분율 계산
    percentage = (tree[tree_name] / count) * 100
    print(f'{tree_name} {percentage:.4f}')