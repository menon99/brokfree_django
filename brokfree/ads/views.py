from django.shortcuts import render
import csv
from ads.models import property
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def enter_vals(request):
    with open('D:/study_material/software/project/housedata.csv', 'r') as file:
        content = csv.reader(file, delimiter=',')
        j=0
        for row in content:
            if j==0:
                j=1
                continue
            p=property()
            p.location = row[0]
            p.lattitude = float(row[1])
            p.longitude = float(row[2])
            p.name = row[3]
            p.address = row[4]
            p.description = row[5]
            p.furnishing = row[6]
            p.facing = row[7]
            p.water = row[8]
            p.bathroom = row[9]
            p.security = row[10]
            p.non_veg = row[11]
            p.lift = row[12]
            p.AC = row[13]
            p.swimming_pool = row[14]
            p.servant_room = row[15]
            p.gas_pipe = row[16]
            p.sewage_trt = row[17]
            p.v_parking = row[18]
            p.gym = row[19]
            p.club = row[20]
            p.child_play_area = row[21]
            p.park = row[22]
            p.house_keeping = row[23]
            p.internet = row[24]
            p.intercom = row[25]
            p.fire_safe = row[26]
            p.shopping = row[27]
            p.water_harv = row[28]
            p.power_back = row[29]
            rent = row[30]
            f = rent.find('/')
            rent = rent[:f]
            p.rent = int(rent)
            p.builtup = int(row[31])
            p.deposit = int(row[32])
            b = row[33]
            b = b[0]
            p.bedroom = int(b)
            p.btype = row[34]
            p.tenants = row[35]
            p.possession = row[36]
            p.parking = row[37]
            p.age = row[38]
            p.balcony = int(row[39])
            p.save()
    return HttpResponse('houses added to database')


@login_required(login_url='/login/')
def post_ad(request):
    return render(request, 'posting-ads.html')
    
class prop(object):
    def __init__(self,name,builtup,deposit,rent,furnishing,age,pt,avail,link):
        self.name=name
        self.builtup=builtup
        self.deposit=deposit
        self.rent=rent
        self.furnishing=furnishing
        self.age=age
        self.pt=pt
        self.avail=avail
        self.link=link

def search(request):
    if request.method=='GET':
        loc=request.GET['city']
        plist=property.objects.filter(location=loc)
        li=[]
        for i in plist:
            id=i.id
            link='/prop'+'/'+str(id)+'/'
            p=prop(i.name, int(i.builtup), int(i.deposit), int(i.rent), i.furnishing, i.age, i.tenants, i.possession,link)
            li.append(p)
    return render(request, 'search-homes.html',{'list':li})

def viewhome(request,id):
    i=int(id)
    p=property.objects.get(id=i)
    dic={
        'lat':p.lattitude,
        'long':p.longitude,
        'name':p.name,
        'addr':p.address,
        'desc':p.description,
        'loc':p.location,
        'furnish':p.furnishing,
        'face':p.facing,
        'water':p.water,
        'bath':p.bathroom,
        'bed':p.bedroom,
        'security':p.security,
        'non_veg':p.non_veg,
        'lift':p.lift,
        'ac':p.AC,
        'swimming':p.swimming_pool,
        'servant':p.servant_room,
        'gas_pipe':p.gas_pipe,
        'sewage':p.sewage_trt,
        'v_parking':p.v_parking,
        'gym':p.gym,
        'club':p.club,
        'child_play_area':p.child_play_area,
        'park':p.park,
        'house_keeping':p.house_keeping,
        'internet':p.internet,
        'intercom':p.intercom,
        'fire_safe':p.fire_safe,
        'shopping':p.shopping,
        'water_harv':p.water_harv,
        'power_back':p.power_back,
        'rent':p.rent,
        'deposit':p.deposit,
        'builtup':p.builtup,
        'btype':p.btype,
        'tenants':p.tenants,
        'possession':p.possession,
        'parking':p.parking,
        'age':p.age,
        'balcony':p.balcony,
    }
    return render(request,'view-home.html',dic)


def check(request):
    i=0
    if request.method=='GET':
        html=[]
        for k,v in request.GET.items():
            html.append('<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'.format(k, v, type(v)))
        return HttpResponse('<table>%s</table>' % '\n'.join(html))

def post(request):
    p=property()
    p.lattitude = request.POST['latitude']
    p.longitude = request.POST['longitude']
    p.name = request.POST['hname']
    p.address = request.POST['addr']
    p.description = request.POST['description']
    p.location = request.POST['locality']
    p.furnishing = request.POST['furnish_type']
    p.facing = request.POST['direction']
    p.water = request.POST['water_supply']
    p.bathroom=request.POST['no_of_bathrooms']
    p.bedroom=request.POST['no_of_bedrooms']
    p.security = request.POST['security']
    p.non_veg = request.POST['non_veg_allowance']
    p.lift = request.POST['lift_facility']
    p.AC = request.POST['airconditioner']
    p.swimming_pool = request.POST['swimming_pool']
    p.servant_room = request.POST['servant_room']
    p.gas_pipe = request.POST['gas_pipeline']
    p.sewage_trt = request.POST['sewage_treatment']
    p.v_parking = request.POST['visitor_parking']
    p.gym = request.POST['gym_facility']
    p.club = request.POST['club_house']
    p.child_play_area = request.POST['child_play_area']
    p.park = request.POST['park']
    p.house_keeping = request.POST['house_keeping']
    p.internet=request.POST['internet']
    p.intercom=request.POST['intercom']
    p.fire_safe=request.POST['fire_safety']
    p.shopping=request.POST['shopping']
    p.water_harv=request.POST['rainwater_harvesting']
    p.power_back=request.POST['power_backup']
    p.rent=request.POST['rentpm']
    p.deposit=request.POST['deposit']
    p.builtup=request.POST['sqft']
    p.btype=request.POST['prop_type']
    p.tenants=request.POST['tenant_type']
    p.possession=request.POST['possession_type']
    p.parking=request.POST['parking_type']
    p.age=request.POST['building_age']
    p.balcony=request.POST['balcony']
    p.save()
    c={'message':'Your property has been registered'}
    return render(request,'thank-you.html',c)



def filtered(request):
    if request.method=='GET':
        loc = request.GET['city']
        plist=property.objects.filter(location=loc)
        new_list=[]
        
        for p in plist:
            if int(p.rent) < int(request.GET['max']) and int(p.rent) > int(request.GET['min']):
                new_list.append(p)
        
        if 'radio' in request.GET.keys():
            temp=[]
            for p in new_list:
                if int(p.bedroom) == int(request.GET['radio']):
                    temp.append(p)
            new_list=temp
        
        if 'radio1' in request.GET.keys():
            temp=[]
            for p in new_list:
                if p.water == request.GET['radio1']:
                    temp.append(p)
            new_list=temp
        
        if 'radio2' in request.GET.keys():
            temp=[]
            for p in new_list:
                if p.tenants == request.GET['radio2']:
                    temp.append(p)
            new_list=temp
        
        if 'radio3' in request.GET.keys():
            temp=[]
            for p in new_list:
                if p.furnishing == request.GET['radio3']:
                    temp.append(p)
            new_list=temp
        
        li=[]
        for i in new_list:
            id = i.id
            link = '/prop'+'/'+str(id)+'/'
            p = prop(i.name, int(i.builtup), int(i.deposit), int(i.rent), i.furnishing, i.age, i.tenants, i.possession, link)
            li.append(p)
        
        empty=False
        if len(li)==0:
            empty=True
        return render(request, 'search-homes.html', {'list': li,'empty':empty})