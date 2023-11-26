from django.shortcuts import render

# Create your views here.

# django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# django-rest-framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import random

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def shuffleCards(request):
    letter = ["A", "J", "Q", "K"] + [str(i) for i in range(2, 11)]
    sign = [1, 2, 3, 4]
    card = []
    
    for l in letter:
        for s in sign:
            card.append(
                {
                    "letter": l,
                    "sign": s
                }
            )
    
    random.shuffle(card)

    return Response(
        {
            "status": True,
            "data": card
        }
    )
