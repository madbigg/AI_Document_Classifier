# 文档分类器（Document Classifier）

使用OpenAI的GPT-3.5-turbo模型对Markdown文件进行分类并将文件移动到相应的分类文件夹。

This tool uses OpenAI's GPT-3.5-turbo model to classify Markdown documents and move them into corresponding categorized folders.

# 功能 Features

从指定的待分类文件夹中读取Markdown文件。
使用GPT-3.5-turbo模型为每个文件生成分类建议。
将文件移动到相应的分类文件夹。
Read Markdown files from a specified folder.
Generate classification suggestions for each file using the GPT-3.5-turbo model.
Move the files into corresponding categorized folders.

# 使用方法 Usage

将您的OpenAI API密钥填入API_KEY变量。
根据需要修改source_folder和categories变量。
运行document_classifier.py。
Fill in your OpenAI API key in the API_KEY variable.
Modify the source_folder and categories variables as needed.
Run document_classifier.py.
