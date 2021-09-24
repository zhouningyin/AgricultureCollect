from django.http import HttpResponse
def getPhoto(request,image_name):
    with open("photos/"+image_name,'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpg")


