from src.index import app

# -------------------------
# APP RUNNER
# -------------------------
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5002)
