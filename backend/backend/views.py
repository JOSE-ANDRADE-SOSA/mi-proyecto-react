from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_test(request):
    if request.method == 'GET':
        return JsonResponse({
            'status': 'success',
            'message': 'Backend Django funcionando correctamente en AWS!'
        })
    return JsonResponse({'status': 'error'}, status=400)