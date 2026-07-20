from flask import Flask, render_template_string

app = Flask(__name__)

# Alaabtaada iyo kaydkaaga oo aad halkaan si manual ah uga beddeli kartid
inventory_items = [
    {"id": 1, "title": "Buugga Barashada Kombuyuutarka", "price": 15, "stock": 25},
    {"id": 2, "title": "Qalabka Elektaroonigga ah", "price": 45, "stock": 10},
    {"id": 3, "title": "Shaah Geedo Dabiici ah", "price": 5, "stock": 50}
]

@app.route('/')
def home():
    # Bog HTML ah oo si toos ah u soo bandhigaya alaabtaada
    html_content = """
    <!DOCTYPE html>
    <html lang="so">
    <head>
        <meta charset="UTF-8">
        <title>Arafat Shop - Inventory</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f6f9; padding: 20px; }
            h1 { color: #2c3e50; text-align: center; }
            .card { background: white; padding: 15px; margin: 10px auto; max-width: 500px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            p { margin: 5px 0; color: #555; }
        </style>
    </head>
    <body>
        <h1>Arafat Multi-Store Inventory</h1>
        {% for item in items %}
        <div class="card">
            <h3>{{ item.title }}</h3>
            <p><strong>Qiimaha:</strong> ${{ item.price }}</p>
            <p><strong>Kaydka Hadhay (Stock):</strong> {{ item.stock }} xabo</p>
        </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html_content, items=inventory_items)

if __name__ == '__main__':
    app.run(debug=True)
