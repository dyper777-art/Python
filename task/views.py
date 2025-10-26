import os
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
import resend

User = get_user_model()

def activate_user(request, uid, token):
    try:
        uid_decoded = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=uid_decoded)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        return JsonResponse({'detail': 'Invalid activation link'}, status=400)

    if default_token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()

            # Get current host from environment
            current_host = os.environ.get("CURRENT_HOST")
            activation_url = f"{current_host}/api/verify-email/{uid}/{token}/"

            # Set Resend API key from environment
            resend.api_key = os.environ.get("RESEND_API_KEY")

            # Send activation email via Resend
            try:
                email_params = {
                    "from": "Acme <onboarding@resend.dev>",  # Use a verified domain or test domain
                    "to": "dyper777@gmail.com",
                    "subject": "Activate Your Account",
                    "html": (
                        f"<p>Hello {user.username},</p>"
                        f"<p>Your account has been activated successfully!</p>"
                        f"<p>You can verify your email or log in here:</p>"
                        f"<p><a href='{activation_url}'>{activation_url}</a></p>"
                        f"<p>If you didn’t request this, ignore this email.</p>"
                    ),
                }
                sent_email = resend.Emails.send(email_params)
                email_id = sent_email["id"]
            except Exception as e:
                return JsonResponse({'detail': f'Account activated but failed to send email: {e}'}, status=500)

            return JsonResponse({
                'detail': f'{user.username} account has been activated successfully.',
                'activation_url': activation_url,
                'email_id': email_id
            }, status=200)

        else:
            return JsonResponse({'detail': 'Account already activated.'}, status=200)

    else:
        return JsonResponse({'detail': 'Activation link is invalid or expired.'}, status=400)
