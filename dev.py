from src.index import create_app

# -------------------------
# APP RUNNER for devlopment environment
# -------------------------
if __name__ == '__main__':
    create_app().run(debug=True)
