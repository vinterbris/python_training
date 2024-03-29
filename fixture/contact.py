from model.contact import Contact
import re


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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_main_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_contact_by_id(contact_id)
        self.choose_group_to_add_contact(group_id)
        wd.find_element_by_name("add").click()
        self.app.open_main_page()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.choose_group_to_delete_contact(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.app.open_main_page()
        self.contact_cache = None

    def choose_group_to_add_contact(self, id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % id).click()

    def choose_group_to_delete_contact(self, id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[1]" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self):
        self.modify_first_contact(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_main_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_main_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_main_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_main_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()

    def open_contact_to_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

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
                cells = element.find_elements_by_tag_name("td")
                lastname_text = element.find_element_by_xpath(".//td[2]").text
                firstname_text = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname_text, last_name=lastname_text, address=address,
                                                  id=id, all_phones=all_phones,
                                                  all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, address=address,
                       phone_home=phone_home, phone_work=phone_work,
                       phone_mobile=phone_mobile, secondary_phone=secondary_phone,
                       email_1=email, email_2=email2, email_3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(phone_home=phone_home, phone_work=phone_work,
                       phone_mobile=phone_mobile, secondary_phone=secondary_phone)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def clear_email(self, s):
        return s

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.phone_home, contact.phone_mobile,
                                            contact.phone_work, contact.secondary_phone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_email(x),
                                    filter(lambda x: x is not None,
                                           [contact.email_1, contact.email_2, contact.email_3]))))

    def clean(self, contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
