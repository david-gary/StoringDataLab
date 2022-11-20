from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def jobs():
    # TODO: Load the jobs from the JSON file

    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)
