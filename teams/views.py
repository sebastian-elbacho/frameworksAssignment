from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    MessageForm,
    ProfileEditForm,
    ProjectForm,
    UserEditForm,
    UserRegistrationForm,
)
from .models import Message, Project, UserProfile


def home(request):
    """
    Home page view.

    Renders the main landing page for the application.
    If the user is authenticated, the template shows shortcuts
    to projects, inbox and profile. Otherwise it shows login/register buttons.
    """
    return render(request, "teams/home.html")


def register(request):
    """
    Register a new user account.

    - On GET: display the registration form.
    - On POST: validate the form, create a new User and related UserProfile.
    - After successful registration: redirect to the login page and
      show a success toast notification.
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create user object but do not save to DB yet
            new_user = form.save(commit=False)
            # Hash the password using Django's secure password hasher
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()

            # Create a related profile object with additional fields
            UserProfile.objects.create(
                user=new_user,
                phone=form.cleaned_data.get("phone", ""),
                address=form.cleaned_data.get("address", ""),
                city=form.cleaned_data.get("city", ""),
            )

            # Show popup notification (Bootstrap toast)
            messages.success(
                request,
                "Account created successfully. You can now log in.",
            )

            # Redirect to login page
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "teams/register.html", {"form": form})


@login_required
def profile(request):
    """
    Display the current user's profile page.

    Shows basic user information such as username, email and
    additional details from the UserProfile model.
    Only accessible to authenticated users.
    """
    return render(request, "teams/profile.html")


@login_required
def edit_profile(request):
    """
    Edit profile details for the currently logged-in user.

    - Uses two forms: one for the built-in User model and
      one for the related UserProfile model.
    - On successful POST, saves changes and redirects back to the profile page.
    """
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.userprofile, data=request.POST
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "teams/edit_profile.html", context)


@login_required
def add_project(request):
    """
    Create a new project.

    - On GET: show an empty ProjectForm.
    - On POST: validate and save a new Project instance,
      automatically assigning the current user as the owner.
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            # Assign currently logged-in user as the project owner
            project.owner = request.user
            project.save()
            messages.success(request, "Project has been created.")
            return redirect("project_list")
    else:
        form = ProjectForm()

    return render(request, "teams/add_project.html", {"form": form})


@login_required
def project_list(request):
    """
    List projects for the current user.

    - If the user has role 'admin' in UserProfile, they can see all projects.
    - Otherwise, they only see projects where they are the owner.
    """
    user_profile = request.user.userprofile

    if user_profile.role == "admin":
        # Admin can see all projects in the system
        projects = Project.objects.all()
    else:
        # Regular user only sees their own projects
        projects = Project.objects.filter(owner=request.user)

    return render(request, "teams/project_list.html", {"projects": projects})


@login_required
def edit_project(request, project_id):
    """
    Edit an existing project.

    Only the owner of the project (or an admin, if desired) should be able
    to edit it. Here we restrict editing to the owner for simplicity.
    """
    project = get_object_or_404(Project, id=project_id, owner=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project has been updated.")
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)

    return render(request, "teams/edit_project.html", {"form": form})


@login_required
def delete_project(request, project_id):
    """
    Delete a project owned by the current user.

    Shows a confirmation page on GET.
    On POST it deletes the project and redirects back to the project list.
    """
    project = get_object_or_404(Project, id=project_id, owner=request.user)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been deleted.")
        return redirect("project_list")

    return render(request, "teams/delete_project.html", {"project": project})


@login_required
def inbox(request):
    """
    Display all messages received by the current user.

    Messages are ordered from the newest to the oldest.
    """
    messages_qs = Message.objects.filter(recipient=request.user).order_by(
        "-timestamp"
    )
    return render(request, "teams/inbox.html", {"messages": messages_qs})


@login_required
def send_message(request):
    """
    Send a new message to another user.

    - On GET: show a MessageForm.
    - On POST: validate and save a new Message,
      automatically setting the sender to the current user.
    """
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message_obj = form.save(commit=False)
            message_obj.sender = request.user
            message_obj.save()
            messages.success(request, "Message has been sent.")
            return redirect("inbox")
    else:
        form = MessageForm()

    return render(request, "teams/send_message.html", {"form": form})
