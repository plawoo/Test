from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open('message_trans.txt', 'r', encoding='UTF-8').read()
wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2).generate(f)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('example1.png')
