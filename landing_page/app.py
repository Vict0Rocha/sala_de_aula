from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave-secreta-para-flash-messages'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Captura os dados do formulário
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Aqui você pode salvar os dados em um banco de dados ou enviar por e-mail
        print(f"Nome: {name}, E-mail: {email}, Mensagem: {message}")

        flash("Obrigado pelo contato! Recebemos sua mensagem.", "success")
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
