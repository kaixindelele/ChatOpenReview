from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re

def clean_reply_text(text):
    # 将换行符分隔的字符和数字连接起来
    cleaned_text = re.sub(r'(?<!\.)\n', ' ', text)
    return cleaned_text

url = 'https://openreview.net/forum?id=OoNmOfYVhEU'

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)

# 获取所有审稿意见元素
review_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "note_with_children") and contains(@class, "comment-level-odd")]')))

reviews = {}

for review_element in review_elements:
    review_text = review_element.text.strip()
    reviewer_id = review_element.find_element(By.CSS_SELECTOR, ".meta_row .signatures").text.split()[-1]
    
    # 获取当前审稿意见下的所有审稿回复元素
    reply_elements = review_element.find_elements(By.XPATH, './/*[contains(@class, "note_with_children") and contains(@class, "comment-level-even")]')
    replies = [reply_element.text.strip() for reply_element in reply_elements]
    
    reviews[reviewer_id] = {
        "review_text": review_text,
        "replies": replies
    }

driver.quit()

# 打印审稿人ID以及对应的审稿文本和审稿回复
for reviewer_id, review_data in reviews.items():
    # print(f"Reviewer ID: {reviewer_id}")
    # print(f"Review text: {review_data['review_text']}")
    # print("Replies:")
    for reply_index, reply in enumerate(review_data['replies']):        
        print("reply_index:", reply_index)
        print("reply:", reply)
        print("^" * 50)
        cleaned_reply = clean_reply_text(reply)
        print("cleaned_reply:", cleaned_reply)
        print("-" * 50)
    print("*" * 50)
