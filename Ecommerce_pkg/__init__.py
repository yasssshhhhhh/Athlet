from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
# import os
# from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0a3fa894671a909542fe5526ab60874'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(current_app.root_path, 'static/images/Products')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from Ecommerce_pkg import routes
# from Ecommerce_pkg.routes import UPLOAD_FOLDER
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER