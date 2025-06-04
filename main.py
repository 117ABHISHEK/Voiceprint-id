from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os, uuid, json, traceback
import numpy as np
import librosa
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

DB_FILE = 'voice_db.json'

# Create DB if not exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump({}, f)


def load_db():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    try:
        audio = request.files['audio']
        username = request.form['username']
        filename = f"{uuid.uuid4()}.wav"
        audio.save(filename)

        features = extract_features(filename).tolist()

        db = load_db()
        db[username] = features  # ✅ Only this gets saved
        save_db(db)

        os.remove(filename)
        return jsonify({'message': f'{username} registered successfully!'})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500



@app.route('/verify', methods=['POST'])
def verify():
    try:
        audio = request.files['audio']
        username = request.form['username']
        filename = f"{uuid.uuid4()}.wav"
        audio.save(filename)

        features = extract_features(filename).reshape(1, -1)
        db = load_db()

        if username not in db:
            return jsonify({
                'authenticated': False,
                'message': 'User not found'
            }), 404

        stored_features = np.array(db[username]).reshape(1, -1)
        similarity = cosine_similarity(features, stored_features)[0][0]

        os.remove(filename)

        return jsonify({
            'username': username,
            'similarity': round(float(similarity), 3),
            'authenticated': similarity >= 0.8  # ✅ Only sent, not saved
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
