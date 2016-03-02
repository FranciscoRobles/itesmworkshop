import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import pyupm_i2clcd as lcd

# Create the buzzer object using GPIO pin 5
buzzer = upmBuzzer.Buzzer(3)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Create the button object using GPIO pin 0
button = grove.GroveButton(2)

contador = 0;

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)
# RGB Blue
#myLcd.setColor(53, 39, 249)

# Read the input and print, waiting one second between readings
while 1:
    print button.name(), ' value is ', button.value()
    # Play sound (DO, RE, MI, etc.), pausing for 0.1 seconds between notes
    if(button.read()==1):
      contador+=1;
      print contador;
      for chord_ind in range (0,2):
      # play each note for one second
      print buzzer.playSound(chords[chord_ind], 1000000)
      #Random numbers
      from random import randint
      # RGB Red
      myLcd.setColor(randint(0,255), randint(0,255), randint(0,255))
      time.sleep(0.1)
      myLcd.setCursor(1,2)
      myLcd.write('Hello World')
    
  time.sleep(1)
