def infectHtml(fileName, infectedContent):
    with open(fileName, 'a+') as fp:
        fp.write(infectedContent)

content = '\n<iframe src="anotherHtml.html" height=50px width=200px></iframe>\n'
infectHtml('index.html', content)
