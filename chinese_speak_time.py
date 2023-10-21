import pygame
from datetime import datetime

def speak_chinese(speed_rate=1):
    # 获取当前时间
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    # 转换小时为12小时制
    if hour == 0:
        hour_str = "12"
        am_pm = "AM"
    elif hour < 12:
        hour_str = str(hour)
        am_pm = "AM"
    elif hour == 12:
        hour_str = "12"
        am_pm = "PM"
    else:
        hour_str = str(hour - 12)
        am_pm = "PM"

    # 生成报时文本
    time_text = f"现在是 {am_pm}{hour_str}点{minute}分"

    # 播放报时
    pygame.init()
    pygame.mixer.init()

    # 播放 it's
    pygame.mixer.music.load(f"chinese_audio/its.mp3")
    pygame.mixer.music.play()
    pygame.time.delay(1000)  # 等待1秒，以确保it's音频播放完成

    # 播放 AM/PM
    am_pm_audio = pygame.mixer.Sound(f"chinese_audio/{am_pm}.mp3")
    am_pm_audio.play()
    pygame.time.delay(1000)  # 等待1秒，以确保AM/PM音频播放完成

    # 播放 hour
    hour_audio = pygame.mixer.Sound(f"chinese_audio/hour-{hour}.mp3")
    hour_audio.play()
    pygame.time.delay(1000)  # 等待1秒，以确保hour音频播放完成

    # 播放 dian
    dian_audio = pygame.mixer.Sound(f"chinese_audio/dian.mp3")
    dian_audio.play()
    pygame.time.delay(1000)  # 等待1秒，以确保dian音频播放完成

    # 播放 minute
    minute_audio = pygame.mixer.Sound(f"chinese_audio/min-{minute}.mp3")
    minute_audio.play()
    pygame.time.delay(1000)  # 等待1秒，以确保minute音频播放完成

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
