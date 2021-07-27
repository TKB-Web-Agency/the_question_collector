from .models import Categories

def sidebar_categories(request):
    return {
            'all_categories': Categories.objects.all()
            }
