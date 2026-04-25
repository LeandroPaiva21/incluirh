from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/")
def home():
    return render_template("tela_inicial.html")

# Handler para Vercel
def handler(request, *args, **kwargs):
    return app(request.environ, lambda *args: None)