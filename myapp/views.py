import json
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

@api_view(['GET'])
def ping(request):
    return Response({"status": "Django server is running!"})

@api_view(['POST'])
def generate_ai_report(request):
    try:
        data = request.data
        spending_trend = data.get('spending_trend', [])
        categories = data.get('categories', [])
        suppliers = data.get('suppliers', [])
        savings = data.get('savings', [])

        prompt = f"""
        Analyze this vendor data:
        Spending Trend: {spending_trend}
        Categories: {categories}
        Suppliers: {suppliers}
        Savings: {savings}
        Provide 5 actionable insights to optimize cost, improve supplier selection, and maximize profit.
        """

        # Call Gemini
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return Response({"recommendations": response.text.split("\n")})

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
