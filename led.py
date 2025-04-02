import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # 使用BCM引脚编号（即GPIO18）
GPIO.setwarnings(False) # 关闭警告（可选）
GPIO.setup(18, GPIO.OUT) # 设置GPIO18为输出模式
try:
print("LED 点亮！")
GPIO.output(18, GPIO.HIGH) # 输出高电平（3.3V），LED点亮
time.sleep(1) # 保持1秒
print("LED 熄灭！")
GPIO.output(18, GPIO.LOW) # 输出低电平（0V），LED熄灭
finally:
GPIO.cleanup() # 清理引脚资源（可选，防止下次报错）
