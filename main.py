class TestClass:
    def __new__(cls):
        print("New metod ishlayapti")
        return super().__new__(cls)

    def __init__(self):
        print("Init metod ishlayapti")


obj = TestClass()
```

`__new__` metodining asosiy vazifasi yangi obyekt yaratishdir. U obyekt yaratish uchun javobgardir. `__init__` metodining vazifasi esa obyekt yaratilganidan keyin uning xususiyatlarini belgilashdir. `__new__` metodidan keyin `__init__` metodidan foydalanish kerak.
