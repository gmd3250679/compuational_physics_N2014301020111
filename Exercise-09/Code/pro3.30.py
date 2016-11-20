class billiaro_collision:
    ...
    def calculate(self):
        ...
        while(...):
            ...
            #累计路程
            self.passed_road.append(self.passed_road[-1] + math.hypot(self.x[-1] - self.x[-2], self.y[-1] - self.y[-2]))
            #判断路程是不是超过了总路程
            if self.passed_road[-1] > self.total_road:
                temp_x = self.x[-1]
                temp_y = self.y[-1]
                #计算出小球的停止位置
                self.x[-1] = self.x[-2] + (temp_x - self.x[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                self.y[-1] = self.y[-2] + (temp_y - self.y[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                loop_calculate = False
            #经过的路程恰好等于总路程
            if self.passed_road[-1] == self.total_road:
                loop_calculate = False