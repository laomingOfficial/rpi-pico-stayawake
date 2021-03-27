# 樹莓派Pico虛擬鼠標防休眠
 前段時間在淘寶上看到一款虛擬鼠標USB設備，作用是插入電腦之後鼠標就會一直移動，以防電腦休眠。
 肯定有人會問，幹嘛不把電腦的休眠模式給關閉就好，我對這點也很好奇。查了購買評論才發現說有些企業公司的電腦是不允許員工去更換休眠模式的，所以才需要這樣的設備去“防休眠”。

影片教程: [點這裡](https://www.youtube.com/watch?v=2P3kpWEMU6E)

安裝步驟:  
- 需要在Pico刷上 [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
- 把code.py粘貼到Pico盤裡
- 把[庫Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)下載到Pico裡