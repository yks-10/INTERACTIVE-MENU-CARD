from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .utils import CommonUtils
from .models import Item
from .serializers import ItemSerializer
from validators.Error import Error
# Create your views here.
class HealthView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        @description: This API used to check if server is active or not
        @param request:
        @return: "SUCCESS"
        """
        return CommonUtils.dispatch_success(request, "SUCCESS")


class ItemView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        This method will return the all Items based on the category,
        @param request: Request object
            category
        @return: List Item details of the category
        """
        try:
            data = request.data
            category_name = data.get('name')
            if category_name:
                item = Item.objects.filter(category=category_name).order_by('name')
                serializer = ItemSerializer(item, many=True)
                return CommonUtils.dispatch_success(request, serializer.data)
            else:
                return CommonUtils.dispatch_failure(request, Error.INVALID_PARAMETERS)
        except Exception as e:
            return CommonUtils.dispatch_failure(request, Error.INTERNAL_SERVER_ERROR, str(e))

    def post(self, request):
        """
        This method will add the Items based on the category,
        @param request: Request object
           name  category price
        @return: "SUCCESS"
        """
        try:
            data = request.data
            name = data.get('name')
            category = data.get('category')
            price = data.get('price')
            if name and category:
                try:
                    item_check = Item.objects.get(name=name, category=category)
                    if item_check:
                        return CommonUtils.dispatch_failure(request, Error.ALREADY_EXISTS)
                except Exception as e:
                    item = Item.objects.create(name=name, category=category, price=price)
                    item.save()
                    no = e
                    return CommonUtils.dispatch_success(request, "SUCCESS")
            else:
                return CommonUtils.dispatch_failure(request, Error.INVALID_PARAMETERS)
        except Exception as e:
            return CommonUtils.dispatch_failure(request, Error.INTERNAL_SERVER_ERROR, str(e))

    def put(self, request):
        """
        This method will update the Items based on the category,
        @param request: Request object
           name  category price
        @return: "SUCCESS"
        """
        try:
            data = request.data
            name = data.get('name')
            category = data.get('category')
            name1 = data.get('new_name')
            category1 = data.get('new_category')
            price = data.get('price')
            if name and category:
                item = Item.objects.get(name=name, category=category)
                if name1:
                    item.name = name1
                if category1:
                    item.category = category1
                if price:
                    item.price = price
                item.save()
                return CommonUtils.dispatch_success(request, "SUCCESS")
            else:
                return CommonUtils.dispatch_failure(request, Error.INVALID_PARAMETERS)
        except Item.DoesNotExist as e:
            return CommonUtils.dispatch_failure(request, Error.NO_DATA_FOUND, str(e))
        except Exception as e:
            return CommonUtils.dispatch_failure(request, Error.INTERNAL_SERVER_ERROR, str(e))


