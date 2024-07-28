from flask import Flask, render_template, request, redirect, url_for, flash
from main import find_fragrance

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_fragrance():
    if request.method == 'POST':
        # Implement your logic for adding fragrance here
        flash('Fragrance added successfully!')
        return redirect(url_for('index'))
    return render_template('add_fragrance.html')

@app.route('/search', methods=['GET', 'POST'])
def search_fragrance():
    if request.method == 'POST':
        search_term = request.form['search_term']
        if search_term:  # Check if search term is not empty 
            results = find_fragrance(search_term)  # Call the find_fragrance function
            return render_template('search_results.html', results=results)
    return render_template('search_fragrance.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_fragrance():
    if request.method == 'POST':
        # Implement your logic for deleting fragrance here
        flash('Fragrance deleted successfully!')
        return redirect(url_for('index'))
    return render_template('delete_fragrance.html')

if __name__ == "__main__":
    app.run(debug=True)