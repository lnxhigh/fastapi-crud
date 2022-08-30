def getList(inventory):
    lists = ""
    for id, content in inventory.items():
        lists += f"<li><a href='/items/{id}'>{content['title']}</a></li>"
    return lists

def getTitleList(inventory):
    titleList = []
    for id, content in inventory.items():
        titleList.append(content['title'])
    
    return titleList
