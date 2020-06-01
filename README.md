# hukyroaster


<h1>Huky Stove – Gas Automation</h1>

<h2>Materials ~$47.00 CAD</h2>
-	Arduino 
-	Timing Belt and Pulley
-	Scrap wood used for motor mount and track system

Smraza Super Starter Kit (Arduino Clone Kit with stepper motor) - $35.99 Cdn
https://www.amazon.ca/gp/product/B06XXYVWVJ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
![arduino_motor](pics/arduino_motor.png?raw=true "Arduino setup with motor")
![stepper_motor](pics/stepper_motor.png?raw=true)


Fularr 3D Printer  2mm Pitch/6 mm shaft dia (matches stepper motor and Huky needle valve) - $11.90
https://www.amazon.ca/gp/product/B07PBXGL74/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1
![belt](pics/belt.png?raw=true)

<h2>Files Used</h2>
roaster.ino - Program to run on arduino  <br>
arduinoCommunicator.py - Runs in bg at start, receives all commands from artisanprog calls, sends to arduino over serial connection <br>
artisanprog.py - Sends commands to arduinoCommunicator on button presses or events  <br>
e.g. artisanprog.py KPAI 50 (Set motor position to 50% of kpa_max)

<h2>Initial Setup Steps</h2>
Download python 2.7 https://www.python.org/downloads/release/python-278/ <br>
<ol>
	<li>Load Arduino script onto Arduino (roaster.ino)
	<ul>
		<li>Test motor function </li>
	</ul>
	</li>
	<li>Setup Computer to have Artisan interface with Stepper Motor
	<ul>
		<li>Create folder for Artisanprog.py and Arduinocommunicator.py and save files there</li>
		<li>Setup buttons in artisan to trigger Artisanprog.py</li>
	</ul>
	</li>
	<li>Test
	<ul>
		<li>From Command prompt execute Arduinocommunicator.py (so it is awake), or create a button in artisan to start the program (artisan setup part b)</li>
		<li>From Artisan – click buttons and verify stepper motor is responding</li>
	</ul>
	</li>
	<li>Calibration
	<ul>
		<li>Determine amount of rotation for full gas and calculate number of steps (based on stepper motor specs. For this motor, one rotation = 4076 steps; full gas was 1 1/4 turns so kpa max is 5095 steps) note: this was taken starting from 0.5 kpa to allow manual startup and because the motor was not powerful enough to reliably turn the valve if it was closed tight </li>
		<li>Assign the max number of steps to kpa_max in artisanprog.py</li>
	</ul>
	</li>
	<li>Artisan setup
	<ul>
		<li>In buttons tab, create buttons to start and stop the Arduino communicator.</li>
			![start_stop](pics/artisan_buttons_1.png?raw=true)
		<li>In the events tab create a slider that gets the KPAI value and set it to burner; call program; C:\Python27\python.exe C:\Users\User\Documents\Arduino\hukyroaster-master\artisanprog.py KPAI {} </li>
			![sliders](pics/artisan_sliders.png?raw=true)
		<li>Press the button to start Arduino communicator, and then use the slider to adjust the gas until you reach kPa value you want to create a button for. Record these values (100 is max kPa, 0 is 0.5kPa) </li>
		<li>Create a button for each kPa value, adjusting the number at the end of the documentation column command line as well as the value of the slider to the recorded values; C:\Python27\python.exe C:\Users\User\Documents\Arduino\hukyroaster-master\artisanprog.py KPAI 100 </li>
        ![buttons_2](pics/artisan_buttons_2.png?raw=true)
		<li>Create alarms for each button to trigger at specified temperatures setting action to event button and the description as the button number (i.e. event Nr 22 is triggered when the bean temp reaches 340 which triggers event button 37, setting the gas to 2.5kPa) Note: set time to 00:00. This tells artisan to ignore time and only trigger based on temp. </li>
		![events](pics/artisan_events_1.png?raw=true)
	</ul>
	</li>
</ol>

![setup](pics/motor_belt_setup.jpg?raw=true)
![setup](pics/motor_belt_setup_2.jpg?raw=true)
![setup](pics/motor_belt_setup_3.jpg?raw=true)

