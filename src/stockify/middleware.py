from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from functools import wraps

# Hiérarchie des rôles
ROLE_PRIORITY = {
    'admin': 3,
    'editor': 2,
    'viewer': 1
}

# Pour les vues de fonction
def min_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect('signin')
            user_role = getattr(user, 'role', 'viewer')
            if ROLE_PRIORITY.get(user_role, 0) < ROLE_PRIORITY.get(required_role, 0):
                return redirect('unauthorized')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


#Pour les class-based views (CBV)
class RoleRequiredMixin(LoginRequiredMixin):
    required_role = 'viewer'  # rôle minimum par défaut

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        user_role = getattr(user, 'role', 'viewer')

        if ROLE_PRIORITY.get(user_role, 0) < ROLE_PRIORITY.get(self.required_role, 0):
            return redirect('unauthorized')  # vers la vue non autorisée

        return super().dispatch(request, *args, **kwargs)
