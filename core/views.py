from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactMessage


def base(request):
    return render(request, 'index.html')

def home(request):
    skills = [
        ("Python", 85, "🐍"),
        ("Machine Learning", 85, "🤖"),
        ("Django", 60, "🌿"),
        ("Data analytics", 70, "📈"),
        ("C / C++", 75, "💻"),
        ("VHDL", 65, "🔌"),
        ("HTML", 80, "🌐"),
        ("CSS", 75, "🎨"),
        ("Proteus", 85, "⚙️"),
        ("MATLAB", 75, "📊"),
        ("AutoCAD Fusion 360", 65, "🛠️"),
        ("Circuit Design", 70, "🔋"),
    ]

    projects = [
        {
            "title": "Grocery Store Management System",
            "domain": "Desktop Application / Automation",
            "category": "ai",
            "description": "A complete store management solution built with Tkinter where owners can monitor employee activity, sales, and working hours, while sellers can generate invoices using product scanning just like real retail systems.",
            "image": "/static/images/grocery.png",
            "github": "https://github.com/abdullahee297",
            "demo": "#"
        },

        {
            "title": "PDF Handler Web App",
            "domain": "Django Web Development",
            "category": "web",
            "description": "A powerful web application that allows users to upload PDFs and perform operations like data extraction, merging, watermarking, and encryption in a user-friendly interface.",
            "image": "/static/images/pdf.png",
            "github": "https://github.com/abdullahee297/Django-PyPDF",
            "demo": "https://django-py-pdf.vercel.app/"
        },

        {
            "title": "AI Virtual Mouse",
            "domain": "Computer Vision / AI",
            "category": "ml",
            "description": "An AI-based system using MediaPipe that enables users to control the mouse pointer using hand gestures, specifically tracking the index finger for real-time interaction.",
            "image": "/static/images/mouse.png",
            "github": "https://github.com/abdullahee297/VirtualMouse",
            "demo": "#"
        },

        {
            "title": "AI Virtual Painter",
            "domain": "Computer Vision / AI",
            "category": "ml",
            "description": "A gesture-based drawing system that allows users to draw on screen using hand movements with multiple colors and an eraser feature powered by MediaPipe.",
            "image": "/static/images/paint.png",
            "github": "https://github.com/abdullahee297/AI-Virtual-Painter",
            "demo": "#"
        },

        {
            "title": "Pen Detection System",
            "domain": "Machine Learning / YOLO",
            "category": "ai",
            "description": "A custom-trained object detection model using YOLO and Label Studio to classify different types of pens such as marker, gel, and ink pens from images.",
            "image": "/static/images/pen.jpg",
            "github": "#",
            "demo": "#"
        },

        {
            "title": "Django Chatbot",
            "domain": "AI / NLP",
            "category": "ai",
            "description": "An intelligent chatbot built with Django and Ollama (LLaMA 3) that processes user input and generates contextual responses in real-time.",
            "image": "/static/images/chatbot.png",
            "github": "https://github.com/abdullahee297/Django-ChatBot",
            "demo": "#"
        },

        {
            "title": "Spam Message Detector",
            "domain": "Machine Learning",
            "category": "ml",
            "description": "A machine learning-based system that detects whether a message is spam or not using text classification techniques.",
            "image": "/static/images/spam.png",
            "github": "https://github.com/abdullahee297/ML-SpamMessages",
            "demo": "#"
        },

        {
            "title": "Weather App",
            "domain": "Django / API Integration",
            "category": "web",
            "description": "A weather forecasting web application that fetches real-time weather data using APIs based on user-input city names.",
            "image": "/static/images/weather.png",
            "github": "https://github.com/abdullahee297/WeatherAppDjango",
            "demo": "https://weather-app-django-demi.vercel.app/"
        },

        {
            "title": "QR Code Generator",
            "domain": "Django Web App",
            "category": "web",
            "description": "A simple and efficient tool that generates QR codes instantly from user-provided links for easy sharing and access.",
            "image": "/static/images/qrcode.png",
            "github": "https://github.com/abdullahee297/Django-QRGenerator",
            "demo": "https://django-qr-generator-13be.vercel.app/"
        },

        {
            "title": "Student Portal System",
            "domain": "Database / Desktop App",
            "description": "A student management system using Tkinter and MongoDB that allows storing, updating, and managing student records efficiently. This helps to improe the data handling.",
            "image": "/static/images/portal.png",
            "github": "https://github.com/abdullahee297/dsa-student-portal",
            "demo": "#"
        },

        {
            "title": "Space War Game",
            "domain": "Game Development / Pygame",
            "category": "game",
            "description": "An interactive space shooter game where players control a rocket to destroy incoming obstacles using lasers, featuring scoring, lives, power-ups, and immersive sound effects.",
            "image": "/static/images/game.png",
            "github": "https://github.com/abdullahee297/SpaceWar-Game",
            "demo": "#"
        },

        {
            "title": "AI YouTube Control",
            "domain": "AI / Computer Vision",
            "category": "ai",
            "description": "An AI-powered computer vision system that allows hands-free control of YouTube using hand gestures, enabling play/pause, speed control, and full-screen mode through finger tracking.",
            "image": "/static/images/yt.png",
            "github": "https://github.com/abdullahee297/ytcontrol-ml",
            "demo": "#"
        },

        {
            "title": "GPA Calculator",
            "domain": "Django Web Develoment",
            "category": "web",
            "description": "Easy for the students to calculate there gpa in an easy and quick way.",
            "image": "/static/images/gpa.png",
            "github": "https://github.com/abdullahee297/gpa_calculator",
            "demo": "https://gpa-calculator-sigma-six.vercel.app/"
        },
    ]

    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True

    return render(request, "index.html", {
        "skills": skills,
        "projects": projects,
        "success": success
    })


def about(request):
    return redirect('/#about')

def education(request):
    return redirect('/#education')

def exerience(request):
    return redirect('/#experience')
