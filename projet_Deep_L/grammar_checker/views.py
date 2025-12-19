from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .utils import correct_text

# Import du moteur qu'on vient de créer
# from .nlp_engine import GECModel

def index_view(request):
    return render(request, 'index.html')


@csrf_exempt
@api_view(['POST'])
def correct_text_view(request):
    text = request.data.get("text", "")

    if text.strip() == "":
        return Response({"message": "Texte vide"}, status=400)

    try:
        correction = correct_text(text)
        return Response({
            "status": "success",
            "original": text,
            "correction": correction,
        })
    except Exception as e:
        return Response({"message": str(e)}, status=500)