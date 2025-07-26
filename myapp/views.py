# views.py
from django.shortcuts import render
import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyCo28PDVfKE8ONjWqAz5QzE_IudTd3a27U")

def dailyportion(request):
    recommendation = None

    if request.method == "POST":
        item = request.POST.get("item")
        yesterday_qty = request.POST.get("yesterday_qty")
        temperature = request.POST.get("temperature")
        event = request.POST.get("event", "None")

        prompt = f"""
You are a food business AI assistant.

Here is vendor data:
- Item sold: {item}
- Quantity sold yesterday: {yesterday_qty} kg
- Today's temperature: {temperature}°C
- Local event: {event}

Based on this, suggest the optimal quantity to prepare today.
Give a range and explain why.
"""

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        recommendation = response.text

    return render(request, "myapp/dashboard.html", {"recommendation": recommendation})
