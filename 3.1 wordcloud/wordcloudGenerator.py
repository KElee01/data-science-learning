from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_file = open("中国社会各阶级的分析", encoding="utf8")
text = text_file.read()
wordcloud = WordCloud(
    font_path="SourceHanSerifCN-Medium.otf"
    ).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()