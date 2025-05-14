# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life, price):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__battery_life = battery_life  # Private attribute (battery state)
        self.price = price  # Public attribute
    
    def get_battery_status(self):
        """Returns the battery status."""
        return f"{self.model} has {self.__battery_life}% battery left."
    
    def charge_phone(self, amount):
        """Charge the phone (with some limitations)."""
        if self.__battery_life + amount <= 100:
            self.__battery_life += amount
            print(f"{self.model} charged by {amount}%. Battery is now at {self.__battery_life}%.")
        else:
            self.__battery_life = 100
            print(f"{self.model} is fully charged!")
    
    def phone_info(self):
        """Returns a string with basic info about the phone."""
        return f"{self.brand} {self.model}, Battery: {self.__battery_life}%, Price: ${self.price}"
    
    def use_phone(self, hours):
        """Simulate phone usage by reducing battery life."""
        battery_drain = hours * 10  # Drain 10% battery per hour
        self.__battery_life = max(0, self.__battery_life - battery_drain)
        print(f"{self.model} used for {hours} hours. Battery now at {self.__battery_life}%.")

# Subclass: GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, price, performance_mode):
        super().__init__(brand, model, battery_life, price)
        self.performance_mode = performance_mode  # Extra attribute for gaming phones
    
    def activate_performance_mode(self):
        """Activate high-performance mode for gaming."""
        if self.performance_mode:
            print(f"{self.model} is now in high-performance mode!")
        else:
            print(f"{self.model} does not support high-performance mode.")
    
    def phone_info(self):
        """Override the parent method to include performance mode in the info."""
        parent_info = super().phone_info()
        return f"{parent_info} Performance Mode: {'Enabled' if self.performance_mode else 'Disabled'}"
