from flask import request, render_template, send_from_directory, abort, flash
from pytube import YouTube
from werkzeug.utils import secure_filename

from os import path
from app import app


FILE_PATH = app.config['DOWNLOADS_FOLDER']


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('home.html', title='Youtube-dw Home')


@app.route('/get-video', methods=['GET', 'POST'])
def get_video():
    url = request.form.get('url')
    yt = YouTube(url)

    file_name: str = secure_filename(f'{yt.title}.mp4')

    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(22)

    stream.download(FILE_PATH, filename=file_name)

    try:
        flash("Downloading")
        return send_from_directory(FILE_PATH, file_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    return render_template('error.html', msg=ex, code=ex.code)