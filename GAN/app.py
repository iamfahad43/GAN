"""
    Let's start by using a simple GAN model for image generation. For simplicity, we'll use a pre-trained DCGAN model with TensorFlow. 
    We'll then create Flask APIs to interact with this model, allowing students to adjust parameters and see the live training process.
    
"""

# Filename: app.py
from flask import Flask, jsonify, request, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dcgan_model import load_dcgan_model, generate_image
import time

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for GAN parameters
class GANParameters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    learning_rate = db.Column(db.Float, nullable=False, default=0.001)
    batch_size = db.Column(db.Integer, nullable=False, default=64)
    image_path = db.Column(db.String(255), nullable=True, default=None)  # Add this line for the image_path column

# Load the DCGAN model
dcgan_model = load_dcgan_model()

# Initialize the database within the application context
with app.app_context():
    db.create_all()

# Define the Leaderboard model
class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)
    
# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# API to generate an image based on text input
@app.route('/api/generate-image', methods=['GET', 'POST'])
def generate_image_endpoint():
    if request.method == 'GET':
        return jsonify({"message": "Send a POST request with text input to generate an image."})
    elif request.method == 'POST':
        #data = request.json
        with app.app_context():
            try:
                data = request.json
            
                # Generate and return an image based on text input
                text_input = data.get('textInput', 'Default description')
                
                # Generate the image using the dcgan_model
                image_path = generate_image(text_input)
                
                if image_path:
                    # Save the image path to the database
                    parameters = GANParameters.query.first()
                    if parameters is not None:
                        parameters.image_path = image_path
                        db.session.commit()
                        return jsonify({"imagePath": image_path})
                    else:
                        # Create a new GANParameters record
                        new_parameters = GANParameters(image_path=image_path)
                        db.session.add(new_parameters)
                        db.session.commit()
                        return jsonify({"imagePath": image_path})
                else:
                    return jsonify({"message": "Error generating the image."}), 500
            except Exception as e:
                return jsonify({"message": f"Error: {str(e)}"}), 500

# Add a route to download the generated image
@app.route('/api/download-image', methods=['GET'])
def download_image():
    with app.app_context():
        # Retrieve the last generated image path from the database
        parameters = GANParameters.query.first()
        image_path = parameters.image_path

    if image_path:
        return send_file(image_path, as_attachment=True)
    else:
        return jsonify({"message": "No image available for download."}), 404

# Route to show the last generated image on the website
@app.route('/last-generated-image')
def last_generated_image():
    with app.app_context():
        # Retrieve the last generated image path from the database
        parameters = GANParameters.query.first()
        image_path = parameters.image_path

    return render_template('last_generated_image.html', image_path=image_path)

# API to get the current GAN parameters
@app.route('/api/get-parameters', methods=['GET'])
def get_parameters():
    with app.app_context():
        gan_params = GANParameters.query.first()
    return jsonify({"learning_rate": gan_params.learning_rate, "batch_size": gan_params.batch_size})

# API to update GAN parameters
@app.route('/api/update-parameters', methods=['POST'])
def update_parameters():
    data = request.json
    with app.app_context():
        gan_params = GANParameters.query.first()
        gan_params.learning_rate = data.get('learning_rate', gan_params.learning_rate)
        gan_params.batch_size = data.get('batch_size', gan_params.batch_size)
        db.session.commit()
    return jsonify({"message": "GAN parameters updated successfully"})

# API to simulate the live training process
@app.route('/api/train', methods=['GET'])
def train_gan():
    with app.app_context():
        """
        for epoch in range(5):
            progress = (epoch + 1) / 5# Simulate the training process (replace this with actual training logic)
            # Here, we're using a simple sleep to simulate training time
            time.sleep(5)
        return jsonify({"message": "GAN training completed", "progress": 100})
        """
        time.sleep(5)
        # Update the leaderboard (replace this with actual logic based on user progress)
        user = "TestUser"  # Replace with actual user identification
        leaderboard_entry = Leaderboard.query.filter_by(user=user).first()
        if leaderboard_entry:
            leaderboard_entry.points += 10  # Give points for completing training
        else:
            new_entry = Leaderboard(user=user, points=10)
            db.session.add(new_entry)

        db.session.commit()

    return jsonify({"message": "GAN training completed"})

if __name__ == '__main__':
    app.run(debug=True)

