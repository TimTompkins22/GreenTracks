from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .classes import *
from .forms import NameForm
from .forms import GroupForm
import re

import copy

# Create your views here.

donation_data = (StaticData())

def index(request):
    return HttpResponseRedirect('/assigned_requests/')


def login(request):
    if (donation_data.time==0):
        donation_data.current_user = None
        print("none")
        donation_data.time=5
    username = request.POST.get("userName")
    password = request.POST.get("passWord")
    authenticate(username,password)
    #elif (request.POST.get("userName")):
    #        donation_data.time=2
    if (request.POST.get("newacc")):
        return render(request, 'request/new_user.html')
    return render(request, 'request/login.html',
                  {"current_user": donation_data.current_user, "time": donation_data.time})


def new_donation(request):

    qty = request.POST.get("qty")
    donType = request.POST.get("donType")
    itemType = request.POST.get("itemType")
    weight = request.POST.get("weight")
    size = request.POST.get("size")

    if request.POST.get("weight"):
        createDonation(createDonationItem([], weight, qty, donType, itemType,))
    #elif (request.POST.get("userName")):
    #        donation_data.time=2

    return render(request, 'request/new_donation.html',
                  {"current_user": donation_data.current_user, "time": donation_data.time})


def new_user(request):
    # FIXME: Update with new static data

    username = request.POST.get("username")
    name = request.POST.get("name")
    password = request.POST.get("password")
    group = request.POST.get("group")

    createuser(username, name, password, group)
    return render(request, 'request/new_user.html')



def assigned_request(request):

    update_donation_status()
    get_donation_total(donation_data)
    donation_data.time=0
    # if donation_data.current_user == ""
    #    0get_new_user()
    query_results = donation_data.donation
    listofusers = donation_data.user_dict
    groups=(donation_data.group_dict)
    return render(request, 'request/assigned_list.html', {"query_results": query_results, "listofusers":listofusers,
                                                          "current_user": donation_data.current_user, "groups":groups, "time": donation_data.time})


def settings(request):

    update_donation_status()
    donation_data.time=0

    get_donation_total(donation_data)
    if request.POST.get("yes"):
        print("111")
        donate= request.POST.get("yes")
        approve_donation(donate)
    if request.POST.get("no"):
        print("111111111")
        donate = (request.POST.get("no"))
        decline_donation(donate)
    # if donation_data.current_user == ""
    #    0get_new_user()
    query_results = donation_data.donation
    listofusers = donation_data.user_dict
    groups=(donation_data.group_dict)
    return render(request, 'request/settings.html', {"query_results": query_results, "listofusers":listofusers,
                                                          "current_user": donation_data.current_user, "groups":groups, "time": donation_data.time})


def status(request):

        donation_data.time = 0

        get_donation_total(donation_data)
        if request.POST.get("swap"):
            name = request.POST.get("swap")
            swap_status(name)
        # if donation_data.current_user == ""
        #    0get_new_user()
        query_results = donation_data.donation
        listofusers = donation_data.user_dict
        groups = (donation_data.group_dict)
        return render(request, 'request/status.html', {"query_results": query_results, "listofusers": listofusers,
                                                         "current_user": donation_data.current_user, "groups": groups,
                                                         "time": donation_data.time})


def main_donation(request,user_name):
    global donation_data
    query_results= donation_data.donation
    get_donation_total(donation_data)
    update_donation_status()


#    table_header = [table_column("DonatedBy", "text", form_id="donatedBy"),
#                    table_column("Group", "text", form_id="mfgBrandName"),
#                    table_column("Donation Weight", "text", form_id="MRODesc"),
#                    table_column("Items Donated", "text", form_id="vendorNumber"),
#                    table_column("QTY", "numeric", form_id="quantity"),
#                    table_column("UOM", "dropdown", ["%-Percentage", "EA-Each"], form_id="unitOfMeasure"),
#                    table_column("Sell_Price/Unit-USD", "numeric", form_id="sellPrice"),]

    currentprofile=""
    for x in donation_data.user_dict:
        if donation_data.user_dict[x].user_name==user_name:
            currentprofile= donation_data.user_dict[x]
            break;
    if currentprofile == "":
        for x in donation_data.group_dict:
            if donation_data.group_dict[x].group_name == user_name:
                currentprofile = donation_data.group_dict[x]
    if hasattr(currentprofile,'user_name'):
         data = {  # 'first_name': currentprofile.first_name,
            'userName': currentprofile.user_name,
            'firstName': currentprofile.first_name,
            'lastName': currentprofile.last_name,
            'totalDonations': get_total_donations(currentprofile.user_name),
             'lastDonation': get_last_donation(currentprofile.user_name),
    #       'transactionType': currentdonation_request.transaction_type,
    #       'customerNo': currentdonation_request.customer.customerSAP_number,
    #       'donationType': currentdonation_request.group_id,
    #       # 'createdBy': currentdonation_request.created_by.user_id,
    #       'customer': currentdonation_request.customer.customer_name,
     #      'SAPSalesOrder': currentdonation_request.sap_sales_order,
     #      # 'quoteOrder': currentdonation_request.quote_completed_by.datetime,
#
           'quoteOrder': currentprofile.last_name}
#
         form = NameForm(data)
    else:
        data = {  # 'first_name': currentprofile.first_name,
            'groupName': currentprofile.group_name,
            'totalMembers': count_members(currentprofile.group_name),
            #'lastName': currentprofile.last_name,
            'totalDonations': get_total_donations(currentprofile.group_name),
            'lastDonation': get_last_donation(currentprofile.group_name),
               }

        form = GroupForm(data)

    return render(request, 'request/main_donation.html',
                  {"table_list": [], "numLines": 5, "form": form,
                   "current_user": user_name, "query_results": query_results
                   })

class table_column():
    def __init__(self, name, data_type, dropdown_choices=[], is_readonly=False, is_last=False, form_id=None):
        self.name = name
        self.data_type = data_type
        self.dropdown_choices = dropdown_choices
        self.is_readonly = is_readonly
        self.isLast = is_last
        self.form_id=form_id


def get_one_donation(donation):
    sum = 0
    for x in donation:
        sum += 1
    return sum



def get_last_donation(name):
    for x in donation_data.donation:
        if donation_data.donation[x].donated_by.user_name == name or donation_data.donation[x].group.group_name == name:
            return donation_data.donation[x].don_date


def get_total_donations(name):
    sum=0
    for x in donation_data.donation :
        sum += 1
        if donation_data.donation[x].donated_by.user_name == name or donation_data.donation[x].group.group_name == name:
            get_one_donation(donation_data.donation[x].donation_items)
    return sum


def update_donation_status():
    for x in donation_data.donation:
    #    print(donation_data.donation[x].donation_id)
        if donation_data.donation[x].donated_by.status == True:
    #        print("yes11")
            donation_data.donation[x].status = "Approved"


def count_members(name):
    ct=0
    for x in donation_data.user_dict:
        if donation_data.user_dict[x].group.group_name == name:
            ct += 1
    return ct


def get_single_donation(donation):
    sum=0
    for x in donation.donation_items:
            sum+= float(x.weight)
    return sum


def get_donation_total(donation_data):
    for i in donation_data.donation:
        donation_data.donation[i].total= get_single_donation(donation_data.donation[i])



def logon (name, pw):
    user=donation_data.user_dict
    for x in user:
        if user[x].user_name == name:
            if (user[x].password == pw):
                donation_data.current_user=user[x]
                print("0")
                break;
    #print("fail")


def createuser(username, name, password, group):
    groups=donation_data.group_dict
    for x in groups:
        if groups[x].group_name == group:
            group=groups[x]
    donation_data.add_to_user_dict(Users(len(donation_data.user_dict), username, name, "" , group, password))


def createDonation(donitems):
    username= donation_data.current_user
    group = donation_data.current_user.group
    time= datetime.datetime.now()
    #print(group)
    #print("^^^")
    donation_data.add_to_donation_dict(Donation(len(donation_data.donation)+1, time, group, username, donitems))


def createDonationItem(donitems, weight, quantity, dontype, mattype):
    weight= weight
    quantity= quantity
    dontype=dontype
    matype=mattype
    newdono= DonationItem(1,dontype, matype, weight)
    return [newdono]

def addDonationItem(donitems, newdono):
    #print(newdono)
    return donitems.append(newdono)


def approve_donation(id):
    #print(id)
    for x in donation_data.donation:
    #    print(donation_data.donation[x].donation_id)
        if str(donation_data.donation[x].donation_id) == id:
    #        print("yes11")
            donation_data.donation[x].status = "Approved"
    #        print("yes")


def decline_donation(id):
    #print(id)
    for x in donation_data.donation:
     #   print(donation_data.donation[x].donation_id)
        if str(donation_data.donation[x].donation_id) == id:
     #       print("yes11")
            donation_data.donation[x].status = "Rejected"
      #      print("yes")


def swap_status(id):
    print(id)
    for x in donation_data.user_dict:
     #   print(donation_data.donation[x].donation_id)
        if str(donation_data.user_dict[x].user_id) == id:
            print(donation_data.user_dict[x].user_id)
            if (donation_data.user_dict[x].status):
                donation_data.user_dict[x].status = False
                print("off")
            else:
                donation_data.user_dict[x].status = True
                print("on")
      #      print("yes")

#TODO Add Status Change Functions Here


def authenticate(username=None, password=None):
    if ((username) and (password)):
        logon(username, password)
        if donation_data.current_user != None:
            print("success")
            donation_data.time = 3
        else:
            print("failx2")
            donation_data.time = 4