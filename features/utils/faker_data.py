from faker import Faker


class FakeData:
    fake = Faker()

    def fake_email(self):
        return self.fake.ascii_email()

    def fake_first_name(self):
        return self.fake.first_name()

    def fake_last_name(self):
        return self.fake.last_name()

    def fake_text(self):
        return self.fake.text()

    def fake_address(self):
        return self.fake.address()

    def fake_city(self):
        return self.fake.city()

    def fake_zip(self):
        return self.fake.zipcode()

    def fake_phone_number(self):
        return self.fake.phone_number()

    def fake_name(self):
        return self.fake.name()
