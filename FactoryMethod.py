
 
class FrenchLocalizer:
 
    def __init__(self):
 
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
 
       
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    
 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    
 
    def localize(self, msg):
        return msg
 
def Factory(language ="English"):
 
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
 
    return localizers[language]()
 
if __name__ == "__main__":
 
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print("\nFrench", f.localize(msg))
        print("English", e.localize(msg))
        print("Spanish", s.localize(msg))