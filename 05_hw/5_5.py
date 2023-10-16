"""
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]

Країна	    Код  ISO	Префікс
Japan	    JP	+81
Singapore	SG	+65
Taiwan	    TW	+886
Ukraine  	UA	+380

}
"""

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
    country_type = ["UA", "JP", "TW", "SG"]
    jp = []
    sg = []
    tw = []
    ua = []
    fin_phone_list = []
    for tel in list_phones:
        tel_new = sanitize_phone_number(tel)
        if tel_new.startswith("81"):
            jp.append(tel_new)
        elif tel_new.startswith("65"):
            sg.append(tel_new)
        elif tel_new.startswith("886"):
            tw.append(tel_new)
        else:
            ua.append(tel_new)
    fin_phone_list = [ua, jp, tw, sg]
    fin_dic = dict(zip(country_type, fin_phone_list))

    return fin_dic
    
    



tel_base = ['380998759405', '818765347', '818765345', '8867658976', '657658976']
print(get_phone_numbers_for_countries(tel_base))
