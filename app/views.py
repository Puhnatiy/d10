from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.db.models import Q
from app.models import Car



class CarList(ListView):
    model = Car
    template_name = 'car_list.html'
    def get_queryset(self):
        if 'btnSearch' in self.request.GET:
            query = self.request.GET.get('search', '')
            query = query.lower()
            flag = False
            if query == 'механика':
                query = 1
                flag = True
            elif query == 'автомат':
                query = 2
                flag = True
            elif query == 'робот':
                query = 3
                flag = True
            if flag:
                car_list = Car.objects.filter(
                    gearbox=query)
            else:
                car_list = Car.objects.filter(
                    Q(manufacturer__icontains=query)|
                    Q(model__icontains=query)|
                    Q(release_year__icontains=query)|
                    Q(color__icontains=query))
            return car_list
        return Car.objects.all()
