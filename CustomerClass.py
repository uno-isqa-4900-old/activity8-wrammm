#create Customer class
class Customer:
    #Customer constructor
    def __init__(self, ID, firstName, lastName, company, address, city, state, zip):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    #method that returns address
    def getAddress(self):
        #if Customer does not have company attribute, don't return company in string
        if(self.company == ''):
            return self.firstName + ' ' + self.lastName + '\n' + self.address + '\n' + self.city + ', ' + self.state + ' ' + self.zip
        else:
            return self.firstName + ' ' + self.lastName + '\n' + self.company + '\n' + self.address + '\n' + self.city + ', ' + self.state + ' ' + self.zip