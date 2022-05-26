class MainProvideLocators:

    driver_path = "C:/Users/IMOE001/PycharmProjects/pythonProject/pythonProject/Driver/chromedriver.exe"

    base_url = 'https://ivolunteer-app.herokuapp.com/'

    yosef_links = ["//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]/i[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]/i[1]"]

    oshri_links = ["//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/i[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]/i[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]/i[1]"]

    matan_links = ["//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[1]/i[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[2]/i[1]",
                   "//div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/a[3]/i[1]"]

    go_volunteer_button_var = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]"

    email_field_login = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"

    valid_email = 'salmon997@walla.co.il'

    password_field_login = "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"

    valid_password = '123456'

    send_button_login = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]"

    provide_assistance = "//button[2]"

    name_field = "//form[1]/div[1]/div[1]/div[1]/textarea[1]"

    name = 'salmon'

    last_name_field = "//form[1]/div[1]/div[2]/div[1]/textarea[1]"

    last_name = 'tasama'

    email_field_pv_page = "//form[1]/div[1]/div[3]/div[1]/textarea[1]"

    age_field = "//form[1]/div[1]/div[4]/div[1]/textarea[1]"

    age = "24"

    skills_field = "//form[1]/div[1]/div[5]/div[1]/textarea[1]"

    skill = 'Adult help'

    start_hour_field = "//form[1]/div[2]/div[1]/div[1]/textarea[1]"

    start_hour = '9:00'

    finish_hour_field = "//form[1]/div[2]/div[2]/div[1]/textarea[1]"

    finish_hour = '17:00'

    phone_number_field = "//form[1]/div[2]/div[3]/div[1]/textarea[1]"

    phone_number = '0547877244'

    profile_pic_field = "//form[1]/div[2]/div[4]/div[1]/textarea[1]"

    pic_url = "https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg"

    select_city_field = '//form[1]/div[2]/select[1]'

    language_field = "//form[1]/div[3]/div[1]/div[1]/textarea[1]"

    language = 'Hebrew'

    description_field = "//form[1]/div[3]/div[2]/div[1]/textarea[1]"

    desc = 'Nursing Home'

    send_button_pv_page = "//form[1]/div[3]/button[1]"

    name_pop_message = 'זהו שדה חובה.'

    massage_attribute = 'validationMessage'

    ui_name_developers = ["/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h2[1]",
                          "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]",
                          "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/h2[1]"]

    assert_name_developers = ['Lior Yosef', 'Oshri-el Tzagay', 'Matan ysayas']

    ui_logo = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/h1[1]"

    assert_ui_logo = 'iVolunteer'

    ui_logo_button = "//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1] "

    assert_ui_logo_button = 'Go-Volunteer!'

    text_provide_assistance = 'PROVIDE ASSISTANCE'

    ui_text_fields_provide_assistance = "//form[1]"

    text_fields_provide_assistance = "First name *\nFirst name *\nLast name *\nLast name *\nEmail *\nEmail " \
                                     "*\nAge\nAge\nSkills\nSkills\nStartHour\nStartHour\nFinishHour\nFinishHour" \
                                     "\nPhone\nPhone\nProfilePic\nProfilePic\nHaifa\nTel-Aviv\nJerusalem\nBeer " \
                                     "Sheva\nEilat\nKiryat Shmona\nBeer " \
                                     "Sheva\n\n\nLanguage\nLanguage\nDescription\nDescription\nSEND"

    ui_title_provide_assistance = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]"

    text_title_provide_assistance = 'Want\nTo\nVolunteer..?'

    ui_provide_assistance_Bottom_page1 = "//footer[1]/ul[1]"

    text_ui_provide_assistance_Bottom_page1 = "HomeServicesAboutTermsPrivacy Policy"

    ui_provide_assistance_Bottom_page2 = "//footer[1]/p[1]"

    text_ui_provide_assistance_Bottom_page2 = "i Volunteer © 2022"