from smartphone import Smartphone, GamingPhone

# Create some objects
iphone = Smartphone("Apple", "iPhone 13", 85, 999)
gaming_phone = GamingPhone("Asus", "ROG Phone 5", 95, 1199, True)

# Interact with the objects
print(iphone.phone_info())
iphone.use_phone(3)  # Usage for 3 hours
iphone.charge_phone(10)  # Charge by 10%

print("\n")
print(gaming_phone.phone_info())
gaming_phone.activate_performance_mode()
gaming_phone.use_phone(5)  # Usage for 5 hours
gaming_phone.charge_phone(20)  # Charge by 20%
