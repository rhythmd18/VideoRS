from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/feed', methods=['GET'])
def recommend_videos():
    # Parse query parameters
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')
    
    # (Optional) Log query parameters
    print(f'Username: {username}, Category_ID: {category_id}, Mood: {mood}')

    # Generate recommendations
    recommendations = generate_recommendations(username, category_id, mood)

    # return recommendations as JSON
    return jsonify(recommendations)


def generate_recommendations(username, category_id, mood):
    # Placeholder for recommendation logic
    return [
        {'video_id': '123', 'title': 'Motivational Video', 'category': 'Self-help'},
        {'video_id': '456', 'title': 'Inspirational Video', 'category': 'Wellness'}
    ]


if __name__ == '__main__':
    app.run(debug=True, port=5000)