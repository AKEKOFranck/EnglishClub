from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    nom = request.form['nom']
    email = request.form['email']
    
    # Afficher les données dans la console
    print(f"Nom: {nom}")
    print(f"Email: {email}")
    
    # Faire quelque chose avec les données (par exemple, les afficher)
    result = [nom, email]
    
    # Retourner une réponse (par exemple, un message de succès)
    return "Données reçues avec succès!"

if __name__ == '__main__':
    app.run(debug=True)