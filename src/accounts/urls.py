from .views import signin_view, signup_view, logout_user, AccountListView, CreateUserByAdminView, createAdminUser, \
    createEditorUser, deleteUser, createViewerUser
from django.urls import path


urlpatterns = [
    path('', AccountListView.as_view(), name='accounts'),
    path('add', CreateUserByAdminView.as_view(), name='add'),
    path('add-admin/<int:user_id>', createAdminUser, name='add_admin'),
    path('add-moderator/<int:user_id>', createEditorUser, name='add_editor'),
    path('add-viewer/<int:user_id>', createViewerUser, name='add_viewer'),
    path('delete/<int:user_id>', deleteUser, name='delete_user'),
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_user, name='logout'),
]