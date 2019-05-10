def createHtml(newContent, filename):
    headers = getHeaders()
    ending = getPageEnd()

    completeContent = headers + """
    """ + newContent + """
""" + ending

    f = open('python_page.html','w+')
    f.write(completeContent)
    f.close()
    import webbrowser
    webbrowser.open_new_tab(filename)

def getHeaders():
    f = open('header.html', 'r')
    headers = f.read()
    return headers

def getPageEnd():
    f = open('page_end.html', 'r')
    ending = f.read()
    return ending

def myCreateNewTag(tagName, string):
    tag = "<" + tagName + ">" + string + "</" + tagName + ">"
    return tag

def myCreateNewTagWClass(tagName, string, classname):
    tag = "<" + tagName + " class=\"" + classname + "\">" + string + "</" + tagName + ">"
    return tag