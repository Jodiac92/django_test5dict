from django.shortcuts import render
from myapp.models import Profile

# Create your views here.
def MainFunc(request):
    return render(request, 'index.html')

def DictFunc(request):
    profile_list = Profile.objects.all()
    #print(len(profile_list))
    pro_list = []
    
    
    for pro in profile_list:
        pro_dict = {}
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
        #print(pro_list)
        
    context = {'pro_list':pro_list}
    return render(request, 'abc.html', context)
        
    