release: flask db upgrade
web: gunicorn sent_extractor.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
