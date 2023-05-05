import os
import shutil
import requests
import glob

# 替换成你的API密钥
API_KEY = ""


gpt_url = "https://api.openai.com/v1/chat/completions"

def generate_gpt_response(prompt):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    response = requests.post(gpt_url, headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, json=data)

    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        print(response.text)
        return "未知"

    response_data = response.json()
    response_text = response_data["choices"][0]["message"]["content"].strip()
    
    return response_text

def classify_document(document, categories):
    prompt = f"请将以下文档内容分类：\n\n{document}\n\n可选分类：{', '.join(categories)}\n\n分类结果为："
    classification = generate_gpt_response(prompt)
    
    if classification in categories:
        return classification
    else:
        return "未知"

def move_file_to_category_folder(file_path, category):
    file_name = os.path.basename(file_path)
    category_folder = os.path.join("Inbox", category)
    os.makedirs(category_folder, exist_ok=True)
    new_file_path = os.path.join(category_folder, file_name)
    shutil.move(file_path, new_file_path)

def read_md_files(folder_path):
    md_files = glob.glob(f"{folder_path}/*.md")
    return md_files

def main():
    source_folder = "Inbox"
    categories = ["科技", "历史", "文学", "艺术", "教育", "娱乐", "体育", "政治"]

    md_files = read_md_files(source_folder)

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8") as file:
            document = file.read()

        classification = classify_document(document, categories)
        print(f"文件：{file_path}")
        print(f"建议分类：{classification}\n")

        # 如果需要调整分类，可以在此处进行调整
        # classification = "新分类"

        move_file_to_category_folder(file_path, classification)
        print(f"已将文件从 {file_path} 移动到 '分类文件夹/{classification}'\n")

if __name__ == "__main__":
    main()

