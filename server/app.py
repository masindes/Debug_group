

from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 
migrate = Migrate(app, db)



   
    
    if __name__ == '__main__':
        app.run(debug=True, port=5555)
    