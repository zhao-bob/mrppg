from re import sub
from collections import Counter
from PIL import Image
from jieba import cut
from numpy import array
from wordcloud import WordCloud

with open('教师节赞美语句.txt', encoding='utf8') as fp:
    content = set(fp.readlines())
text = sub('\d+', '', ''.join(content))
stopwords = ('教师节', '祝您', '老师', '我们', '教师', '学生', '孩子')
words = filter(lambda word: len(word)>1 and word not in stopwords, cut(text))
freq = dict(Counter(words).most_common(200))
# 用来控制词云图大小和形状的心形图片
im = Image.open('心形图片.png')
size = im.size
wc = WordCloud(r'C:\Windows\fonts\simfang.ttf',
               width=size[0], height=size[1],
               mask=array(im),
               background_color='white', font_step=3,
               random_state=False, prefer_horizontal=0.8)
wc.generate_from_frequencies(freq).to_image().show()
