# ● (#1) Assign the arguments into appropriate attributes: data, talk_time, messages,
# cashback, validity and price via a parameterized constructor. All the attributes
# should be of int data type. Note that data is stored in Megabytes (1 GB = 1024
# MB) and the cashback amount is calculated from a percentage value.
# ● (#2,3,4) Implement driver code to display all the information of a package. Check
# if any particular attribute does not exist (is equal to 0), do not print that attribute.
# Attributes validity and price are always printed.

class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback, validity):
        self.price = price
        self.data = data
        self.talk_time = talk_time
        self.messages = messages
        self.cashback = cashback
        self.validity = validity
        self.store = ""
        self.cashback_store = ""
        
        
        for i in self.data:
            if chr(48) <= i <= chr(57):
                self.store += i
        for i in self.cashback:
            if chr(48) <= i <= chr(57):
                self.cashback_store += i
        self.ferot = (int(self.cashback_store) * self.price) // 100

                
        
        self.mb = int(self.store) * 1024
        








pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')

# Data = 6144 MB
if pkg.mb > 0:
    print(f"Data = {pkg.mb} MB")
else:
    pass

# Talktime = 99 Minutes
if pkg.talk_time > 0:
    print("Talktime =", pkg.talk_time, "Minutes")
else:
    pass

# SMS/MMS = 20
if pkg.messages > 0:
    print("SMS/MMS =", pkg.messages)
else:
    pass


# Validity = 7 Days
print("Validity =", pkg.validity, "Days")

# --> Price = 150 tk
print("--> Price =", pkg.price, "tk")

# Buy now to get 10 tk cashback.
if pkg.ferot > 0:
    print("Buy now to get", pkg.ferot, "tk cashback.")
else:
    pass



# Subtask 2: Check each attribute and print
pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
if pkg2.mb > 0:
    print(f"Data = {pkg2.mb} MB")
else:
    pass
if pkg2.talk_time > 0:
    print("Talktime =", pkg2.talk_time, "Minutes")
else:
    pass
if pkg2.messages > 0:
    print("SMS/MMS =", pkg2.messages)
else:
    pass
print("Validity =", pkg2.validity, "Days")
print("--> Price =", pkg2.price, "tk")
if "0" in pkg2.cashback:
    print("Buy now to get", pkg2.ferot, "tk cashback.")
else:
    pass










# Subtask 3: Check each attribute and print
pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')

if pkg4.mb > 0:
    print(f"Data = {pkg4.mb} MB")
else:
    pass
if pkg4.talk_time > 0:
    print("Talktime =", pkg4.talk_time, "Minutes")
else:
    pass
if pkg4.messages > 0:
    print("SMS/MMS =", pkg4.messages)
else:
    pass
print("Validity =", pkg4.validity, "Days")
print("--> Price =", pkg4.price, "tk")
if pkg4.ferot > 0:
    print("Buy now to get", pkg4.ferot, "tk cashback.")
else:
    pass
