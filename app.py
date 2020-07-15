from flask import jsonify, Flask, request
import requests
import json

app = Flask(__name__)

r = requests.get(
        'https://api.github.com/search/repositories?q=created:<=2020-07-13&sort=stars&order=desc&per_page=100')
data = r.json()

@app.route('/', methods=['GET'])
def index():
    return jsonify(data)

@app.route('/A1count', methods=['GET'])
def repos_count_per_lang():
    languages = {}
    for x in range(100):
        num = 0
        for y in range(100):
            if (data['items'][x]['language'] == data['items'][y]['language']):
                num = num + 1
                language = {data['items'][x]['language']: num}
        languages.update(language)
    return '<h1>Number of repos using each language is : </br></h1>' + json.dumps(languages, indent=4)

@app.route('/A1list', methods=['GET'])
def repos_list_per_lang():
    reposdict = {}
    for x in range(100):
         reposList = []
         for y in range(100):
             if (data['items'][x]['language'] == data['items'][y]['language']):
                name = data['items'][y]['full_name']
                reposList.append(name)
                repos = {data['items'][x]['language']: reposList}
         reposdict.update(repos)

    return '<h1></br>List of repos using each language is : </br></h1>' + json.dumps(reposdict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

