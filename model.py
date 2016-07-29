"""Models and database functions for Hot Uploader."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class File(db.Model):
    """Files to be uploaded by users."""

    __tablename__ = "Files"

    file_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    file_URL = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed, for human readability."""

    return "<File file_id=%s fileURL=%s>" % (self.file_id, self.fileURL)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///files'
    db.app = app
    db.init_app(app)



if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
