from urllib.request import urlopen
from bs4 import BeautifulSoup

title_list = []
page_num = 1
while(1) :

    try :
        url = "http://terms.naver.com/list.nhn?cid=40942&so=st3.asc&page="+str(page_num)+"&categoryType=&categoryId=40942&viewType="
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
    except :
        break

    for a in soup.find_all('a'):
        if "<strong>" in str(a) :
            if "[" in a.text :
                title_list.append(a.text[:a.text.index("[")-1])
            else :
                title_list.append(a.text)

    title_list = title_list[:-1]
    print(page_num)
    page_num += 1


print("Save as file... ", end="")
f = open("doosan.txt", "w")
f.write("%s : %d\n" % ("Last page : ", page_num-1))
for title in title_list :
    f.write(title+'\n')
print("Done")