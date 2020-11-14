import datetime
import os

from flask import Flask, Response, request, send_file, abort, jsonify
from flask_mongoengine import MongoEngine
from mongoengine.errors import ValidationError

import models
import config


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_NAME']
}

db = MongoEngine()
db.init_app(app)


class RandomStringGenerator(db.Document):

    alphabet = db.IntField()
    real_numbers = db.IntField()
    alphanumeric = db.IntField()
    integers = db.IntField()


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@app.route("/api/generate", methods=["POST"])
def generate_strings():
    filename = "random_strings.txt"

    stats_list = models.gen_random_alphabet(filename)

    response = RandomStringGenerator(
        alphabet=stats_list["alphabet"],
        real_numbers=stats_list["real_numbers"],
        alphanumeric=stats_list["alphanumeric"],
        integers=stats_list["integers"]).save()

    return {
        "success": True,
        "error": False,
        "data": {
            "download_link": config.DOWNLOAD_LINK % filename,
            "id": str(response.pk)
        }
    }

@app.route("/api/stats/<string:entry_id>", methods=["GET"])
def generate_string_stats(entry_id):
    if not entry_id:
        abort(404)

    try:
        data = RandomStringGenerator.objects.get(pk=str(entry_id))
    except ValidationError as e:
        abort(400)
    return {
        "success": True,
        "error": False,
        "data": {
            "alphabet": data.alphabet,
            "real_numbers": data.real_numbers,
            "alphanumeric": data.alphanumeric,
            "integers": data.integers
        }
    }

@app.route("/file/download/<string:filename>", methods=["GET"])
def download_file(filename):
    if not filename:
        abort(404, description="Not found error")

    return send_file(config.DOWNLOAD_PATH % filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
