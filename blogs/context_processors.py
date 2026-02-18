from .models import Category
from assignments.models import SocialLink


def get_categories(request):
    categorise = Category.objects.all()
    return dict (categorise=categorise)


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)