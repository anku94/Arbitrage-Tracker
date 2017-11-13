from win10toast import ToastNotifier
import requests, json, time

toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
              # "Python is 10 seconds awsm!",
              # icon_path="custom.ico",
              # duration=10)
# toaster.show_toast("Hello World!!!",
             # "Python is awsm by default!")

def show_message(s):
    toaster.show_toast('Arbitrage alert', s)

def get_ethex_price():
    URL = 'https://api.ethexindia.com/ticker/'
    r = requests.get(URL)
    r = json.loads(r.text)
    return r

def get_koinex_price():
    URL = 'https://koinex.in/api/ticker'
    r = requests.get(URL)
    r = json.loads(r.text)
    return r

def check_opp():
    ethex = get_ethex_price()
    koinex = get_koinex_price()
    e_price = ethex['last_traded_price']
    k_price = koinex['prices']['ETH']
    e_price = float(e_price)
    k_price = float(k_price)
    print '='*60
    print ' ', k_price
    print "- %s (%s + %s)" %(e_price * 1.01, e_price, 0.01 * e_price)
    diff = k_price - (1.01 * e_price)
    print '-'*60
    print ' ', diff
    if diff > 1000:
        show_message("Arbitrage opportunity worth %s" % diff)

def main_loop():
    while True:
        check_opp()
        time.sleep(60)


if __name__ == '__main__':
    main_loop()

