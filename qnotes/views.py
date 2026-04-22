############################################################################################################
                                # FOR SENDING LINK PURPOSE ONLY (TO ME ONLY)
############################################################################################################



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# from notes.forms import CreateNoteForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
import random
import secrets
import string
# import hashlib, binascii, os

# Create your views here.


#                                      ###  Hash The Password

def base(request):
    # if 'otp_code' in request.session:
    #     del request.session['otp_code']

    name = 'Mohit'
    context = { 'name': name }
    return render(request, 'notes/base.html', context)



def login_notes(request):
    # if 'otp_code' in request.session:
    #     del request.session['otp_code']


    if not request.user.is_authenticated:

        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email2')
            forgot_password_mail = request.POST.get('fpass_email')

            ## For Login Authentication
            if username is not None and password is not None and email is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                # email = request.POST.get('email')
                # print(username)
                # print(email)

                user = authenticate(username=username, password=password)
                email_user = User.objects.filter(email=username).exists()
                # print(email_user)


                if user is not None:
                    login(request, user)
                    if 'otp_code' in request.session:
                        del request.session['otp_code']

                    ## For System/Server E-mail Response

                    # if request.user.is_authenticated:
                    #     subject = 'Qnotes: Signed-Up Successfully !!'
                    #     message = f'Hello, {user.username}!! A warm welcome to Qnotes, the ultimate Notes-Writing and Managing Platform.\n\n You are safely logged In.\nClick the following link or Copy it in your browser to Login:\nhttps://qnotes23.pythonanywhere.com/authentication/\n\n\nWith Regards,\nQnotes\nCode Notes Inc.'
                    #     sender = settings.EMAIL_HOST_USER
                    #     recipient_list = [ user.email,]
                    #     send_mail(subject, message, sender, recipient_list)

                    return redirect('home')
                elif email_user:
                    euser = User.objects.get(email=username)  ## Output : We get Only Username of the User with Given E-mail.
                    # print(euser)
                    login(request, euser)
                    if 'otp_code' in request.session:
                        del request.session['otp_code']
                    return redirect('home')
                else:
                    messages.info(request, 'Username or Password is not incorrect.')
                    return redirect('login')


            ## For Sign-Up Process
            elif email is not None and username is None and password is None:
                print('vpvpvasoknjksn ----------d   jdj sdjk j')
                username = request.POST.get('username2')
                email = request.POST.get('email2')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')

                if password1 == password2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'User with this Username already exists. Please Sign-Up Again.')
                        return redirect('login')
                        # return render(request, 'notes/login.html')
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, 'This Email ID is already registered. Please Sign-Up Again.')
                        return redirect('login')
                        # return render(request, 'notes/login.html')
                    else:
                        user = User.objects.create_user(username=username, email=email, password=password1)
                        messages.success(request, 'Your account has been successfully created !!');

                        ## For System/Server E-mail Response

                        # if User.objects.filter(username=username, email=email).exists():
                        #     pass    # Email Format

                        return redirect('login')

                else:
                    messages.info(request, 'Sign-Up Pssswords do not match.')
                    return redirect('login')


                # user = User.objects.create_user(username=username, email=email, password)
                # print(username)
                # print(email)
                # print(password1)
                # print(password2)
                # print('in signup')
                return render(request, 'notes/login.html')


            elif forgot_password_mail is not None:
                if User.objects.filter(email=forgot_password_mail).exists():

                    if 'otp_code' in request.session:
                        del request.session['otp_code']

                    messages.info(request, 'Email Found In Database.')
                    secret_suffix = str(random.randint(100000, 999999))               ## Kind Of OTP for the new password of the User
                    secret_prefix = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(6))   ## Secret prefix code for the new password
                    secret_password = secret_prefix + secret_suffix
                    print('\n', secret_prefix)
                    print('\n', secret_suffix)
                    print('\n', secret_password)

                    # def hash_password(password):            ## Function To Hash Password
                    #     """Hash a password for storing."""
                    #     salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
                    #     pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 21600)
                    #     pwdhash = binascii.hexlify(pwdhash)
                    #     return (salt + pwdhash).decode('ascii')

                    # hashed_password = hash_password(secret_password)

                    # user = User.objects.get(email=forgot_password_mail)
                    # user.set_password(secret_password)
                    # user.save()


                    user = User.objects.get(email=forgot_password_mail)

                    #  Passing The OTP as Session
                    request.session['otp_code'] = secret_password

                    #  Sending The OTP in the E-mail
                    subject = 'Qnotes: Password Reset Request !!'
                    message = f'Dear, {user.username}!!\n\nYour One-Time Password(OTP) to reset your account password is:\n\t{secret_password}\n\nYou can change your the password of your account using this link:\n\thttps://qnotes23.pythonanywhere.com/change_user_password/\n\nIf you did not request this password reset, please disregard this email.\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
                    sender = settings.EMAIL_HOST_USER
                    recipient_list = [ user.email,]
                    send_mail(subject, message, sender, recipient_list)

                    messages.info(request, 'The Reset OTP Code has been sent to your Account E-mail.')
                    return redirect('change_password')

                else:
                    messages.info(request, 'Email not Found in our Database.')

                return redirect('login')


        else:
            # return redirect('login')
            return render(request, 'notes/login.html')

    else:
        return redirect('home')



def logout_notes(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')



def change_password(request):

    if request.method == 'POST':

        otp = request.POST.get('scode')
        old_pass = request.POST.get('old_pass')

        # For password change using "Old Password"
        if old_pass is not None and otp is None:
            if request.user.is_authenticated:
                usernm = request.user.username
                temp_user = authenticate(username=usernm, password=old_pass)
                if temp_user is not None:
                    new_pass1 = request.POST.get('new_pass1')
                    new_pass2 = request.POST.get('new_pass2')
                    if (new_pass1 == new_pass2) and new_pass1 is not None and new_pass2 is not None:
                        user = User.objects.get(username=usernm)
                        user.set_password(new_pass1)
                        user.save()

                        new_pass_user = authenticate(username=usernm, password=new_pass1)
                        if new_pass_user is not None:
                            logout(request)     ### New Security Loop Hole Fixed
                            login(request, new_pass_user)

                        messages.info(request, 'Your Password has been changed successfully!!')

                        subject = 'Qnotes: Password Change Alert !!'
                        message = f'Dear, {user.username}!!\n\nThis is to inform you that the password for your account has been successfully changed.\n\nIf you find this password reset suspicious or you did not change the password then quickly reset your password to recover your account.\n\nTo request for a password reset, go to this link:\n\n\thttps://qnotes23.pythonanywhere.com/authentication/\n\nAnd then click on "Forgot Password?" at the bottom.\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
                        sender = settings.EMAIL_HOST_USER
                        recipient_list = [ user.email,]
                        send_mail(subject, message, sender, recipient_list)

                        return redirect('home')
                    else:
                        messages.info(request, 'New Passwords do not match.')
                    # return redirect('change_password')
                else:
                    messages.info(request, 'Please check and re-enter your old password.')
                # return redirect('change_password')
            else:
                messages.info(request, 'You need to login first to change the password here!!')
                # return render(request, 'notes/change_password.html')
            # return redirect('change_password')


        # For password change using "E-mail Reset"
        elif otp is not None and old_pass is None:
            if not request.user.is_authenticated:
                userem = request.POST.get('oemail')
                if User.objects.filter(email=userem).exists():
                    session_otp = request.session['otp_code']
                    if otp == session_otp:
                        new_otp_pass1 = request.POST.get('otp_pass1')
                        new_otp_pass2 = request.POST.get('otp_pass2')
                        if new_otp_pass1 == new_otp_pass2:
                            user = User.objects.get(email=userem)
                            user.set_password(new_otp_pass1)
                            user.save()

                            if 'otp_code' in request.session:
                                del request.session['otp_code']

                            # new_otp_user = authenticate(username=request.user.username, password=new_otp_pass1)
                            # if new_otp_user is not None:
                            #     login(request, new_otp_user)
                            #     logout(request)     ### New Security Loop Hole Fixed
                            #     login(request, new_otp_user)

                            messages.info(request, 'Your Password has been successfully changed!!')
                            subject = 'Qnotes: Password Reset Successful !!'
                            message = f'Dear, {user.username}!!\n\nYour request for the password change has been processed and approved. Your Password is now safely changed.\n\nYou can now login to Qnotes using the New Password created by you.\nTo Login with new credentials, refer to this link:\n\thttps://qnotes23.pythonanywhere.com/authentication/\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
                            sender = settings.EMAIL_HOST_USER
                            recipient_list = [ user.email,]
                            send_mail(subject, message, sender, recipient_list)

                            return redirect('login')
                        else:
                            messages.info(request, 'New Passwords do not match.')
                    else:
                        messages.info(request, 'Entered OTP is not correct. Please Check.')
                else:
                    messages.info(request, 'Please enter your correct E-mail ID.')
            else:
                messages.info(request, 'You are already logged in. Please click on your Account Settings >> Change Password. ')

            # return redirect('change_password')

        return redirect('change_password')
        # return redirect('login')

    else:
        # return redirect('change_password')
        return render(request, 'notes/change_password.html')

        # return redirect('change_password')


    # return render(request, 'notes/change_password.html')





def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            if request.POST.get('mycLink'):
                mycLink = request.POST.get('mycLink')

                subject = 'Qnotes Linker Notification: Link Sent Successfully !!'
                message = f'Hey Pal,\n\n\nThis Link has been sent to you by {request.user.username}.\n\nThe link is given below:\n\n\t{mycLink}\n\nIt is always advised to kindly check the sender of this link so that you can decide whether this link can be trusted or not.\n\nWith Regards,\nQnotes Linker Team\nCode Notes Inc.\n\n'
                sender = settings.EMAIL_HOST_USER
                recipient_list = [ request.user.email,]
                send_mail(subject, message, sender, recipient_list)
                messages.info(request, 'Link Has Been Sent Successfully !!')
                return redirect('home')

        # context = {  }
        return render(request, 'notes/home.html')
    else:
        return redirect('login')


# def create_note(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = CreateNoteForm(request.POST, request.FILES)
#             if form.is_valid():
#                 note_obj = form.save(commit=False)
#                 note_obj.user = request.user
#                 note_obj.save()
#         else:
#             form = CreateNoteForm()

#         context = { 'form': form }
#         return render(request, 'notes/home.html', context)
#     else:
#         return redirect('login')










































############################################################################################################
                                    # ORIGINAL VIEW (INITIAL) #
############################################################################################################




# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# # from notes.forms import CreateNoteForm
# from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from django.conf import settings
# import random
# import secrets
# import string
# import hashlib, binascii, os

# # Create your views here.


# #                                      ###  Hash The Password

# def base(request):
#     # if 'otp_code' in request.session:
#     #     del request.session['otp_code']

#     name = 'Mohit'
#     context = { 'name': name }
#     return render(request, 'notes/base.html', context)



# def login_notes(request):
#     # if 'otp_code' in request.session:
#     #     del request.session['otp_code']


#     if not request.user.is_authenticated:

#         if request.method == 'POST':

#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             email = request.POST.get('email2')
#             forgot_password_mail = request.POST.get('fpass_email')

#             ## For Login Authentication
#             if username is not None and password is not None and email is None:
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 # email = request.POST.get('email')
#                 # print(username)
#                 # print(email)

#                 user = authenticate(username=username, password=password)
#                 email_user = User.objects.filter(email=username).exists()
#                 # print(email_user)


#                 if user is not None:
#                     login(request, user)
#                     if 'otp_code' in request.session:
#                         del request.session['otp_code']

#                     ## For System/Server E-mail Response

#                     # if request.user.is_authenticated:
#                     #     subject = 'Qnotes: Signed-Up Successfully !!'
#                     #     message = f'Hello, {user.username}!! A warm welcome to Qnotes, the ultimate Notes-Writing and Managing Platform.\n\n You are safely logged In.\nClick the following link or Copy it in your browser to Login:\nhttps://qnotes23.pythonanywhere.com/authentication/\n\n\nWith Regards,\nQnotes\nCode Notes Inc.'
#                     #     sender = settings.EMAIL_HOST_USER
#                     #     recipient_list = [ user.email,]
#                     #     send_mail(subject, message, sender, recipient_list)

#                     return redirect('home')
#                 elif email_user:
#                     euser = User.objects.get(email=username)  ## Output : We get Only Username of the User with Given E-mail.
#                     # print(euser)
#                     login(request, euser)
#                     if 'otp_code' in request.session:
#                         del request.session['otp_code']
#                     return redirect('home')
#                 else:
#                     messages.info(request, 'Username or Password is not incorrect.')
#                     return redirect('login')


#             ## For Sign-Up Process
#             elif email is not None and username is None and password is None:
#                 print('vpvpvasoknjksn ----------d   jdj sdjk j')
#                 username = request.POST.get('username2')
#                 email = request.POST.get('email2')
#                 password1 = request.POST.get('password1')
#                 password2 = request.POST.get('password2')

#                 if password1 == password2:
#                     if User.objects.filter(username=username).exists():
#                         messages.info(request, 'User with this Username already exists. Please Sign-Up Again.')
#                         return redirect('login')
#                         # return render(request, 'notes/login.html')
#                     elif User.objects.filter(email=email).exists():
#                         messages.info(request, 'This Email ID is already registered. Please Sign-Up Again.')
#                         return redirect('login')
#                         # return render(request, 'notes/login.html')
#                     else:
#                         user = User.objects.create_user(username=username, email=email, password=password1)

#                         ## For System/Server E-mail Response

#                         # if User.objects.filter(username=username, email=email).exists():
#                         #     pass    # Email Format

#                         return redirect('login')

#                 else:
#                     messages.info(request, 'Sign-Up Pssswords do not match.')
#                     return redirect('login')


#                 # user = User.objects.create_user(username=username, email=email, password)
#                 # print(username)
#                 # print(email)
#                 # print(password1)
#                 # print(password2)
#                 # print('in signup')
#                 return render(request, 'notes/login.html')


#             elif forgot_password_mail is not None:
#                 if User.objects.filter(email=forgot_password_mail).exists():

#                     if 'otp_code' in request.session:
#                         del request.session['otp_code']

#                     messages.info(request, 'Email Found In Database.')
#                     secret_suffix = str(random.randint(100000, 999999))               ## Kind Of OTP for the new password of the User
#                     secret_prefix = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(6))   ## Secret prefix code for the new password
#                     secret_password = secret_prefix + secret_suffix
#                     print('\n', secret_prefix)
#                     print('\n', secret_suffix)
#                     print('\n', secret_password)

#                     # def hash_password(password):            ## Function To Hash Password
#                     #     """Hash a password for storing."""
#                     #     salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
#                     #     pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 21600)
#                     #     pwdhash = binascii.hexlify(pwdhash)
#                     #     return (salt + pwdhash).decode('ascii')

#                     # hashed_password = hash_password(secret_password)

#                     # user = User.objects.get(email=forgot_password_mail)
#                     # user.set_password(secret_password)
#                     # user.save()


#                     user = User.objects.get(email=forgot_password_mail)

#                     #  Passing The OTP as Session
#                     request.session['otp_code'] = secret_password

#                     #  Sending The OTP in the E-mail
#                     subject = 'Qnotes: Password Reset Request !!'
#                     message = f'Dear, {user.username}!!\n\nYour One-Time Password(OTP) to reset your account password is:\n\t{secret_password}\n\nYou can change your the password of your account using this link:\n\thttps://qnotes23.pythonanywhere.com/change_user_password/\n\nIf you did not request this password reset, please disregard this email.\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
#                     sender = settings.EMAIL_HOST_USER
#                     recipient_list = [ user.email,]
#                     send_mail(subject, message, sender, recipient_list)

#                     messages.info(request, 'The Reset Code has been sent to your Account E-mail.')
#                     return redirect('change_password')

#                 else:
#                     messages.info(request, 'Email not Found in our Database.')

#                 return redirect('login')


#         else:
#             # return redirect('login')
#             return render(request, 'notes/login.html')

#     else:
#         return redirect('home')



# def logout_notes(request):
#     if request.user.is_authenticated:
#         logout(request)
#     return redirect('login')



# def change_password(request):

#     if request.method == 'POST':

#         otp = request.POST.get('scode')
#         old_pass = request.POST.get('old_pass')

#         if old_pass is not None and otp is None:
#             if request.user.is_authenticated:
#                 usernm = request.user.username
#                 temp_user = authenticate(username=usernm, password=old_pass)
#                 if temp_user is not None:
#                     new_pass1 = request.POST.get('new_pass1')
#                     new_pass2 = request.POST.get('new_pass2')
#                     if (new_pass1 == new_pass2) and new_pass1 is not None and new_pass2 is not None:
#                         user = User.objects.get(username=usernm)
#                         user.set_password(new_pass1)
#                         user.save()

#                         new_pass_user = authenticate(username=usernm, password=new_pass1)
#                         if new_pass_user is not None:
#                             login(request, new_pass_user)

#                         messages.info(request, 'Your Password has been changed successfully!!')

#                         subject = 'Qnotes: Password Reset Alert !!'
#                         message = f'Dear, {user.username}!!\n\nThis is to inform you that the password for your account has been successfully changed.\n\nIf you find this password reset suspicious or you did not change the password then quickly reset your password to recover your account.\n\nTo request for a password reset, go to this link:\n\n\thttps://qnotes23.pythonanywhere.com/authentication/\n\nAnd then click on "Forgot Password?" at the bottom.\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
#                         sender = settings.EMAIL_HOST_USER
#                         recipient_list = [ user.email,]
#                         send_mail(subject, message, sender, recipient_list)

#                         return redirect('home')
#                     else:
#                         messages.info(request, 'New Passwords do not match.')
#                     # return redirect('change_password')
#                 else:
#                     messages.info(request, 'Please check or re-enter your old password.')
#                 # return redirect('change_password')
#             else:
#                 messages.info(request, 'You need to login first to change the password here!!')
#                 # return render(request, 'notes/change_password.html')
#             # return redirect('change_password')

#         elif otp is not None and old_pass is None:
#             if not request.user.is_authenticated:
#                 userem = request.POST.get('oemail')
#                 if User.objects.filter(email=userem).exists():
#                     session_otp = request.session['otp_code']
#                     if otp == session_otp:
#                         new_otp_pass1 = request.POST.get('otp_pass1')
#                         new_otp_pass2 = request.POST.get('otp_pass2')
#                         if new_otp_pass1 == new_otp_pass2:
#                             user = User.objects.get(email=userem)
#                             user.set_password(new_otp_pass1)
#                             user.save()

#                             if 'otp_code' in request.session:
#                                 del request.session['otp_code']

#                             messages.info(request, 'Your Password has been successfully changed!!')
#                             subject = 'Qnotes: Password Reset Successful !!'
#                             message = f'Dear, {user.username}!!\n\nYour request for the password change has been processed and approved. Your Password is now safely changed.\n\nYou can now login to Qnotes\2122 using the New Password created by you.\nTo Login with new credentials, refer to this link:\n\thttps://qnotes23.pythonanywhere.com/authentication/\n\n\nWith Regards,\nQnotes Team\nCode Notes Inc.\n\n'
#                             sender = settings.EMAIL_HOST_USER
#                             recipient_list = [ user.email,]
#                             send_mail(subject, message, sender, recipient_list)

#                             return redirect('login')
#                         else:
#                             messages.info(request, 'New Passwords do not match.')
#                     else:
#                         messages.info(request, 'Entered OTP is not correct. Please Check.')
#                 else:
#                     messages.info(request, 'Please enter your correct E-mail ID.')
#             else:
#                 messages.info(request, 'You are already logged in. Please click on your Account Settings >> Change Password. ')

#             # return redirect('change_password')

#         return redirect('change_password')

#     else:
#         # return redirect('change_password')
#         return render(request, 'notes/change_password.html')

#         # return redirect('change_password')


#     # return render(request, 'notes/change_password.html')





# def home(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':

#             if request.POST.get('mycLink'):
#                 mycLink = request.POST.get('mycLink')

#                 subject = 'Qnotes Linker Notification: Link Sent Successfully !!'
#                 message = f'Hey Pal,\n\n\nThis Link has been sent to you by {request.user.username}.\n\nThe link is given below:\n\n\t{mycLink}\n\nIt is always advised to kindly check the sender of this link so that you can decide whether this link can be trusted or not.\n\nWith Regards,\nQnotes Linker Team\nCode Notes Inc.\n\n'
#                 sender = settings.EMAIL_HOST_USER
#                 recipient_list = [ request.user.email,]
#                 send_mail(subject, message, sender, recipient_list)
#                 messages.info(request, 'Link Has Been Sent Successfully !!')
#                 return redirect('home')

#         # context = {  }
#         return render(request, 'notes/home.html')
#     else:
#         return redirect('login')


# # def create_note(request):
# #     if request.user.is_authenticated:
# #         if request.method == 'POST':
# #             form = CreateNoteForm(request.POST, request.FILES)
# #             if form.is_valid():
# #                 note_obj = form.save(commit=False)
# #                 note_obj.user = request.user
# #                 note_obj.save()
# #         else:
# #             form = CreateNoteForm()

# #         context = { 'form': form }
# #         return render(request, 'notes/home.html', context)
# #     else:
# #         return redirect('login')

