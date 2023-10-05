from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import About, FAQ, ContactUs, ContactConsultant
from.serializers import AboutSerializer, FAQSerializer, ContactUsSerializer, ContactConsultantSerializer



class AboutData(ListAPIView):
    queryset = About.objects.language('en-us').only('id', 'translations')
    serializer_class = AboutSerializer

class AboutDataAr(ListAPIView):
    queryset = About.objects.language('ar-sa').only('id', 'translations')
    serializer_class = AboutSerializer

class FaqData(ListAPIView):
    queryset = FAQ.objects.language('en-us').only('id', 'translations')
    serializer_class = FAQSerializer

class FaqDataAR(ListAPIView):
    queryset = FAQ.objects.language('ar-sa').only('id', 'translations')
    serializer_class = FAQSerializer


class Contactus(CreateAPIView):
    queryset = ContactUs.objects.only('firstname',
                                      'lastname',
                                      'email',
                                      'number_phone',
                                      'place',
                                      'check_in',
                                      'check_out',
                                      'adults_number',
                                      'children_number_and_their_age',
                                      'infant',
                                      'room_number',
                                      'notes')
    serializer_class = ContactUsSerializer


class Contactconsultant(CreateAPIView):
    queryset = ContactConsultant.objects.only('firstname',
                                              'lastname',
                                              'email',
                                              'number_phone',
                                              'place',
                                              'check_in',
                                              'check_out',
                                              'adults_number',
                                              'children_number_and_their_age',
                                              'infant',
                                              'room_number',
                                              'notes')
    serializer_class = ContactConsultantSerializer

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












































