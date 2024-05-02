from app import app, db

# Create all database tables
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)

