import json
from django.http import HttpResponse, JsonResponse
from .models import Shapes
from django.utils import timezone


def index(request):
    return HttpResponse("Hello,You're at the shapes index.")


def addshape(request):
    if request.method == "POST":
        print('request.POST')
        description = request.POST.get("description")
        croptype = request.POST.get("croptype")
        shapesdescrip = request.POST.get('shapesdescrip')
        location = request.POST.get("location")
        uploader = request.POST.get('uploader')
        pic1 = request.FILES.get('image1')
        pic2 = request.FILES.get('image2')
        pic3 = request.FILES.get('image3')
        up = request.POST.get('up')
        down = request.POST.get('down')
        right = request.POST.get('right')
        left = request.POST.get('left')
        ifchecked = request.POST.get('if_checked')
        idafterchecked = request.POST.get('id_after_checked')
        area = request.POST.get('area')
        if description is None or croptype is None or shapesdescrip is None or uploader is None:
            return HttpResponse("UploadFailed")
        try:
            new_item = Shapes()
            new_item.shapesdescrip = shapesdescrip
            new_item.croptype = croptype
            new_item.description = description
            new_item.location = location
            new_item.uploader = uploader
            new_item.pic1 = pic1
            if pic2 is not None:
                new_item.pic2 = pic2
            if pic3 is not None:
                new_item.pic3 = pic3
            new_item.up = up
            new_item.down = down
            new_item.update_time = timezone.now().strftime("%Y-%m-%d")
            new_item.left = left
            new_item.right = right
            new_item.if_checked = ifchecked
            new_item.id_after_checked = idafterchecked
            new_item.area = area
            new_item.save()
        except Exception as e:
            return HttpResponse("Upload fail,Because of" + str(e) + ",Please try it later")
    return HttpResponse("UploadSucessful")


def getshapes(request):
    if request.method == "GET":
        json_dict = {}
        up = float(request.GET.get("up"))
        down = float(request.GET.get("down"))
        right = float(request.GET.get("right"))
        left = float(request.GET.get("left"))
        shapes = Shapes.objects.all()
        numOfShape = 0
        for shape in shapes:
            if (shape.right >= left and shape.left <= right) and (shape.up >= down and shape.down <= up):
                numOfShape += 1
                json_dict["shape" + str(numOfShape)] = shape.shapesdescrip
                json_dict["id" + str(numOfShape)] = shape.id
        json_dict["num"] = numOfShape
        response = JsonResponse(json_dict)
        return response


def getshapelist(request):
    if request.method == "GET":
        sort = request.GET.get("sort")
        detail = request.GET.get('detail')
        page = request.GET.get('page')
        search_list = Shapes.objects.all()
        if sort is not None and detail is not None:
            if len(sort) == 8:
                # if Shapes.objects.filter(croptype=detail):
                search_list = Shapes.objects.filter(croptype=detail)
            if len(sort) == 11:
                search_list = Shapes.objects.filter(update_time=detail)
            if len(sort) == 10:
                search_list = Shapes.objects.filter(if_checked=detail)
            if len(sort) == 16:
                search_list = Shapes.objects.filter(id_after_checked=detail)
            if len(sort) == 2:
                search_list = Shapes.objects.filter(id=detail)
        else:
            pass

        numOfList = len(search_list)
        print('numOfList is ', numOfList)
        if page is not None:
            page = int(page)
            list = search_list.order_by('-update_time')[(page - 1) * 10:page * 10]
        else:
            if len(sort) == 2:
                list = search_list.order_by('update_time')
            else:
                list = search_list.order_by('-update_time')
        total_page = int(numOfList / 10) + 1
        response = {}
        for i in range(0, len(list)):
            response[i] = getItemList(list[i])
        response["total_page"] = total_page
        print('response is:', response)
        response = JsonResponse(response)
        return response


def getallshape(request):
    if request.method == "GET":
        sort = request.GET.get("sort")
        detail = request.GET.get('detail')
        search_list = Shapes.objects.all()
       # numaflist = len(Shapes.objects.all())
        if sort is not None and detail is not None:
            if len(sort) == 8:
                # if Shapes.objects.filter(croptype=detail):
                search_list = Shapes.objects.filter(croptype=detail)
            if len(sort) == 11:
                search_list = Shapes.objects.filter(update_time=detail)
            if len(sort) == 10:
                search_list = Shapes.objects.filter(if_checked=detail)
            if len(sort) == 16:
                search_list = Shapes.objects.filter(id_after_checked=detail)
            if len(sort) == 2:
                search_list = Shapes.objects.filter(id=detail)
        else:
            pass
        numOfList = len(search_list)
        print('numOfList is ', numOfList)
        if len(sort) == 2:
            list = search_list.order_by('update_time')
        else:
            list = search_list.order_by('-update_time')
        total_page = 1
        response = {}
        for i in range(0, len(list)):
            response[i] = getItemList(list[i])
        response["total_page"] = total_page
        print('response is:', response)
        response = JsonResponse(response)
        return response


def getItemList(shape):
    shape_dict = {"description": shape.description,
                  "croptype": shape.croptype,
                  'shapesdescrip': shape.shapesdescrip,
                  "update_time": shape.update_time,
                  'location': shape.location,
                  'uploader': shape.uploader,
                  'up': shape.up,
                  'down': shape.down,
                  'right': shape.right,
                  'left': shape.left,
                  'pic1': str(shape.pic1),
                  'pic2': str(shape.pic2),
                  'pic3': str(shape.pic3),
                  'if_checked': shape.if_checked,
                  'id_after_checked': shape.id_after_checked,
                  'area': shape.area,
                  "id": shape.id,
                  }
    return shape_dict


def getoneshape(request):
    if request.method == "GET":
        i = int(request.GET.get("id"))
        print(i)
        shape = Shapes.objects.get(id=i)
        json_dict = {}
        json_dict["description"] = shape.description
        json_dict["shapesdescrip"] = shape.shapesdescrip
        json_dict["croptype"] = shape.croptype
        json_dict["location"] = shape.location
        json_dict["uploader"] = shape.uploader
        json_dict["update_time"] = shape.update_time
        json_dict["up"] = shape.up
        json_dict["down"] = shape.down
        json_dict["right"] = shape.right
        json_dict["left"] = shape.left
        json_dict["pic1"] = str(shape.pic1)
        json_dict["pic2"] = str(shape.pic2)
        json_dict["pic3"] = str(shape.pic3)
        json_dict["if_checked"] = shape.if_checked
        json_dict["id_after_checked"] = shape.id_after_checked
        json_dict["area"] = shape.area
        print(shape.pic1)
        print(json_dict)
        return JsonResponse(json_dict)
