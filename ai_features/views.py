from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os
import google.generativeai as genai

# Load and configure the API key once at startup
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
else:
    raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

def generate_response(prompt):
    """Helper function to handle API requests and error handling."""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text if response else "No response generated."
    except Exception as e:
        return str(e)

@require_GET
def view_sales_history(request):
    prompt = "Generate a detailed summary for the recent sales history including key trends and product highlights."
    summary = generate_response(prompt)
    return JsonResponse({"summary": summary})

@require_GET
def view_open_sales(request):
    prompt = "Generate a report for all open sales transactions, including customer and item details."
    report = generate_response(prompt)
    return JsonResponse({"report": report})

@require_GET
def cash_in_out(request):
    prompt = "Provide an analysis of today's cash-in and cash-out transactions with any discrepancies highlighted."
    analysis = generate_response(prompt)
    return JsonResponse({"analysis": analysis})

@require_GET
def end_of_day(request):
    prompt = "Create a summary of the day's performance, highlighting the best-selling products and key metrics."
    summary = generate_response(prompt)
    return JsonResponse({"summary": summary})

@require_GET
def feedback_analysis(request):
    prompt = "Analyze the collected feedback and generate key insights and recommendations for improving service."
    insights = generate_response(prompt)
    return JsonResponse({"insights": insights})
