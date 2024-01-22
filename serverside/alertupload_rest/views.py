from alertupload_rest. serializers import UploadAlertSerializer 
from rest_framework. response import Response 
from rest_framework.decorators import api_view 
from django.http import JsonResponse
@api_view( ['POST'])
def post_alert (request):
    serializer=UploadAlertSerializer(data=request. data) 
    if serializer. is_valid():
        serializer.save()
    else:
        return JsonResponse({'error': 'Unable to process data!'}, status=400)
    return Response(request.META. get ('HTTP_AUTHORIZATION'))