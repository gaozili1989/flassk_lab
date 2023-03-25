from settings import DATABASE, USER, PASSWORD
from api import create_app

app = create_app(user = USER, database = DATABASE, password=PASSWORD)

app.run(debug=True)