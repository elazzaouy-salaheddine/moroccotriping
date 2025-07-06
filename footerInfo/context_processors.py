from .models import FooterAboutInfo,SocialLinks,FooterLinks


def footer_data(request):
    return {
        'footer_info':FooterAboutInfo.objects.first(),
        'FooterLinks': FooterLinks.objects.all(),
        'social_links':SocialLinks.objects.all(),
    }