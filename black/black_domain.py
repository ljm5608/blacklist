import os
import subprocess

class BlackDomain:

    def __init__(self):
        self.domain_set = []
        self.domain_set_ns = []
        self.domain = ""
        self.ipv4_set = []
        self.ipv6_set = []

        self.input_domain()
        self.ns_lookup()
        self.slicing_domain()

    def input_domain(self):
        while True:
            ans = ""
            print("차단할 domain을 입력하세요.")
            domain_temp_str = input("comma(,) 구분 > ")
            domain_temp_str = domain_temp_str.split(",")
            while True:
                length = len(domain_temp_str)
                print(f"{length}개의 domain을 입력하였습니다.{domain_temp_str}")
                ans = input("입력하신 domain이 맞습니까? (Y/N) > ")
                if ans == "Y":
                    self.domain_set = domain_temp_str.copy()
                    return
                elif ans == "N":
                    break
                else:
                    print("올바른 값을 입력하세요")
                    break

    def ns_lookup(self):
        for domain in self.domain_set:
            command = "nslookup " + domain
            sysMsg = subprocess.getstatusoutput(command)
            self.domain_set_ns = sysMsg[1]
            self.domain_set_ns = self.domain_set_ns.replace("    ", " ")
            self.domain_set_ns = self.domain_set_ns.replace("  ", " ")
            self.domain_set_ns = self.domain_set_ns.replace("\n", " ")
            self.domain_set_ns = self.domain_set_ns.replace("\t", " ")
            self.domain_set_ns = self.domain_set_ns.split(" ")
            self.domain_set_ns = [v for v in self.domain_set_ns if v]

    def slicing_domain(self):
        idx = 0
        for i in range(len(self.domain_set_ns)):
            if self.domain_set_ns[i] == "이름:":  # 이름값 담기
                idx = i
                break
        idx += 1
        length = len(self.domain_set_ns)
        self.domain = self.domain_set_ns[idx]  # 이름변수 담기

        for i in range(idx + 2, length):  # ip담기 (ipv4, ipv6구분)
            if self.domain_set_ns[i] == 'Alias:' or self.domain_set_ns[i] == 'Aliases:': break
            if '.' not in self.domain_set_ns[i]:
                self.ipv6_set.append(self.domain_set_ns[i])
            else:
                self.ipv4_set.append(self.domain_set_ns[i])
        self.ipv4_set = ",".join(self.ipv4_set)  # 문자열로 변환
        self.ipv6_set = ",".join(self.ipv6_set)

    def make_report_domain(self, dir, fname, date):
        with open(f"{dir}/{fname}.csv", 'w', encoding='utf-sig-8') as f:
            f.write("ZONE,도메인 객체 이름,도메인 네임,IPv4,IPv6,설명\n")  # 맨위에 목록 작성
            f.write(f"E,{self.domain}_공격차단")
            f.write(f',{self.domain},"{self.ipv4_set}",{self.ipv6_set},{date}_악성메일유포차단\n')