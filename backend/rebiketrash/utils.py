from optparse import Values
from .models import trash_kind, uploaded_trash_image, challenge, user_challenge

import boto3
from datetime import datetime, timedelta
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

import torch
import os

def get_img_url(request):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    image = request.FILES['filename']
    image_time = (str(datetime.now())).replace(" ", "")
    image_type = (image.content_type).split("/")[1]
    s3_client.upload_fileobj(
        image,
        "image-bucket2",
        image_time+"."+image_type,
        ExtraArgs={
            "ContentType": image.content_type
        }
    )
    image_url = "http://image-bucket2.s3.ap-northeast-2.amazonaws.com/" + \
        image_time+"."+image_type
    image_url = image_url.replace(" ", "/")
    return image_url

def get_ai_result(instance):
    hubconfig = os.path.join(os.getcwd(), 'rebiketrash', 'yolov5')
    weightfile = os.path.join(os.getcwd(), 'rebiketrash', 'yolov5',
                              'runs', 'train', 'garbage_yolov5s_results', 'weights', 'best.pt')
    model = torch.hub.load(hubconfig, 'custom',
                           path=weightfile, source='local')
    results = model(instance)
    results_dict = results.pandas().xyxy[0].to_dict(orient="records")
    if not results_dict:
        return 0
    return results_dict[0].get('name')

def check_challenge(user_id):
    return 0
    #if user_challenge.objects.filter(user_id):