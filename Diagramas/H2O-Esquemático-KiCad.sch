EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Dispositivo-H2O"
Date "                 2021-02-26"
Rev "Escobar J.W."
Comp "IER-UNAM"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Module:ESP8266LolinV3 U1
U 1 1 6038A7E0
P 2700 2550
F 0 "U1" V 2771 622 50  0000 R CNN
F 1 "ESP8266LolinV3" V 2680 622 50  0000 R CNN
F 2 "" H 1700 1400 50  0001 C CNN
F 3 "" H 1700 1400 50  0001 C CNN
	1    2700 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:R 2K2
U 1 1 60390CE3
P 2750 1400
F 0 "2K2" V 2543 1400 50  0000 C CNN
F 1 "R10" V 2634 1400 50  0000 C CNN
F 2 "" V 2680 1400 50  0001 C CNN
F 3 "~" H 2750 1400 50  0001 C CNN
	1    2750 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 220H1
U 1 1 60391E94
P 3200 1400
F 0 "220H1" V 2993 1400 50  0000 C CNN
F 1 "R11" V 3084 1400 50  0000 C CNN
F 2 "" V 3130 1400 50  0001 C CNN
F 3 "~" H 3200 1400 50  0001 C CNN
	1    3200 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 220H2
U 1 1 60392058
P 3650 1400
F 0 "220H2" V 3443 1400 50  0000 C CNN
F 1 "R12" V 3534 1400 50  0000 C CNN
F 2 "" V 3580 1400 50  0001 C CNN
F 3 "~" H 3650 1400 50  0001 C CNN
	1    3650 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 2K3
U 1 1 603921C6
P 4100 1400
F 0 "2K3" V 3893 1400 50  0000 C CNN
F 1 "R13" V 3984 1400 50  0000 C CNN
F 2 "" V 4030 1400 50  0001 C CNN
F 3 "~" H 4100 1400 50  0001 C CNN
	1    4100 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 220H3
U 1 1 60392407
P 4550 1400
F 0 "220H3" V 4343 1400 50  0000 C CNN
F 1 "R14" V 4434 1400 50  0000 C CNN
F 2 "" V 4480 1400 50  0001 C CNN
F 3 "~" H 4550 1400 50  0001 C CNN
	1    4550 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 2K1
U 1 1 603926DE
P 2300 1400
F 0 "2K1" V 2093 1400 50  0000 C CNN
F 1 "R9" V 2184 1400 50  0000 C CNN
F 2 "" V 2230 1400 50  0001 C CNN
F 3 "~" H 2300 1400 50  0001 C CNN
	1    2300 1400
	0    1    1    0   
$EndComp
$Comp
L Device:R 1K8
U 1 1 60395337
P 6500 3850
F 0 "1K8" H 6570 3896 50  0000 L CNN
F 1 "R1" H 6570 3805 50  0000 L CNN
F 2 "" V 6430 3850 50  0001 C CNN
F 3 "~" H 6500 3850 50  0001 C CNN
	1    6500 3850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female J8
U 1 1 6039C67C
P 6500 5950
F 0 "J8" V 6600 5900 50  0000 L CNN
F 1 "Conn_01x03_Female" V 6700 5550 50  0000 L CNN
F 2 "" H 6500 5950 50  0001 C CNN
F 3 "~" H 6500 5950 50  0001 C CNN
	1    6500 5950
	0    1    1    0   
$EndComp
Wire Wire Line
	4250 1400 4400 1400
Wire Wire Line
	3800 1400 3850 1400
Wire Wire Line
	3350 1400 3500 1400
Wire Wire Line
	2900 1400 3050 1400
Wire Wire Line
	2450 1400 2600 1400
$Comp
L Amplifier_Operational:LM324 U?
U 4 1 6040E4B5
P 6500 4800
F 0 "U?" V 6546 4570 50  0000 R CNN
F 1 "LM324" V 6455 4570 50  0000 R CNN
F 2 "" H 6450 4900 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm2902-n.pdf" H 6550 5000 50  0001 C CNN
	4    6500 4800
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6500 4500 6500 4000
Wire Wire Line
	4450 3150 6100 3150
Wire Wire Line
	6100 3150 6100 4000
Wire Wire Line
	6100 4000 6500 4000
Connection ~ 6500 4000
$Comp
L Connector:USB_A J?
U 1 1 60CA5CD6
P 5600 1250
F 0 "J?" H 5657 1717 50  0000 C CNN
F 1 "USB_A" H 5657 1626 50  0000 C CNN
F 2 "" H 5750 1200 50  0001 C CNN
F 3 " ~" H 5750 1200 50  0001 C CNN
	1    5600 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 1050 6200 1050
Wire Wire Line
	6200 1050 6200 700 
Wire Wire Line
	6200 700  5250 700 
Wire Wire Line
	5250 700  5250 1400
Wire Wire Line
	5250 1400 4700 1400
Wire Wire Line
	2450 1900 2450 1700
Wire Wire Line
	1850 1700 1850 1400
Wire Wire Line
	1850 1400 2150 1400
Wire Wire Line
	1850 1700 2450 1700
Wire Wire Line
	3850 1400 3850 1600
Wire Wire Line
	3850 1600 2300 1600
Wire Wire Line
	2300 1600 2300 1900
Connection ~ 3850 1400
Wire Wire Line
	3850 1400 3950 1400
Wire Wire Line
	6200 1050 6200 2600
Wire Wire Line
	6200 2600 7550 2600
Connection ~ 6200 1050
Wire Wire Line
	7550 2600 7550 5750
Wire Wire Line
	7550 5750 6600 5750
Wire Wire Line
	5600 1650 5600 1700
Wire Wire Line
	5600 1700 2450 1700
Connection ~ 2450 1700
Wire Wire Line
	5600 1700 5600 2950
Wire Wire Line
	5600 2950 6500 2950
Wire Wire Line
	7300 2950 7300 5600
Wire Wire Line
	7300 5600 6500 5600
Wire Wire Line
	6500 5600 6500 5750
Connection ~ 5600 1700
Wire Wire Line
	6400 5750 6400 5450
Wire Wire Line
	6400 5450 6600 5450
Wire Wire Line
	6600 5450 6600 5100
Wire Wire Line
	2300 3150 2300 5300
Wire Wire Line
	2300 5300 6400 5300
Wire Wire Line
	6400 5300 6400 5100
Wire Wire Line
	6500 3700 6500 2950
Connection ~ 6500 2950
Wire Wire Line
	6500 2950 7300 2950
$EndSCHEMATC
