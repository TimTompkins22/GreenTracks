from django import forms




class NameForm(forms.Form):
    userName = forms.CharField(label='User Name',max_length = 100,required=False)
    firstName = forms.CharField(label='First Name',max_length = 100,required=False)
    lastName = forms.CharField(label='Last Name', max_length=100, required=False)
    totalDonations = forms.CharField(label='Total Donations', max_length=100, required=False)
    lastDonation = forms.CharField(label='Last Donation Date', max_length=100, required=False)
    customerNo = forms.CharField(label='Customer No', max_length=100,required=False)
    sourcingType = forms.CharField(label='Sourcing Type', max_length=100,required=False)
    accountType = forms.CharField(label='Created By', max_length=100,required=False)
    group = forms.CharField(label='Member of:', max_length=100,required=False)
    SAPSalesOrder = forms.CharField(label='SAP Sales Order', max_length=100,required=False)
    quoteOrder = forms.CharField(label='Quote/Order Completed By', max_length=100,required=False)
    orderClass = forms.CharField(label='Order Class', max_length=100,required=False)


class GroupForm(forms.Form):
    groupName = forms.CharField(label='Group Name',max_length = 100,required=False)
    totalMembers = forms.CharField(label='Total Members',max_length = 100,required=False)
    totalDonations = forms.CharField(label='Total Donations', max_length=100, required=False)
    lastDonation = forms.CharField(label='Last Donation Date', max_length=100,required=False)
    sourcingType = forms.CharField(label='Sourcing Type', max_length=100,required=False)
    accountType = forms.CharField(label='Created By', max_length=100,required=False)
    group = forms.CharField(label='Member of:', max_length=100,required=False)
    SAPSalesOrder = forms.CharField(label='SAP Sales Order', max_length=100,required=False)
    quoteOrder = forms.CharField(label='Quote/Order Completed By', max_length=100,required=False)
    orderClass = forms.CharField(label='Order Class', max_length=100,required=False)


class LineItemForm(forms.Form):
    customer_description = forms.CharField(max_length=100, required=True)
    place_order_indicator = forms.BooleanField()
    mfg_brand_name = forms.CharField(max_length=100, required=True)
    find_mro_description = forms.CharField(max_length=100, required=True)
    item_comments_to_customer = forms.CharField(max_length=100)
    sap_material = forms.CharField(max_length=100)


#class LoginForm(AjaxForm):
#    email_address = forms.EmailField(label = "Email Address", required = True, max_length = 100,
#                    widget = forms.TextInput(attrs = {'placeholder': 'email@domain.com', 'autocomplete':'off'}))
#    password = forms.CharField(label = "Password", required = True, max_length = 100,
#                    widget = forms.PasswordInput(attrs = {'placeholder': 'Password', 'autocomplete':'off'}))#
#
#    def setup_form_helper(self, helper):
#        helper.form_id = 'login_form'
#        helper.layout = Layout(
#            'email_address',
#            'password',
#            Div(
#                Submit('submit', 'Login', css_class='btn btn-primary'),
#                css_class="form-group text-center"
#                ),
#            HTML('<p class="pull-right light-top-bottom-padding"><a href="/account/forgot-password" title="Forgot Password">Forgot Password?</a></p>')
#            )



