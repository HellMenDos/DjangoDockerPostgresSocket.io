from django.contrib import admin
from .models import Applications, Messages, Review, Typeof, Location, Commucate, Proposal
from django.db.models.functions import TruncDay
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import Coalesce
from django.db.models import F
from django.db.models import Value as V
from .serializers import ApplicationsSerializer
admin.site.site_header = '3R_GROUP_ADMINPANEL'


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'company', 'status',
                    'active', 'weight', 'location', 'date')
    list_filter = ('active', 'company', 'date', 'status')
    filter_horizontal = ('typeOf',)
    search_fields = ("title__startswith", )

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        types = Typeof.objects.values()
        names = []
        data = []
        color = []
        secondbar = []
        typesId = []
        for i in range(len(types)):
            count = Applications.objects.filter(
                typeOf__id=types[i]['id']).count()
            names.append(types[i]['title'])
            color.append(types[i]['color'])
            typesId.append(types[i]['id'])

            if request.GET.get('active__exact', ''):
                if request.GET.get('company__id__exact', ''):
                    if request.GET.get('date__gte', ''):
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F("weight")).filter(active=request.GET.get('active__exact', '')).filter(
                            company=request.GET.get('company__id__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')]).filter(typeOf__id=types[i]['id'])
                    else:
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F("weight")).filter(active=request.GET.get(
                            'active__exact', '')).filter(company=request.GET.get('company__id__exact', '')).filter(typeOf__id=types[i]['id'])
                else:
                    if request.GET.get('date__gte', ''):
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F("weight")).filter(active=request.GET.get(
                            'active__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')]).filter(typeOf__id=types[i]['id'])
                    else:
                        applsec = Applications.objects.annotate(x=F("date")).values("x").annotate(y=F("weight")).filter(
                            active=request.GET.get('active__exact', '')).filter(typeOf__id=types[i]['id'])
            else:
                if request.GET.get('company__id__exact', ''):
                    if request.GET.get('date__gte', ''):
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F("weight")).filter(company=request.GET.get(
                            'company__id__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')]).filter(typeOf=types[i]['id'])
                    else:
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F(
                            "weight")).filter(company=request.GET.get('company__id__exact', '')).filter(typeOf=types[i]['id'])
                else:
                    if request.GET.get('date__gte', ''):
                        applsec = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=F("weight")).filter(
                            date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')]).filter(typeOf=types[i]['id'])
                    else:
                        applsec = Applications.objects.annotate(x=F("date")).values(
                            "x").annotate(y=F("weight")).filter(typeOf__id=types[i]['id'])

            dataBar = (
                applsec
            )
            data.append(applsec.count())
            jsondata = json.dumps(list(dataBar), cls=DjangoJSONEncoder)
            secondbar.append(jsondata)

        if request.GET.get('active__exact', ''):
            if request.GET.get('company__id__exact', ''):
                if request.GET.get('date__gte', ''):
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=Count("id")).filter(active=request.GET.get('active__exact', '')).filter(
                        company=request.GET.get('company__id__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')])
                else:
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=Count("id")).filter(
                        active=request.GET.get('active__exact', '')).filter(company=request.GET.get('company__id__exact', ''))
            else:
                if request.GET.get('date__gte', ''):
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=Count("id")).filter(active=request.GET.get(
                        'active__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')])
                else:
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(
                        y=Count("id")).filter(active=request.GET.get('active__exact', ''))
        else:
            if request.GET.get('company__id__exact', ''):
                if request.GET.get('date__gte', ''):
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=Count("id")).filter(company=request.GET.get(
                        'company__id__exact', '')).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')])
                else:
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(
                        y=Count("id")).filter(company=request.GET.get('company__id__exact', ''))
            else:
                if request.GET.get('date__gte', ''):
                    appl = Applications.objects.annotate(x=TruncDay("date")).values("x").annotate(y=Count(
                        "id")).filter(date__range=[request.GET.get('date__gte', ''), request.GET.get('date__lt', '')])
                else:
                    appl = Applications.objects.annotate(x=TruncDay(
                        "date")).values("x").annotate(y=Count("id"))

        chart_data = (appl)

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = {"time_data": as_json, "data": data,
                         "names": names, "color": color, "secondbar": secondbar}
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Commucate)
class Commucate(admin.ModelAdmin):
    list_display = ('id', 'userFrom', 'userTo')
    list_filter = ('userFrom', 'userTo')


@admin.register(Messages)
class Messages(admin.ModelAdmin):
    list_display = ('room', 'user', 'message', 'date')
    list_filter = ('room', 'user', 'date')
    search_fields = ("message__startswith", )


@admin.register(Typeof)
class TypeofAdmib(admin.ModelAdmin):
    list_display = ('id','title', 'describe')
    search_fields = ("title__startswith", )


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('userFrom', 'userTo', 'raiting', 'date')
    list_filter = ('date', 'userFrom', 'userTo')


@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = ('id', 'title', 'describe')
    search_fields = ("title__startswith", )


@admin.register(Proposal)
class Proposal(admin.ModelAdmin):
    list_display = ('id', 'application', 'company')
    list_filter = ('application', 'company')
