from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import os
from django.conf import settings

from .forms import UserRegistrationForm, FaceLoginForm
from .models import UserProfile
from .face_utils import encode_face, compare_faces, save_face_image


def register(request):
    """Handle user registration with face capture"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        face_data = request.POST.get('face_image')
        
        if form.is_valid():
            if not face_data:
                messages.error(request, 'Please capture your face image')
                return render(request, 'accounts/register.html', {'form': form})
            
            # Encode face
            encoding, error = encode_face(face_data)
            
            if error:
                messages.error(request, error)
                return render(request, 'accounts/register.html', {'form': form})
            
            # Save user
            user = form.save()
            
            # Save face image and encoding
            profile = user.profile
            
            # Create media directory if not exists
            face_dir = os.path.join(settings.MEDIA_ROOT, 'face_images')
            os.makedirs(face_dir, exist_ok=True)
            
            # Save face image
            image_filename = f"{user.username}_face.jpg"
            image_path = os.path.join(face_dir, image_filename)
            success, error = save_face_image(face_data, image_path)
            
            if success:
                profile.face_image = f"face_images/{image_filename}"
                profile.face_encoding = encoding
                profile.save()
                
                messages.success(request, 'Registration successful! Please login with your face.')
                return redirect('accounts:login')
            else:
                user.delete()
                messages.error(request, f'Failed to save face image: {error}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """Handle face-based login"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    
    if request.method == 'POST':
        form = FaceLoginForm(request.POST)
        face_data = request.POST.get('face_image')
        
        if form.is_valid():
            username = form.cleaned_data['username']
            
            if not face_data:
                messages.error(request, 'Please capture your face for accounts')
                return render(request, 'accounts/login.html', {'form': form})
            
            try:
                user = User.objects.get(username=username)
                profile = user.profile
                
                if not profile.face_encoding:
                    messages.error(request, 'No face data found for this user')
                    return render(request, 'accounts/login.html', {'form': form})
                
                # Compare faces
                match, message = compare_faces(profile.face_encoding, face_data)
                
                if match:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name}!')
                    return redirect('accounts:profile')
                else:
                    messages.error(request, f'accounts failed: {message}')
            
            except User.DoesNotExist:
                messages.error(request, 'User not found')
        else:
            messages.error(request, 'Please enter your username')
    else:
        form = FaceLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    """Display user profile"""
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })


@login_required
def user_logout(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('accounts:login')


def home(request):
    """Home page - redirect to login or profile"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    return redirect('accounts:login')