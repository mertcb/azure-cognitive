from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
# face api
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
#python related
from array import array
import os
from PIL import Image
import sys
import time

subscription_key = ""
endpoint = ""

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))
remote_image_url = "https://i.hizliresim.com/jeR4GW.jpg"

#### IMAGE DESCRIPTION ####

print("===== IMAGE DESCRIPTION =====")

description = computervision_client.describe_image(remote_image_url, 2)

print("Description of remote image: ")
if (len(description.captions) == 0):
    print("No description detected.")
else:
    for caption in description.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
#### IMAGE DESCRIPTION ####


#### BRAND DETECTION ####

print("===== BRAND DETECTION =====")

brand_image_url = "https://c.static-nike.com/a/images/w_1920,c_limit/mdbgldn6yg1gg88jomci/image.jpg"
brand_image_features = ["brands"]

brands = computervision_client.analyze_image(brand_image_url, brand_image_features)
print("Brands detected in remote image: ")
if (len(brands.brands) == 0):
    print("No brands detected.")
else:
    for brand in brands.brands:
        print("'{}' with confidence {:.2f}%".format(brand.name, brand.confidence * 100))
#### BRAND DETECTION ####

#### OCR ####

print("===== TEST OCR =====")

remote_image_handwritten_text_url = "https://i.hizliresim.com/LWaNkZ.png"

recognize_handw_results = computervision_client.read(remote_image_handwritten_text_url,  raw=True)

operation_location_remote = recognize_handw_results.headers["Operation-Location"]
operation_id = operation_location_remote.split("/")[-1]

while True:
    get_handw_text_results = computervision_client.get_read_result(operation_id)
    if get_handw_text_results.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line

# actual text 
# We used two 4:1 multiplexers here and 
# gave x-y as select inputs and like on the 
# truth table we did on implementation for 
# sum and c-out multiplexers 

if get_handw_text_results.status == OperationStatusCodes.succeeded:
    for text_result in get_handw_text_results.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()

#### OCR ####

#### FACE DETECTION ####

print("===== Detect Faces - remote =====")
# Get an image with faces
face_url = "https://i.hizliresim.com/Yg9Nb7.jpg"
# Select the visual feature(s) you want.
face_image_features = ["faces"]
# Call the API with remote URL and features
detect_faces_results_remote = computervision_client.analyze_image(face_url, face_image_features)

# Print the results with gender, age, and bounding box
print("Faces in the remote image: ")
if (len(detect_faces_results_remote.faces) == 0):
    print("No faces detected.")
else:
    for face in detect_faces_results_remote.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))




