from flask import Flask, jsonify, request
from crypt import methods
app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hi~! This is test code of flash web server !! if you wannar get response Skill server, Go to /skill"

@app.route("/test", methods=["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list=[
            "abc", "def"]
        )
    return data

@app.route("/Skill", methods=["post","get"])
def skill():
    data = {
        "version" : "2.0",
        "template" : {
            "outputs": [
                {
                    "simpleText" : {
                        "text": "간단한 텍스트 요소입니다."
                        }
                    }
                ]
            }
        }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)