from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_main_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_first_contact(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_main_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self):
        self.modify_first_contact(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_main_page()
        self.contact_cache = None

    def fill_contact_fields(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.phone_fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("notes", contact.secondary_notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                firstname_text = element.find_element_by_xpath(".//td[3]").text
                lastname_text = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=firstname_text, last_name=lastname_text, id=id))
        return list(self.contact_cache)

