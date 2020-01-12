# from flask import Flask, request, render_template
# import requests
# import re

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/', methods=['POST'])
# def response():
#     headers = {
#         "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#     }
#     URL = request.form.get("url")

#     try:
#         page = requests.get(URL, headers=headers)
#     except:
#         print("Error while opening the URL")

#     words = page.text.replace('\n', ' ').split()
#     words = [word.lower() for word in words]

#     dictionary = dict()
#     regex = r"([^a-z'+])"

#     for word in words[:100]:
#         word = re.sub(regex, "", word)
#         counter = words.count(word)
#         dictionary[word] = counter

#     return render_template('index.html', dictionary=dictionary)

# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def response():
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    url = request.form.get("url")
    page = requests.get(url, headers=headers)
   
    words = page.text.replace('\n', ' ').split()

    words = [word.lower() for word in words]

    dictionary = dict()
    regex = r"([^a-z'+])"

    for word in words[:50]:
        word = re.sub(regex, "", word)
        counter = words.count(word)
        dictionary[word] = counter

    return render_template("index.html", url=url, dictionary=dictionary)

if __name__ == '__main__':
    app.run()