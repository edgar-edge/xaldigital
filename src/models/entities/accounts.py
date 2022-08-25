class Account():

    def __init__(self, user_id, first_name=None,\
        last_name=None, company_name=None, address=None,\
        city=None, state=None, zip=None, phone1=None, phone2=None,\
        email=None,	department=None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email
        self.department = department
    
    def to_JSON(self):
        return {
            'user_id':self.user_id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'company_name':self.company_name,
            'address':self.address,
            'city':self.city,
            'state':self.state,
            'zip':self.zip,
             'phone1':self.phone1,
            'phone2':self.phone2,
            'email':self.email,
            'department':self.department
        }

