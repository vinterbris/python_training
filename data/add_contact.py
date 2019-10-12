from model.contact import Contact
import random
import string


constant = [
    Contact(first_name="first_name1", middle_name="middle_name1", last_name="last_name1",
            address="address1", phone_home="phone_home1", phone_mobile="phone_mobile1",
            phone_work="phone_work1", secondary_phone="secondary_phone1",
            email_1="email_11", email_2="email_21", email_3="email_21"),
    Contact(first_name="first_name2", middle_name="middle_name2", last_name="last_name2",
            address="address2", phone_home="phone_home2", phone_mobile="phone_mobile2",
            phone_work="phone_work2", secondary_phone="secondary_phone2",
            email_1="email_12", email_2="email_22", email_3="email_22")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="",last_name="", address="", phone_home="", phone_mobile="",
            phone_work="", secondary_phone="", email_1="", email_2="", email_3="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
            last_name=random_string("last_name", 10), address=random_string("address", 10),
            phone_home=random_string("phone_home", 10), phone_mobile=random_string("phone_mobile", 10),
            phone_work=random_string("phone_work", 10), secondary_phone=random_string("secondary_phone", 10),
            email_1=random_string("email_1", 10), email_2=random_string("email_2", 10), email_3=random_string("email_3", 10))
    for i in range(5)
]
