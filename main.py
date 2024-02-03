from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import smtplib

def work(Email):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.8",
        "sec-ch-ua": '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "Accept-Encoding": "gzip, deflate, br",
        "X-Forwarded-For": "27.7.81.18",
        "Cookie": "PHPSESSID=bf8d54908edd79099800eb54c228045ex-forwarded-proto:https"
    }
    ans = False
    gPrice = 0
    # need = int(input("Enter the target price : "))
    # We use while loop so that we loop until it stops returning captcha and then we get the price
    while ans == False:
        try:
            response = requests.get(url, headers=header)
            soup = BeautifulSoup(response.content, "html.parser")
            price = soup.find(class_="a-price-whole").getText()
            # int_price = price.split(".")[0].split(",")
            int_price = price.replace(',', '')
            # Price = int(int_price[0]+int_price[1])
            int_price = int_price.replace('.', '')
            Price = int(int_price)
            print(Price)
            gPrice = Price
            ans = True
        except AttributeError as err:
            ans = False

    myemail = "CashCraft.Official1@gmail.com"#"xassassinffx@gmail.com"
    toemail = Email
    password = "brnxwmekedthdmit"#"sziitqnghzwtxyyr"
    if gPrice < int(need):
        SUBJECT = "Price Alert"
        TEXT = f"Your product price has dropped!! for {url}"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(myemail, password)
        connection.sendmail(from_addr=myemail, to_addrs=Email, msg=message)
    else:
        print("The price is currently higher than target price")

url = ''
need = 0
priceAlerter = Flask(__name__)

@priceAlerter.route("/")
def home():
    return render_template("index.html")

@priceAlerter.route("/abstract")
def abstract():
    return render_template("index3.html")

@priceAlerter.route("/up")
def index():
    text = request.args.get('text', '')
    return render_template("index2.html", text=text)

@priceAlerter.route("/docs")
def docs():
    return render_template("docs.html")

@priceAlerter.route("/search", methods=['POST'])
def search():
    global url, need
    url = request.form.get('url')
    need = request.form.get('need')
    email = request.form.get('email')
    print(url, need)
    work(email)
    return redirect(url_for('index', text=url))

if __name__ == "__main__":
    priceAlerter.run(debug=True)


#header = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#    "Accept-Language": "en-US,en;q=0.8",
#    "sec-ch-ua": '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#    "Accept-Encoding": "gzip, deflate, br",
#    "X-Forwarded-For": "27.7.81.18",
#    "Cookie": "PHPSESSID=bf8d54908edd79099800eb54c228045ex-forwarded-proto:https"
#}
#ans = False
#gPrice = 0
##need = int(input("Enter the target price : "))
##We use while loop so that we loop until it stops returning captcha and then we get the price
#while ans==False:
#    try:
#        response = requests.get(url, headers=header)
#        soup = BeautifulSoup(response.content, "html.parser")
#        price = soup.find(class_="a-price-whole").getText()
#        #int_price = price.split(".")[0].split(",")
#        int_price = price.replace(',','')
#        #Price = int(int_price[0]+int_price[1])
#        int_price = int_price.replace('.', '')
#        Price = int(int_price)
#        print(Price)
#        gPrice = Price
#        ans = True
#    except AttributeError as err:
#        ans = False
#
#myemail = "xassassinffx@gmail.com"
#password = "sziitqnghzwtxyyr"
#if gPrice<need:
#    connection = smtplib.SMTP("smtp.gmail.com")
#    connection.starttls()
#    connection.login(myemail, password)
#    connection.sendmail(from_addr=myemail, to_addrs="latureanish@gmail.com", msg="Price Alert")
#else:
#    print("The price is currently higher than target price")