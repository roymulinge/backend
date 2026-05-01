
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import PhoneNumberForm
from rest_framework import generics, permissions
from .serializers import UserProfileSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@login_required
def phone_number_required_view(request):
    if request.user.phone_number_provided:
        return redirect('/')
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.phone_number_provided = True
            user.save()
            return redirect('/')
    else:
        form = PhoneNumberForm(instance=request.user)
    return render(request, 'users/phone_number_form.html', {'form': form})