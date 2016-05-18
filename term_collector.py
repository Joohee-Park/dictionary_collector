from urllib.request import urlopen
from bs4 import BeautifulSoup
from Tree import Tree

def build_cattree(url) :

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    root = Tree()

    for box in soup.find_all("div", { "class" : "m_detail"}) :
        for a in box.find_all("a") :
            categoryId = str(a)[str(a).index("categoryId=")+len("categoriId="):str(a).index("\"><span>")]
            title = a.text[:a.text.index(" (")]

            child = build_cattree("http://terms.naver.com/list.nhn?cid=40942&categoryId="+str(categoryId))
            child.parent = root
            child.parent.children.append(child)
            child.title = title
            child.categoryId = categoryId
            print(child.title)

    return root

def print_leaf(root, category) :

    if len(root.children) == 0 :
        print(root.title, category)
        root.category = category
        return

    for child in root.children :
        child_category = category[:]
        child_category.append(child.title)
        print_leaf(child, child_category)

def extract_leaf_node(root, file) :

    if len(root.children) == 0 :
        file.write("%s\t%s\t%s\n" % (root.title, root.categoryId, "\t".join([cat for cat in root.category])))

    for child in root.children :
        extract_leaf_node(child, file)

root = build_cattree("http://terms.naver.com/list.nhn?cid=40942&categoryId=31945")
print_leaf(root, ["스포츠"])
f = open("leaf.txt", "w")
extract_leaf_node(root, f)