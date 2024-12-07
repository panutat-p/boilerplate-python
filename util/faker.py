from faker import Faker


def random_full_name_en() -> str:
    return "{} {}".format(Faker().first_name(), Faker().last_name())


def random_full_name_th() -> str:
    return "{} {}".format(Faker("th_TH").first_name(), Faker("th_TH").last_name())
