import openreview
from rich.progress import track

client = openreview.Client(baseurl='https://api.openreview.net')
invitation = "NeurIPS.cc/2021/Conference/-/Blind_Submission"
submissions = client.get_all_notes(
    invitation=invitation, details='directReplies')

reviews = []
reviews_list = []
title_list = []
for submission in track(submissions):
    # print("submission:", submission)
    reviews = [reply for reply in submission.details["directReplies"]
               if reply["invitation"].endswith("Official_Review")]
    title_list.append(submission.content['title'])
    reviews_list.append(reviews)
    # print("reviews:", reviews)

with open('reviews_list.txt', 'w', encoding="utf-8") as f:
    for reviews_index, reviews in enumerate(reviews_list):
        f.write(title_list[reviews_index] + "\n")
        f.write(str(reviews) + "\n")
        f.write("-"*50 + "\n")
