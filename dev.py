from src.index import create_app

# -------------------------
# APP RUNNER for devlopment
# -------------------------
if __name__ == '__main__':
    create_app().run(debug=True)
