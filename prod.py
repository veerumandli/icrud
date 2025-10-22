from src.index import create_app

# -------------------------
# APP RUNNER for prduction
# -------------------------
if __name__ == '__main__':
    create_app().run(debug=False, host='0.0.0.0', port=5002)
