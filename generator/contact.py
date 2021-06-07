from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt #для чтения опций командной строки
import sys #чтобы получить доступ к этим опциям

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+  string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="",
                      fax="", email="", email2="", email3="", homepage="", bday="15",
                      bmonth="September", byear="5555", aday="14", amonth="November",
                      ayear="6666", address2="", phone2="", notes="")] + [
            Contact(firstname=random_string("firstname",20), middlename=random_string("middlename",20), lastname=random_string("lastname",20),
            nickname=random_string("nickname",10), title=random_string("title",10), company=random_string("company",20),
            address=random_string("address",20), homephone=random_string("homephone",10),mobilephone=random_string("mobilephone",10),
            workphone=random_string("workphone",10), fax=random_string("fax",10), email=random_string("email",20),
            email2=random_string("email2",20), email3=random_string("email3",20), homepage=random_string("homepage",20),
            address2=random_string("address2",20), phone2=random_string("phone2",10), notes=random_string("notes",20))
    for i in range(2)]

# определяем путь относительно директории проекта
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# отркываем файл на запись
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))