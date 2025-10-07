# This is the main library for face detection and face encoding.
# It uses deep learning (built on top of dlib) to:
    # detect faces
    # extract unique numerical features (encodings)
    # compare faces
import face_recognition
import numpy as np
# The Pillow (PIL) library helps open and manipulate images in Python.
from PIL import Image
import io
import base64
import cv2


def encode_face(image_data):
    """
    Encode face from image data (base64 string)
    Returns: face encoding as string or None if no face found
    """
    try:
        # Many base64 strings include a prefix like "data:image/png;base64,...".This removes that prefix if present.
        # Then decodes the remaining base64 string into raw bytes.
        image_data = image_data.split(',')[1] if ',' in image_data else image_data
        image_bytes = base64.b64decode(image_data)
        
        # io.BytesIO(image_bytes) makes a file-like object from bytes.
        # Image.open() reads it as an image.
        # Converts it to a NumPy array (image_np) for OpenCV/face_recognition to process
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        
        # Handles edge cases:
        #     Grayscale image (2D array) → converts to 3-channel RGB.
        #     Image with alpha channel (RGBA) → converts to RGB.
        # Ensures consistent RGB format before face detection.
        if len(image_np.shape) == 2:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB)
        elif image_np.shape[2] == 4:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
        
        # Detects all faces in the image. Returns a list of face bounding boxes (top, right, bottom, left).
        face_locations = face_recognition.face_locations(image_np)
        
        # Rejects if no face or more than one face is detected.
        if len(face_locations) == 0:
            return None, "No face detected in the image"
        
        if len(face_locations) > 1:
            return None, "Multiple faces detected. Please ensure only one face is visible"
        
        # Get face encoding - Extracts the 128-dimensional feature vector that uniquely represents that face.
        face_encodings = face_recognition.face_encodings(image_np, face_locations)
        
        if len(face_encodings) == 0:
            return None, "Could not encode face"
        
        # Converts NumPy array of 128 floats → a comma-separated string, suitable for saving in the database (UserProfile.face_encoding).
        encoding_str = ','.join(map(str, face_encodings[0]))
        
        return encoding_str, None
        
    except Exception as e:
        return None, f"Error processing image: {str(e)}"


def compare_faces(known_encoding_str, unknown_image_data, tolerance=0.6):
    """
    Compare a known face encoding with an unknown face image
    Returns: (match, message)
    """
    try:
        # Decode the known encoding
        known_encoding = np.array([float(x) for x in known_encoding_str.split(',')])
        
        # Get encoding from unknown image
        unknown_encoding_str, error = encode_face(unknown_image_data)
        
        if error:
            return False, error
        
        # Converts new encoding string to NumPy array.
        unknown_encoding = np.array([float(x) for x in unknown_encoding_str.split(',')])
        
        # Compare faces
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=tolerance)
        
        if results[0]:
            # Calculate face distance for confidence
            face_distance = face_recognition.face_distance([known_encoding], unknown_encoding)[0]
            confidence = (1 - face_distance) * 100
            print(f"Face matched with {confidence:.2f}% confidence")
            return True, f"Face matched with {confidence:.2f}% confidence"
        else:
            return False, "Face does not match"
            
    except Exception as e:
        return False, f"Error comparing faces: {str(e)}"


def save_face_image(image_data, file_path):
    """
    Save base64 image to file
    """
    try:
        # Removes metadata header and decodes base64 → raw bytes.
        image_data = image_data.split(',')[1] if ',' in image_data else image_data
        image_bytes = base64.b64decode(image_data)
        
        # Opens file in binary write mode ('wb') and writes image bytes.
        with open(file_path, 'wb') as f:
            f.write(image_bytes)
        
        return True, None
    except Exception as e:
        return False, f"Error saving image: {str(e)}"