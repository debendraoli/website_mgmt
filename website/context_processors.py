from .models import SiteInfo


def site_info_processor(request):
    site_info = SiteInfo.objects.get(info='core')
    return {'site_info': site_info}
