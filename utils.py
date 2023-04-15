from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
import openreview
from rich.progress import track

def get_paper_links(invitation):
    def get_url(bibtex):
        url_pattern = r'url={(https?://\S+)}'
        url = re.search(url_pattern, bibtex)
        if url:
            return url.group(1)
        else:
            return ""

    paper_links = {}
    client = openreview.Client(baseurl='https://api.openreview.net')
    submissions = client.get_all_notes(
        invitation=invitation, details='directReplies')
    for submission in track(submissions):
        url = get_url(submission.content["_bibtex"])
        title = submission.content["title"]
        paper_links[title] = url
    return paper_links

def clean_reply_text(text):
    # 将换行符分隔的字符和数字连接起来
    cleaned_text = re.sub(r'(?<!\.)\n', ' ', text)
    return cleaned_text


#
def get_responses(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    # 获取所有审稿意见元素
    review_elements = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//*[contains(@class, "note_with_children") and contains(@class, "comment-level-odd")]')))

    reviews = {}

    for review_element in review_elements:
        review_text = review_element.text.strip()
        reviewer_id = review_element.find_element(By.CSS_SELECTOR, ".meta_row .signatures").text.split()[-1]

        # 获取当前审稿意见下的所有审稿回复元素
        reply_elements = review_element.find_elements(By.XPATH,
                                                      './/*[contains(@class, "note_with_children") and contains(@class, "comment-level-even")]')
        replies = [reply_element.text.strip() for reply_element in reply_elements]

        reviews[reviewer_id] = {
            "review_text": review_text,
            "replies": replies
        }

    driver.quit()

    return reviews



if __name__ == "__main__":
    invitation = "NeurIPS.cc/2021/Conference/-/Blind_Submission"
    paper_links = get_paper_links(invitation)
    print(paper_links)
