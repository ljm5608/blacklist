class BlackNetwork:

    def __init__(self):
        self.net_set = []
        self.net_set_slice = []
        self.input_net()

    def input_net(self):
        while True:
            ans = ""
            print("차단할 network를 입력하세요.")
            net_temp_str = input("comma(,) 구분 > ")
            net_temp_str = net_temp_str.split(",")
            while True:
                net_length = len(net_temp_str)
                print(f"{net_length}개의 network를 입력하였습니다.{net_temp_str}")
                ans = input("입력하신 network가 맞습니까? (Y/N) > ")
                if ans == "Y":
                    self.net_set = net_temp_str.copy()
                    return
                elif ans == "N":
                    break
                else:
                    print("올바른 값을 입력하세요")
                    break

    def slicing_net(self):
        for i in self.net_set:
            cnt = 0
            # data[i] = 111.111/24
            for j in i:
                cnt += 1
                if j =="/":
                    break
            self.net_set_slice.append([i[:cnt-1], i[cnt:]])

    def make_report_network(self, dir, fname, date):
        with open(f"{dir}/{fname}.csv", 'w', encoding='utf-8-sig') as f:
            f.write("ZONE,네트워크 이름,IP,설명\n")  # 맨위에 목록 작성
            for i in self.net_set_slice:  # 데이터 줄마다 작성하기
                f.write(f"E,EXT_Attack_{date}_{i[0]}_{i[1]}")
                f.write(f",{i[0]}/{i[1]},EXT_Attack_{date}_{i[0]}_{i[1]}\n")