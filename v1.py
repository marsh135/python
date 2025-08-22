def read_file():
    fileName = input("File name:  ")
    data = []
    file =  open(fileName)
    for line in file:
        line = line.strip().split("-")
        data.append(line)
    return data

def find_tallest_tree(tree_d):
    max_height = 0
    tallest_tree = ""
    
    for tree in tree_data:
        height = float(tree[1])
        if height > max_height:
            max_height = height
            tallest_tree = tree[0]
    return tallest_tree

tree_data = read_file()
tallest_tree = find_tallest_tree(tree_data)
print("Tallest tree: ", tallest_tree)

