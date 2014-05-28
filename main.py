from web.static import app

if __name__ == '__main__':
    port = app.config.get('port', 8080)
    app.run(host='0.0.0.0', port=port, debug=True)
