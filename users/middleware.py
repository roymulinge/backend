from django.shortcuts import redirect
from django.urls import reverse

class PhoneNumberRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.phone_number_provided:
           if request.path not in [reverse('phone-number-required'), reverse('account_logout')]:
                return redirect('phone-number-required')
        response = self.get_response(request)
        return response