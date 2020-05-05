import os

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@csrf_exempt
def matching_species(request):
    try:
        if request.method == 'GET':
            if 'search' in request.GET:
                query = request.GET['search']
                test = lambda x: x.startswith(str(query).capitalize().replace(" ", "_"))
            elif 'exact' in request.GET:
                query = request.GET['exact']
                test = lambda x: x == str(query).capitalize().replace(" ", "_")
            # This API doesn't use any models or serializers since it doesn't store the data within Django
            filename = os.path.join(BASE_DIR, 'static', 'list_of_species.txt')

            file = open(filename, 'r')
            specieslist = file.read().splitlines()
            file.close()
            filtered = [x for x in specieslist if test(x)]
            if 'exact' in request.GET and len(filtered) == 0:
                return JsonResponse({
                    "detail": "No matching value was found for " + query
                }, status=404)
            return JsonResponse({
                "search": query,
                "results": [{"value": f, "text": f} for f in filtered[:10]]
            }, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
