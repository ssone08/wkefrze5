# 导入模块
import time
import winsound

# 定义专注时钟的函数
def focus_timer(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60
    # 循环倒计时
    while seconds:
        # 计算剩余的分钟和秒数
        mins, secs = divmod(seconds, 60)
        # 格式化倒计时的显示
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 在同一行打印倒计时
        print(timer, end='\r')
        # 暂停一秒
        time.sleep(1)
        # 减少一秒
        seconds -= 1
    # 倒计时结束，播放提示音
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    # 打印提示信息
    print("时间到了，可以休息一会了！")

# 主函数
if __name__ == '__main__':
    # 输入要专注的分钟数
    minutes = int(input("请输入你想要专注的分钟数："))
    # 调用专注时钟的函数
    focus_timer(minutes)
