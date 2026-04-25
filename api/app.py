from flask import Flask, render_template
from supabase import create_client
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def home():
    return render_template("tela_inicial.html")

# Handler para Vercel
def handler(request, *args, **kwargs):
    return app(request.environ, lambda *args: None)