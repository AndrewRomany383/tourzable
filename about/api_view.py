from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import About, FAQ
from.serializers import AboutSerializer, FAQSerializer



class AboutData(RetrieveAPIView):
    queryset = About.objects.only('what_we_do', 'our_mission', 'our_goals', 'image')
    serializer_class = AboutSerializer

class FaqData(RetrieveAPIView):
    queryset = FAQ.objects.only('title', 'description')
    serializer_class = FAQSerializer



"""@api_view(['GET'])
def faq(request):
    faq_title = FAQ.objects.only('title', 'description')
    about = About.objects.only('what_we_do', 'our_mission', 'our_goals', 'image')
    faq_data = FAQSerializer(faq, many=True).data
    about_data = AboutSerializer(about, many=True, context={'request':request}).data
    return Response({'faq_request': faq_data[0],
                     'faq_data': faq_data[1],
                     'what_we_do': about_data[0],
                     'our_mission': about_data[1],
                     'our_goals': about_data[2],
                     'image': about_data[2]})"""












































