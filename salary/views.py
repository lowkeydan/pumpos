from django.shortcuts import render
from salary.models import Person, Work, Salary


# Create your views here.
def index(request):
    person_all = Person.objects.all()
    work_detail_all = Work.objects.all()
    if request.method == "POST":
        person = request.POST.get('person')
        unit = request.POST.get('unit')
        work_detail = request.POST.get('work_detail')
        unit_price = Work.objects.get(work_detail=work_detail).unit_price
        salary_today = float(unit) * unit_price

        new_salary = Salary()
        new_salary.work_detail = Work.objects.get(work_detail=work_detail)
        new_salary.person = Person.objects.get(name=person)
        new_salary.unit = unit
        new_salary.salary_today = salary_today
        new_salary.save()
        print(person, float(unit), work_detail, unit_price, round(salary_today, 2))
    content = {'person_all': person_all, 'work_detail_all': work_detail_all, }
    return render(request, 'salary/index.html', content)
