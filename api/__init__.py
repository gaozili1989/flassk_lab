from flask import Flask, jsonify
import psycopg2
from api.models import Health

def create_app(database, user, password):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE = database,
        USER = user,
        PASSWORD = password
    )

    @app.route('/health')
    def health():
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'], password = app.config['PASSWORD'])
        cursor = conn.cursor()
        cursor.execute('select * from health limit 5;')
        results = cursor.fetchall()
        result_objs = [Health(result).__dict__ for result in results]
        return jsonify(result_objs)

    @app.route('/health/<health_id>')
    def health_id(health_id):
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'], password = app.config['PASSWORD'])
        cursor = conn.cursor()
        cursor.execute('select * from health where id = %s limit 5;', (health_id,))
        results = cursor.fetchall()
        result_objs = [Health(result).__dict__ for result in results]
        return jsonify(result_objs)

    return app