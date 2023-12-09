def infectHtml(fileName, infectedContent):
    with open(fileName, 'r') as fp:
        lines = fp.readlines()
    for index, line in enumerate(lines):
        if line.strip().lower().startswith('<html>'):
            lines.insert(index+1, infectedContent)
            break
    with open(fileName, 'w') as fp:
        fp.writelines(lines)

content = '<head><script>window.onload=function(){alert("test");}</script></head>\n'
infectHtml('index.html', content)
