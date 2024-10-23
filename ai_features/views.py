from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os
import google.generativeai as genai

# Load the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@require_GET
def view_sales_history(request):
    prompt = "Generate a detailed summary for the recent sales history including key trends and product highlights."
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return JsonResponse({"summary": response.text})

@require_GET
def view_open_sales(request):
    prompt = "Generate a report for all open sales transactions, including customer and item details."
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return JsonResponse({"report": response.text})

@require_GET
def cash_in_out(request):
    prompt = "Provide an analysis of today's cash-in and cash-out transactions with any discrepancies highlighted."
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return JsonResponse({"analysis": response.text})

@require_GET
def end_of_day(request):
    prompt = "Create a summary of the day's performance, highlighting the best-selling products and key metrics."
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return JsonResponse({"summary": response.text})

@require_GET
def feedback_analysis(request):
    prompt = "Analyze the collected feedback and generate key insights and recommendations for improving service."
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return JsonResponse({"insights": response.text})

