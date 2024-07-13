import json


#{"id+id":[]}

class Chat:
    
    def __init__(self,users=[]):
        self.users=users
        try:
            with open("./src/db/Messanges.json","r",encoding="UTF-8") as f:
                self.data=json.load(f)
        except:
            with open("./src/db/Messanges.json","w",encoding="UTF-8") as f:
                json.dump({},f)
            self.data={}
        code1=self.users[0]+self.users[1]
        code2=self.users[1]+self.users[0]
        
        if code1 in self.data:
            self.code=code1
            self.sms=self.data[self.code]
        elif code2 in self.data:
            self.code=code2
            self.sms=self.data[self.code]
        else:
            self.code=code1
            self.sms=[]

        
    def add_sms(self,sms):
        #if "@clear" in sms:
        #    self.sms=[]
        #elif "@del_last" in sms:
        #    del self.sms[-1]
        #else:
        self.sms.append(sms)
    
    def get_sms(self):
        return self.sms
    
    def __del__(self):
        self.data[self.code]=self.sms
        with open("./src/db/Messanges.json","w",encoding="UTF-8") as f:
            json.dump(self.data,f)