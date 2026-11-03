from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy Database (In-memory)
posts = [
    {
        "id": 1,
        "title": "Welcome to My Flask Blog",
        "author": "Chetana",
        "content": "This is the first post on my new blog! I built this using Flask and Jinja2. It was really fun to learn about server-side rendering and template inheritance."
    },
    {
        "id": 2,
        "title": "Why Jinja2 is Awesome",
        "author": "Chetana",
        "content": "Jinja2 makes it super easy to pass Python variables into HTML. You can use loops, if-conditions, and even template inheritance (like extending base.html), just like I did here!"
    }
]

# Comments ka dummy database
comments = {
    1: [{"author": "Rahul", "text": "Great start! Keep it up."}],
    2: [{"author": "Amit", "text": "Agreed, Jinja2 is very powerful."}]
}

# --- ROUTES ---

@app.route('/')
def home():
    # Saare posts list page par bhej rahe hain
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # Specific post aur uske comments nikal rahe hain
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    
    post_comments = comments.get(post_id, [])
    return render_template('post.html', post=post, comments=post_comments)

@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    # Form se naya comment le rahe hain
    author = request.form.get('author')
    text = request.form.get('text')
    
    if author and text:
        if post_id not in comments:
            comments[post_id] = []
        comments[post_id].append({"author": author, "text": text})
        
    # Comment add hone ke baad wapas usi post par redirect
    return redirect(url_for('post_detail', post_id=post_id))

if __name__ == '__main__':
    app.run(debug=True, port=5000)