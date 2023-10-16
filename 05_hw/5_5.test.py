def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phones_per_country = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone[:2] == '81':
            phones_per_country["JP"].append(phone)
        elif phone[:2] == '65':
            phones_per_country["SG"].append(phone)
        elif phone[:3] == '886':
            phones_per_country["TW"].append(phone)
        else:
            phones_per_country["UA"].append(phone)
    return phones_per_country

tel_base = ['818765347', '380998759405', '818765345', '8867658976', '657658976']
print(get_phone_numbers_for_countries(tel_base))