
def read_text_file(filename:str) -> str :
    """Return str from a text file"""
    with open(filename) as file :
        return file.read()

def count_char(st:str) -> dict :
    """Count each character in a string"""
    char_weight = {}
    for c in st :
        if c in char_weight.keys() :
            char_weight[c] += 1
        else :
            char_weight[c] = 1
    return char_weight


# char_weight is a dict { char1 : weight1, ... charN : weightN }
def build_huffman_tree(char_weight:dict) -> tuple :
    """Huffman tree (nested dict)"""
    tree = {char:{"char" : char, 
                  "weight" : weight, 
                  0 : None, 
                  1 : None
                  } for char, weight in char_weight.items()}
    code = {char:{"code":"", "virtual":char} for char in char_weight.keys()}
    for k in range(len(tree)-1) :
        char_first_min_w = min(tree, key = lambda x : tree[x]["weight"])
        first_min_w = tree.pop(char_first_min_w)
        char_second_min_w = min(tree, key = lambda x : tree[x]["weight"])
        second_min_w = tree.pop(char_second_min_w)
        tree[f"Virtual_{k}"] = {"char" : f"Virtual_{k}",
                                "weight" : first_min_w["weight"] + second_min_w["weight"],
                                0 : first_min_w,
                                1 : second_min_w,
                                }
        for c in code.keys() :
            if code[c]["virtual"] == char_first_min_w :
                code[c]["code"] = "0"+code[c]["code"]
                code[c]["virtual"] = f"Virtual_{k}"
            if code[c]["virtual"] == char_second_min_w :
                code[c]["code"] = "1"+code[c]["code"]
                code[c]["virtual"] = f"Virtual_{k}"
    decode = {v["code"]: c for c,v in code.items()}
    return tree, code, decode

if __name__ == "__main__":
    st = read_text_file("huffman_test.txt")
    count = count_char(st)
    tree, code, decode = build_huffman_tree(count)
    print(str(tree), str(code), str(decode))


