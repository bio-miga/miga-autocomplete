from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse

@csrf_exempt
def matching_species(request, prefix):
    try:
        if request.method == 'GET':
            # This API doesn't use any models or serializers since it doesn't store the data within Django
            filename = 'static/list_of_species.txt'

            file = open(filename, 'r')
            specieslist = file.read().splitlines()
            file.close()
            filtered = [x for x in specieslist if x.startswith(str(prefix).capitalize().replace(" ", "_"))]
            return JsonResponse(filtered, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)