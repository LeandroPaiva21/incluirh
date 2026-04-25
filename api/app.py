from flask import Flask, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("SUPABASE_URL ou SUPABASE_KEY não configuradas")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def home():
    return render_template("tela_inicial.html")

@app.route("/teste-supabase")
def teste_supabase():
    try:
        resposta = supabase.table("usuarios").select("*").limit(1).execute()
        return {
            "status": "conectado",
            "dados": resposta.data
        }
    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e)
        }

def handler(request, *args, **kwargs):
    return app(request.environ, lambda *args: None)