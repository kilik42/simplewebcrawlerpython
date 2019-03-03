import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
##printing
print(questions[0].get("id",0))

for question in questions:
    print(questions[0].select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
