
dict={
"merry":"god",
"christmas":"jul",
"and":"och", 
"happy":"gott",
"new":"nytt",
"year":"ar"
}

list=["merry","christmas","year"]
def translate(list):
    n=[]
    for i in list:
        m=dict[i]
        n.append(m)
    return n
print translate(list)


