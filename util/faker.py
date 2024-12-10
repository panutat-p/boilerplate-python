import random
from faker import Faker


def random_title_en() -> str:
    return random.choice(["Mr.", "Mrs.", "Ms.", "Miss", "Dr.", "Prof."])


def random_title_th() -> str:
    return random.choice(["นาย", "นาง", "นางสาว", "ดร.", "ศ."])


def random_full_name_en() -> str:
    return "{} {}".format(Faker().first_name(), Faker().last_name())


def random_full_name_th() -> str:
    return "{} {}".format(Faker("th_TH").first_name(), Faker("th_TH").last_name())


def random_email() -> str:
    return Faker().email()


def random_mobile_no() -> str:
    return (
        "0"
        + random.choice(["6", "8", "9"])
        + Faker().numerify("#")
        + "-"
        + Faker().numerify("###")
        + "-"
        + Faker().numerify("####")
    )


def random_phone_no() -> str:
    return "02" + "-" + Faker().numerify("###") + "-" + Faker().numerify("####")


def random_digit(n: int) -> str:
    return Faker().numerify("%" + "#" * (n - 1))
