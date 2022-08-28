        
from copy import copy


class Mess:
    def __init__(self, noidung, from_, to):
        self.from_ = from_
        self.to = to 
        self.noidung = noidung  

# tmp = {
#     "from":None,
#     "to":None,
#     'noiding':''
# } 

class Phone:
    def __init__(self, ten , belong, danhsach = []):
        self.ten = ten
        self.belongto = belong
        self.danhsach = danhsach
    
    def send_mess(self, noidung, to ):
        mess_sender = Mess(noidung, self.belongto, to)
        self.danhsach.append(mess_sender)
        receiver_phone = to.phone
        mess_receiver = copy(mess_sender)
        receiver_phone.append(mess_receiver)
        print("done!!")

class Person:
    def __init__(self, name, phone  ):
        self.name = name 
        self.phone = phone 
    
    def send(self, noidung, to):
        self.phone.send_mess(noidung, to)
    # def bam_dien_thoai(self, noidung,to): 
        #self.phone.sendmess(noidung,to )
    #def readmess(self, bywhom):
        # self.phone.sendmess(noidung,to )



        