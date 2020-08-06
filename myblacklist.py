import datetime
from black.black_domain import BlackDomain
from black.black_ip import BlackIP
from black.black_network import BlackNetwork

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")

object = int(input("입력할 대상을 선택하세요. [1] ip [2] network 대역 [3] domain [0] 종료"))
dir = "blacklist_report"

if object == 1:
    fname = f"{date}_ip_blacklist"
    ip_black = BlackIP()
    ip_black.make_report_ip(dir, fname, date)
elif object == 2:
    fname = f"{date}_net_blacklist"
    net_black = BlackNetwork()
    net_black.slicing_net()
    net_black.make_report_network(dir, fname, date)
elif object == 3:
    fname = f"{date}_domain_blacklist"
    dom_black = BlackDomain()
    dom_black.make_report_domain(dir, fname, date)