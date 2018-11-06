from typing import List
from difflib import SequenceMatcher
import datetime


# Source request should be none until a sourcing specialist adds a vendor to it
class Account:
    def __init__(self,user_id, account_type, user_name, fname, lname, group, password):
        self.account_type = account_type
        self.user_name = user_name
        self.first_name = fname
        self.last_name = lname
        self.group = group
        self.join_date = ""
        self.user_id = user_id
        self.password = password
        self.email = None
        self.status = False



class Admin(Account):
    def __init__(self, user_id, user_name, fname, lname, group, password):
        Account.__init__(self, user_id, 'Admin', user_name, fname, lname, group, password)


class Supervisor(Account):
    def __init__(self, user_id, user_name, fname, lname, group, password):
        Account.__init__(self, user_id, 'Supervisor', user_name, fname, lname, group, password)


class Users(Account):
    def __init__(self, user_id, user_name, fname, lname, group, password):
        Account.__init__(self, user_id, 'User', user_name, fname, lname, group,password)


class Address:
    def __init__(self, city: str, street: str, zipcode: str, state: str, country: str):
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.state = state
        self.country = country


class VendorItem:
    def __init__(self, name: str, part_num: int, description: str, material_num: str, price: float, brand_name: str):
        self.name = name
        self.part_num = part_num
        self.description = description
        self.material = material_num
        self.price = price
        self.brand_name = brand_name


class Vendor:
    def __init__(self,
                 vendor_id: int,
                 name: str,
                 phone: str,
                 email: str,
                 v_address: Address,
                 v_inventory: List[VendorItem],
                 is_redbook=False):
        self.vendor_id = vendor_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = v_address
        self.inventory = v_inventory
        self.is_redbook = is_redbook


class Group:
    def __init__(self,
                 group_id: int,
                 group_name: str,
                 address: Address,
                 founded: datetime,
                 email: str):
        self.group_id = group_id
        self.group_name = group_name
        self.address = address
        self.founded=founded
        self.contact =""
        self.email = email




class DonationItem:
    def __init__(self,
                 item_id: int,
                 dontype: str,
                 mattype: str,
                 weight: int,
                 quantity: int =1):
        self.item_id = item_id
        self.dontype = dontype
        self.mattype = mattype
        self.quantity = quantity
        self.weight = weight


## when creating a new donation, set the donation id as the count of current donations, it will be +1 of the previous id then
class Donation:
    def __init__(self,
                 donation_id: int,
                 don_date: datetime,
                 group: Group,
                 donated_by: Account,
                 donation_items: List[DonationItem],
                 approval_date: datetime = None,
                 approval: bool = False,
                 total: int = 0,
                 status: str = 'Unapproved'):
        self.donation_id = donation_id
        self.status = status
        self.don_date = don_date
        self.approval_date = approval_date
        self.group = group
        self.donated_by = donated_by
        self.approval = approval
        self.donation_items = donation_items
        self.total=total


class SearchClass:
    def __init__(self, mfg_brand, mfg_part_num, mro_descr):
        self.mfg_brand = mfg_brand
        self.mfg_part_num = mfg_part_num
        self.mro_descr = mro_descr


# Insert Dummy Data


class StaticData:
    def __init__(self):
        StaticData.create_data(self)
        self.donation_data = StaticData.create_data(self)
        self.groups =""
        self.users =""

    def create_data(self):
        # Setup Vendor Items and Vendors List
        item1 = VendorItem("Hammer", 133, "Purple Hammer", "Metal", 60.00, "Brand1")
        item2 = VendorItem("Wood", 252, "4 by 4 wood", "Wood", 5.00, "Brand2")
        item3 = VendorItem("Lamp", 136, "Green lampshade", "Wool", 10.00, "Brand3")
        item4 = VendorItem("Broom", 200, "Wooden 2 foot", "Wood", 8.00, "Brand4")
        item5 = VendorItem("Basketball", 100, "12 inch diameter", "Leather", 12.00, "Brand5")
        item6 = VendorItem("Chair", 50, "Wooden red leather chair", "Leather", 250.00, "Brand6")
        item7 = VendorItem("Monitor", 209, "24 inch, 144hz", "Electric", 300.00, "Brand7")
        item8 = VendorItem("Monitor", 211, "27 inch, 60hz", "Electric", 150.00, "Brand8")
        item9 = VendorItem("Water Bottle", 73, "Red snap top 24oz", "Plastic", 7.00, "Brand9")
        item10 = VendorItem("Phone", 95, "9000 cpu power", "Plastic", 1199.00, "Brand10")

        inventory1 = [item1, item3, item5, item6]
        inventory2 = [item2, item5, item7, item9]
        inventory3 = [item1, item4, item8]
        inventory4 = [item1, item2, item6, item9]
        inventory5 = [item4, item10]
        inventory6 = [item2, item3, item6, item10]



        add_beta = Address("GreenCastle", "415 E Anderson St.", "46135", "IN", "USA")
        Beta = Group(1, "Beta Theta Pi", add_beta, datetime.datetime(2018, 8, 11, 14, 22), "Beta@depauw.edu")

        add_theta = Address("GreenCastle", "815 S College Ave", "46135", "IN", "USA")
        Theta = Group(2, "Kappa A. Theta", add_theta,datetime.datetime(2018, 8, 12, 13, 16) ,"Theta@depauw.edu" )

        add_piphi = Address("GreenCastle", "303 S Locust St.", "46135", "IN", "USA")
        Piphi = Group(3, "Pi Phi", add_piphi, datetime.datetime(2018, 8, 14, 15, 26) ,"PiPhi@depauw.edu")

        add_phipsi = Address("GreenCastle", "110 E Larabee St.", "46135", "IN", "USA")
        Phipsi = Group(4, "Phi Psi", add_phipsi,datetime.datetime(2018, 8, 16, 14, 56), "PhiPsi@depauw.edu")

        add_delt = Address("GreenCastle", "1 Taylor Place", "46135", "IN", "USA")
        Delt = Group(5, "Delt", add_delt, datetime.datetime(2018, 8, 29, 18, 22), "Delt@depauw.edu")

        add_aphi = Address("GreenCastle", "202 E Hannah St.", "46135", "IN", "USA")
        Aphi = Group(6, "Alpha Phi", add_aphi, datetime.datetime(2018, 8, 30, 11, 26),  "AlphaPhi@depauw.edu")




        group_list = [Beta,Theta, Phipsi,Piphi, Delt, Aphi]

        group_dict = {}

        for egroup in group_list:
            group_dict[egroup.group_id] = egroup

        self.group_dict = group_dict

        # TODO: Add user_id's if wanted


        Tim= Admin(28, "TTime", "Tim", "Tompkins", Beta,"tompkins")
        user_delt = Supervisor(1, "Gitter", "Mike", "Littau", Delt,"tompkins")
        user_phipsi = Supervisor(2, "Andy", "Andrew", "Cochrane", Phipsi,"tompkins")
        user_piphi = Supervisor(3, "Jen534", "Jennifer", "Lynn", Piphi,"tompkins")
        user_aphi = Supervisor(4, "Kells", "Kelly", "Littau", Aphi,"tompkins")
        user_theta = Supervisor(5, "Leens", "Kathleen", "Thiel", Theta,"tompkins")
        filler = Users(6, "theUnRealaxer", "Steen", "Jorgensen", Delt,"tompkins")
        filler2 = Users(7, "loweredcracker", "Ben", "Zepp", Delt,"tompkins")
        filler1 = Users(8, "Dipsydoodler", "Nathan", "Greenberg", Beta,"tompkins")
        filler3 = Users(9,"I_B", "Ryan", "Horak", Beta,"tompkins")
        filler4 = Users(10, "Karch", "Sam", "Karcher", Beta,"tompkins")
        filler5 = Users(11,"Shaggy", "Matthew", "Netherton", Beta,"tompkins")
        filler6 = Users(12, "CoachK", "Mitch", "Kenter", Beta,"tompkins")
        filler7 = Users(13,"SplashBro1", "Joe", "Mooney", Beta,"tompkins")
        filler8 = Users(14,"Jazz", "Jasmine", "Torres", Aphi,"tompkins")
        filler9 = Users(15,"Jessie", "Jess", "Spect", Aphi,"tompkins")
        filler10 = Users(16,"MaryGrace", "Mary", "Travers", Aphi,"tompkins")
        filler11 = Users(17,"AnnE", "Anne", "Eck", Theta,"tompkins")
        filler12 = Users(18,"Jet", "JoEllen", "Thome", Theta,"tompkins")
        filler13 = Users(19,"JerryM", "Gianna", "McFadles", Theta,"tompkins")
        filler14 = Users(20,"Rosie", "Rose", "Belcastro", Theta,"tompkins")
        filler15= Users(21,"Cait", "Caitlin", "Garrity", Theta,"tompkins")
        filler16 = Users(22,"Zandra", "Alexandra", "Kaldis", Theta,"tompkins")
        filler17 = Users(23,"Sidthekid", "Sidney", "Burns", Piphi,"tompkins")
        filler18 = Users(24,"KayAnne", "Kaylyn", "Norton", Piphi,"tompkins")
        filler19 = Users(25,"Allie", "Allison", "McAndrew", Piphi,"tompkins")
        filler20 = Users (26,"Tmoney", "Tim", "Joliffe", Phipsi,"tompkins")
        filler21 = Users (27,"JFay", "John", "Fay", Phipsi,"tompkins")
        Tim.join_date= datetime.datetime(2018, 9, 10, 11, 11)
        user_delt.join_date = datetime.datetime(2018, 9, 12, 10, 30)
        user_phipsi.join_date = datetime.datetime(2018, 9, 13, 12, 45)
        user_theta.join_date =datetime.datetime(2018, 9, 14, 14, 17)
        user_aphi.join_date = datetime.datetime(2018, 9, 15, 17, 23)
        user_piphi.join_date = datetime.datetime(2018, 9, 15, 18, 54)
        filler.join_date = datetime.datetime(2018, 9, 16, 17, 38)
        filler1.join_date = datetime.datetime(2018, 9, 17, 12, 12)
        filler2.join_date = datetime.datetime(2018, 9, 18, 11, 26)
        filler3.join_date = datetime.datetime(2018, 9, 19, 9, 19)
        filler4.join_date = datetime.datetime(2018, 9, 20, 8, 9)
        filler5.join_date = datetime.datetime(2018, 9, 21, 10, 13)
        filler6.join_date = datetime.datetime(2018, 9, 22, 12, 7)
        filler7.join_date = datetime.datetime(2018, 9, 23, 14, 15)
        filler8.join_date = datetime.datetime(2018, 9, 24, 19, 33)
        filler9.join_date = datetime.datetime(2018, 9, 25, 11, 51)
        filler10.join_date = datetime.datetime(2018, 9, 26, 13, 57)
        filler11.join_date = datetime.datetime(2018, 9, 27, 7, 12)
        filler11.join_date = datetime.datetime(2018, 9, 28, 10, 20)
        filler12.join_date = datetime.datetime(2018, 9, 29, 9, 39)
        filler13.join_date = datetime.datetime(2018, 9, 30, 14, 53)
        filler14.join_date = datetime.datetime(2018, 10, 1, 13, 14)
        filler15.join_date = datetime.datetime(2018, 10, 2, 16, 29)
        filler16.join_date = datetime.datetime(2018, 10, 3, 15, 17)
        filler17.join_date = datetime.datetime(2018, 10, 4, 18, 53)
        filler18.join_date = datetime.datetime(2018, 10, 5, 11, 34)
        filler19.join_date = datetime.datetime(2018, 10, 6, 13, 23)
        filler20.join_date = datetime.datetime(2018, 10, 7, 7, 45)
        filler21.join_date = datetime.datetime(2018, 10, 8, 9, 41)

        user_list= [Tim, user_aphi, user_delt, user_phipsi, user_piphi, user_theta, filler, filler1, filler2, filler3, filler4, filler5, filler6, filler7, filler8, filler9, filler10, filler11, filler12, filler13, filler14, filler15, filler16, filler17, filler18, filler19, filler20, filler21]

        user_dict = {}
        Aphi.contact= user_aphi
        Delt.contact= user_delt
        Piphi.contact= user_piphi
        Beta.contact= Tim
        Phipsi.contact= user_phipsi
        Theta.contact= user_theta

        for udict in user_list:
            user_dict[udict.user_id] = udict

      #  for x in user_dict:
      #      User.objects.create_user(user_dict[x].user_name, user_dict[x].email, user_dict[x].password)



        self.user_dict = user_dict


        #item1 = DonationItem(1, "Other"  "Plastic", 5, v_alop, "Acer", 209,
         #                    mro_description="24 inch, 144hz")
        ##datetime.datetime(2020, 1, 1, 1),
        item1 = DonationItem(1, "Plastic", "Other", 5)
        #                 mro_description="24 inch, 144hz")
        item2 = DonationItem( 1, "Paper",  "Magazine",1)
        #                 mro_description="Nice phone big screen")
        item3 = DonationItem( 1, "Paper", "Standard", 80)
        item4 = DonationItem( 1, "Plastic","Bottle", 11)

        item5 = DonationItem(1, "Paper", "NewsPaper", 1)
        ##                 mro_description="iPhone X 64GB", net_cost_per_unit=700.00)
        item6 = DonationItem(1, "Cardboard","Boxes",7)
        #                 mro_description="1080 TI Graphics 12Ghz", net_cost_per_unit=650.00)
        item7 = DonationItem(1 , "Plastic", "Bottle", 3)
        item8 = DonationItem(1,  "Aluminum", "Can", 12)
        item9 = DonationItem( 1, "Aluminum", "Can", 58)
        item10 = DonationItem(1, "Standard", "Standard", 29.3)
        item11 = DonationItem(1, "Standard", "Standard", 74.5)
        item12 = DonationItem(1, "Standard", "Standard", 13.4)
        item13 = DonationItem(1, "Standard", "Standard", 6.4)
        item14 = DonationItem(1, "Standard", "Standard", 48.3)
        item15 = DonationItem(1, "Standard", "Standard", 18.2)
        item16 = DonationItem(1, "Standard", "Standard", 41.0)
        item17 = DonationItem(1, "Standard", "Standard", 33.6)
        item18 = DonationItem(1, "Standard", "Standard", 7.8)
        item19 = DonationItem(1, "Standard", "Standard", 16.9)

        #                 mro_description="Surface Tablet 2018", net_cost_per_unit=999.99)

        don_items1 = [item1, item2, item3, item4]
        don_items2 = [item1, item3, item5, item7]
        don_items3 = [item1, item7, item6]
        don_items4 = [item2, item4, item6]
        don_items5 = [item3, item4, item5]
        don_items6 = [item3, item7]
        don_items7 = [item6, item4]
        don_items8 = [item1,  item9]
        don_items9 = [item2, item6, item9, item4, item5]
        don_items10 = [item3, item8]
        don_items11 = [item2, item9]
        don_items12 = [item5]
        don_items13 = [item9]
        don_items14 = [item10]
        don_items15 = [item11]
        don_items16 = [item12]
        don_items17 = [item13]
        don_items18 = [item14]
        don_items19 = [item15]
        don_items20 = [item16]
        don_items21 = [item17]
        don_items22 = [item18]
        don_items23 = [item19]


        # is MRO Description the line item description?

        don1 = Donation(1,
                             datetime.datetime(2018, 8, 9, 9, 00),
                             Beta,
                             Tim,
                             don_items22,
                             )
        don2 = Donation(2,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items4,
                             )
        don3 = Donation(3,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items23,
                             )
        don4 = Donation(4,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items18,
                             )
        don5 = Donation(5,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items8,
                             )
        don6 = Donation(6,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items14,
                             )
        don7 = Donation(7,
                             datetime.datetime(2018, 8, 8, 14, 11),
                             Beta,
                             Tim,
                             don_items1,
                             )
        don8 = Donation(8,
                             datetime.datetime(2018, 8, 9, 9, 00),
                             Beta,
                             Tim,
                             don_items4,
                             )
        don9 = Donation(9,
                             datetime.datetime(2018, 8, 9, 9, 00),
                             Theta,
                             user_theta,
                             don_items18,
                             )
        don10 = Donation(10,
                             datetime.datetime(2018, 8, 9, 9, 00),
                             Theta,
                             user_theta,
                             don_items7,
                             )
        don11 = Donation(11,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Theta,
                        user_theta,
                        don_items12,
                        )
        don12 = Donation(12,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        user_theta,
                        don_items13,
                        )
        don13 = Donation(13,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        user_theta,
                        don_items14,
                        )
        don14 = Donation(14,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Piphi,
                        user_piphi,
                        don_items15,
                        )
        don15 = Donation(15,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        user_piphi,
                        don_items16,
                        )
        don16 = Donation(16,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        user_piphi,
                        don_items17,
                        )
        don17 = Donation(17,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        user_phipsi,
                        don_items18,
                        )
        don18 = Donation(18,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        user_phipsi,
                        don_items19,
                        )
        don19 = Donation(19,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        user_phipsi,
                        don_items20,
                        )
        don20 = Donation(20,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Delt,
                        user_delt,
                        don_items21,
                        )
        don21 = Donation(21,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Delt,
                        user_delt,
                        don_items22,
                        )
        don22 = Donation(22,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Delt,
                        user_delt,
                        don_items23,
                        )
        don23 = Donation(23,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Delt,
                        user_delt,
                        don_items1,
                        )
        don24 = Donation(24,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        user_aphi,
                        don_items2,
                        )
        don25 = Donation(25,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        user_aphi,
                        don_items3,
                        )
        don26 = Donation(26,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        user_aphi,
                        don_items4,
                        )
        don27 = Donation(27,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        user_aphi,
                        don_items5,
                        )
        don28 = Donation(28,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        user_aphi,
                        don_items6,
                        )
        don29 = Donation(29,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Piphi,
                        user_piphi,
                        don_items7,
                        )
        don30 = Donation(30,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Beta,
                        filler,
                        don_items8,
                        )
        don31 = Donation(31,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Beta,
                        filler,
                        don_items9,
                        )
        don32 = Donation(32,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Beta,
                        filler1,
                        don_items10,
                        )
        don33 = Donation(33,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler1,
                        don_items11,
                        )
        don34 = Donation(34,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler2,
                        don_items12,
                        )
        don35 = Donation(35,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler2,
                        don_items13,
                        )
        don36 = Donation(36,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler3,
                        don_items14,
                        )
        don37 = Donation(37,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler3,
                        don_items15,
                        )
        don38 = Donation(38,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler3,
                        don_items16,
                        )
        don39 = Donation(39,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Beta,
                        filler4,
                        don_items17,
                        )
        don40 = Donation(40,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler4,
                        don_items18,
                        )
        don41 = Donation(41,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler5,
                        don_items19,
                        )
        don42 = Donation(42,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler5,
                        don_items20,
                        )
        don43 = Donation(43,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler5,
                        don_items21,
                        )
        don44 = Donation(44,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler5,
                        don_items22,
                        )
        don45 = Donation(45,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler6,
                        don_items23,
                        )
        don46 = Donation(46,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler6,
                        don_items1,
                        )
        don47 = Donation(47,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler7,
                        don_items2,
                        )
        don48 = Donation(48,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        filler7,
                        don_items3,
                        )
        don49 = Donation(49,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        filler8,
                        don_items4,
                        )
        don50 = Donation(50,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        filler8,
                        don_items5,
                        )
        don51 = Donation(51,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        filler8,
                        don_items6,
                        )
        don52 = Donation(52,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        filler9,
                        don_items7,
                        )
        don53 = Donation(53,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        filler9,
                        don_items8,
                        )
        don54 = Donation(54,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Aphi,
                        filler10,
                        don_items9,
                        )
        don55 = Donation(55,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Theta,
                        filler11,
                        don_items10,
                        )
        don56 = Donation(56,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Theta,
                        filler12,
                        don_items11,
                        )
        don57 = Donation(57,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Theta,
                        filler12,
                        don_items12,
                        )
        don58 = Donation(58,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Theta,
                        filler11,
                        don_items13,
                        )
        don59 = Donation(59,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler13,
                        don_items14,
                        )
        don60 = Donation(60,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler14,
                        don_items15,
                        )
        don61 = Donation(61,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler14,
                        don_items16,
                        )
        don62 = Donation(62,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler15,
                        don_items17,
                        )
        don63 = Donation(63,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler15,
                        don_items18,
                        )
        don64 = Donation(64,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler15,
                        don_items19,
                        )
        don65 = Donation(65,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler16,
                        don_items20,
                        )
        don66 = Donation(66,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        filler16,
                        don_items21,
                        )
        don67 = Donation(67,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler17,
                        don_items22,
                        )
        don68 = Donation(68,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler18,
                        don_items23,
                        )
        don69 = Donation(69,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler18,
                        don_items1,
                        )
        don70 = Donation(70,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler19,
                        don_items2,
                        )
        don71 = Donation(71,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler19,
                        don_items3,
                        )
        don72 = Donation(72,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler19,
                        don_items4,
                        )
        don73 = Donation(73,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler20,
                        don_items5,
                        )
        don74 = Donation(74,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler21,
                        don_items6,
                        )
        don75 = Donation(75,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler21,
                        don_items7,
                        )
        don76 = Donation(76,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler21,
                        don_items8,
                        )
        don77 = Donation(77,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler20,
                        don_items9,
                        )
        don78 = Donation(78,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        user_piphi,
                        don_items10,
                        )
        don79 = Donation(79,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Aphi,
                        user_aphi,
                        don_items11,
                        )
        don80 = Donation(80,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Delt,
                        user_delt,
                        don_items12,
                        )
        don81 = Donation(81,
                        datetime.datetime(2018, 8, 9, 9, 00),
                        Phipsi,
                        user_phipsi,
                        don_items13,
                        )
        don82 = Donation(82,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Theta,
                        user_theta,
                        don_items14,
                        )
        don83 = Donation(83,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        user_phipsi,
                        don_items15,
                        )
        don84 = Donation(84,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Delt,
                        user_delt,
                        don_items16,
                        )
        don85 = Donation(85,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        Tim,
                        don_items17,
                        )
        don86 = Donation(86,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Beta,
                        Tim,
                        don_items18,
                        )
        don87 = Donation(87,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler20,
                        don_items19,
                        )
        don88 = Donation(88,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Phipsi,
                        filler20,
                         don_items20,
                        )
        don89 = Donation(89,
                        datetime.datetime(2018, 8, 8, 14, 11),
                        Piphi,
                        filler19,
                        don_items21,
                        )



        query_result_list = [don1, don2, don3, don4, don5, don6, don7, don8, don9, don10, don11, don12, don13, don14,
                             don15, don16, don17, don18, don19, don20, don21, don22, don23, don24, don25, don26, don27,
                             don28, don29, don30, don31, don32, don33, don34, don35, don36, don37, don38, don39, don40, don41, don42, don43,
                             don44, don45, don46, don47, don48, don49, don50, don51, don52, don53, don54, don55, don56, don57, don58, don59, don60,
                             don61, don62, don63, don64, don65, don66, don67, don68, don69, don70, don71, don72, don73, don74, don75, don76, don77,
                             don78, don79, don80, don81, don82, don83, don84, don85, don86, don87, don88, don89]

     ##   historical_result_list = [req7, req8, req9]

     ##   historical_results = {}
     ##   for j in historical_result_list:
     ##       historical_results[j.request_id] = j

     ##   self.historical_request_data = historical_results

        # FIXME: Currently using ID for source request, this should be unique per request
        query_results = {}
        for i in query_result_list:
            query_results[i.donation_id] = i
       ## for j in

        self.donation = query_results

        self.time=0

        self.done= True

        self.current_user = Tim
    # FIXME: Maybe remove this? <- Sourcing specialists don't need this
    def add_to_user_dict(self, user_obj):
        if user_obj.user_id in self.user_dict.keys():
            print("Username is already used")
        else:
            self.user_dict[user_obj.user_id] = user_obj



    def add_to_donation_dict(self, don_obj):
            self.donation[don_obj.donation_id] = don_obj
           # self.query_results[don_obj.donation_id] = don_obj


    def add_to_vendor_dict(self, vendor_obj):
        if vendor_obj.vendor_id in self.vendor_dict.keys:
            print("VendorID already in dict")
        else:
            self.vendor_dict[vendor_obj.vendor_id] = vendor_obj


    @staticmethod
    def similarity_strings(item_a, item_b):
        return SequenceMatcher(None, item_a, item_b).ratio()

    # PrioritizePartNum, BrandName, keywords in description; isRedbook
    #def search_for_item(self, brand_name, item_part_num, item_descr):
        #vendor_sim_list = []
        #for key, vendor_v in self.vendor_dict.items():
        #    vendor_sim_item = 0.0
        #    item_sim_list = []
        #    has_brand_name, has_part_num = False, False

        #    if vendor_v.is_redbook is True:
        #        vendor_sim_item += 10  # Add some addition if item part is found or vendor is RedBook

        #    for items in vendor_v.inventory:
        #        item_sim = StaticData.similarity_strings(item_descr, items.description)
        #        vendor_sim_item += (item_sim * 10)
        #        item_sim_list.append((items, (item_sim * 10)))

        #        if items.brand_name == brand_name:
        #            vendor_sim_item += 8
        #            has_brand_name = True

        #        if items.part_num == item_part_num:
        #            vendor_sim_item += 15
        #            has_part_num = True

        #    sorted_item_sim_list = sorted(item_sim_list, key=lambda tup: -tup[1])

        #    vendor_class_obj = StaticData.vendor_search_item(vendor_v, vendor_sim_item, sorted_item_sim_list,
        #                                                      has_brand_name, has_part_num)
        #    vendor_sim_list.append(vendor_class_obj)

        #sorted_vendor_sim_list = sorted(vendor_sim_list, key=lambda x: -x.sim_score)

        #return sorted_vendor_sim_list

    def search_for_mro(self, brand_name, item_part_num, item_descr):
        req_sim_list = []
        # TODO: Should this be historical data or regular object?
        for key, request_r in self.historical_request_data.items():
            vendor_sim_item = 0.0
            item_sim_list = []
            has_brand_name, has_part_num = False, False

            for items in request_r.line_items:
                #  if items.cost_expire_date < datetime.datetime.now():  # Check is date is older than today
                if items.vendor.is_redbook is True:
                    vendor_sim_item += 10  # Add some addition if item part is found or vendor is RedBook

                if items.mro_description is not None:
                    item_sim = StaticData.similarity_strings(item_descr, items.mro_description)
                else:
                    item_sim = 0.0
                vendor_sim_item += (item_sim * 10)
                item_sim_list.append((items, (item_sim * 10)))

                if items.mfg_brand_name is not None and items.mfg_brand_name == brand_name:
                    vendor_sim_item += 8
                    has_brand_name = True

                if items.manufacturer_part is not None and items.manufacturer_part == item_part_num:
                    vendor_sim_item += 15
                    has_part_num = True

            sorted_item_sim_list = sorted(item_sim_list, key=lambda tup: -tup[1])

            vendor_class_obj = StaticData.vendor_search_item(request_r, vendor_sim_item, sorted_item_sim_list,
                                                             has_brand_name, has_part_num)
            req_sim_list.append(vendor_class_obj)

        sorted_request_sim_list = sorted(req_sim_list, key=lambda x: -x.sim_score)

        return sorted_request_sim_list

    class vendor_search_item:
        def __init__(self, vendor_obj, sim_score, item_scores, has_brand_name=False, has_part_num=False):
            self.vendor_obj = vendor_obj
            self.sim_score = sim_score
            self.item_scores = item_scores
            self.has_brand_name = has_brand_name
            self.has_part_num = has_part_num
