import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone
