from django.shortcuts import render

# Create your views here.
data = {
        'email' : 'mltechi@pm.me',
        'phone' : '(847) 306-2012',
        'name' : 'Marshall Livingston',
        'description' : ['Linux Systems Administrator', 'Cyber Security Consultant', 'Software Engineer'],
        'social' : [
            { 'https://twitter.com/tr33lovah' : 'fa fa-twitter' },
            { 'https://www.linkedin.com/in/marshall-livingston-005945137/' : 'fa fa-linkedin' },
            { 'https://www.youtube.com/channel/UCRV2XpTL8K4pVxaVZx4Vq2A/playlists?view_as=subscriber' : 'fa fa-youtube' },
        ],
        'core' : [
            { 'https://ourcloud.us/s/DKgP2sGCiXai2tn' : 'Resume' },
            { 'https://ourcloud.us/s/yS8MKRZmNwmPM6z' : 'Certifications'},
            { 'https://ourcloud.us/s/GgXTB4ZoNz7M8wY' : 'Reading Material' },
            { 'https://kryptsec.com' : 'KryptSec' },
            { 'https://kwiki.kryptsec.com' : 'Kwiki' },
            { 'https://discord.gg/h22KRvU' : 'Discord' },
        ],
    }
def home(request):
    context = data
    return render(request, 'landing/base.html', context)

def pdfs(request):
    context = data
    return render(request, 'landing/pdfs.html', context)
