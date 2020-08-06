class BlackIP:

    def __init__(self):
        self.ip_set = []
        self.input_ip()

    def input_ip(self):
        while True:
            ans = ""
            print("차단할 ip를 입력하세요.")
            ip_temp_str = input("comma(,) 구분 > ")
            ip_temp_str = ip_temp_str.split(",")
            while True:
                ip_length = len(ip_temp_str)
                print(f"{ip_length}개의 ip를 입력하였습니다.{self.ip_set}")
                ans = input("입력하신 IP가 맞습니까? (Y/N) > ")
                if ans == "Y":
                    self.ip_set = ip_temp_str.copy()
                    return
                elif ans == "N":
                    break
                else:
                    print("올바른 값을 입력하세요")
                    break

    def make_report_ip(self, dir, fname, date):
        with open(f"{dir}/{fname}.csv", 'w', encoding='utf-8-sig') as f:
            f.write("출발지 주소,출발지 포트,목적지 주소,목적지 포트,프로토콜,설명\n")  # 맨위에 목록 작성
            for i in self.ip_set:  # 데이터 줄마다 작성하기
                f.write(i)
                f.write(",ANY,ANY,ANY,ANY")
                f.write(f",EXT_Attack_{date}_{i}\n")
            for i in self.ip_set:  # 데이터 줄마다 작성하기
                f.write("ANY,ANY")
                f.write(f",{i},ANY,ANY")
                f.write(f",EXT_Attack_{date}_{i}\n")