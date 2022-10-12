from django.urls import path

from .views import SignUpView, UpdateProfileView, UserEditView, PasswordChangeView, ProfileView, LibrosSubidosView, LibrosFavoritosView, DatosProfileView, Contact


from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path("profile/", ProfileView, name="profile"),
    path("password/", PasswordChangeView.as_view(), name="recover"),
    path("libros_subidos/", LibrosSubidosView, name="libros_subidos"),
    path("libros_favoritos/", LibrosFavoritosView, name="libros_favoritos"),
    path("profile_data/", DatosProfileView.as_view(), name="profile_data"),
    path("contact/<int:pk>", Contact, name="contact"),
    path("profile_data/<int:pk>", UpdateProfileView.as_view(),
         name="edit_profile_data"),





]
