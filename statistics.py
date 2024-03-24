import os
import csv
from collections import Counter
import jieba
import re

# 设定CSV文件所在的目录和结果文件路径
comments_dir = './output'
output_file = './high_freq_words.txt'

# 停用词列表（根据需要进行扩展）
with open('./stopwords.txt', 'r', encoding='utf-8') as file:
    stop_words = set([line.strip() for line in file])

# 自定义分词词典（根据需要进行扩展）
jieba.load_userdict('./userdict.txt')

# 初始化词频统计器
word_freq = Counter()


# 定义一个函数来去除字符串中的标点符号
def remove_punctuation(text):
    # 使用正则表达式去除标点符号
    return re.sub(r'[^\w\s]', '', text)


# 遍历目录中的所有CSV文件
for filename in os.listdir(comments_dir):
    if filename.endswith('.csv'):
        with open(os.path.join(comments_dir, filename), 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # 先去除标点符号
                comment_no_punctuation = remove_punctuation(row['content'])
                # 分词并去除停用词
                words = [word for word in jieba.cut(comment_no_punctuation) if word not in stop_words]
                # 更新词频统计
                word_freq.update(words)

# 选择出现频次较高的词语，这里示例选择前100个
most_common_words = word_freq.most_common(100)

# 保存到文件
with open(output_file, 'w', encoding='utf-8') as file:
    for word, freq in most_common_words:
        file.write(f"{word}: {freq}\n")

print("高频词提取完成，结果已保存到文件。")
