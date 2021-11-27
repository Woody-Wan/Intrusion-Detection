基于计算机视觉技术所设计的变电所限制区域人员入侵检测实现了人员入侵的分级报警和手动绘制限制区域报警。根据对方法的整体测试结果分析，对于入侵人员检测的准确率可以达到 84.7%，检测速度在 GTX1060显卡的计算机上能够达到 23 帧每秒，且能够对实时画面中的人员进行快速的距离判断以及警报处理，方法整体的实时性较强、可靠性较佳，基本满足方法的性能要求，对变电所的安全稳定运行具有一定的现实与经济意义。

![QQ图片20211110214340](https://user-images.githubusercontent.com/63642698/141228201-1c2c100e-2a27-4609-b6c9-cf2fe2617ad9.png)

![QQ图片20211110214350](https://user-images.githubusercontent.com/63642698/141228205-1c8df17c-56f0-490e-8324-c390fc32b9e4.png)

The substation is an important hub for the reception and distribution of electrical 
energy and is the cornerstone and support of the entire power grid system. A safe and 
stable operation of the substation is of great significance for social stability and 
economic production. In order to ensure the safe and stable operation of substations, 
intrusion detection and alarming is required in the restricted areas of substations to 
avoid damage and theft of substation equipment caused by personnel intrusion. 
Therefore, the installation of intrusion detection systems in restricted areas of 
substations is of great practical importance. 
This thesis takes computer vision technology as a starting point to discuss the 
practical feasibility of target detection algorithms for intrusion detection in restricted 
areas of substations, and based on the location and geometric parameters of intruders 
identified by the target detection algorithm, a distance calculation is performed using 
a monocular ranging algorithm, and the distance information obtained is compared 
with the actual specified safety distance of the substation to achieve real-time 
intrusion warning. In this thesis, firstly, the advantages and disadvantages of the three 
target detection algorithms are analyzed by studying and testing the Faster R-CNN, 
HOG-SVM and YOLO algorithms, and finally YOLOv4, which meets the scenario of 
personnel intrusion in the restricted area of the substation, is selected as the target 
detection algorithm used in the design method of this thesis. Two common monocular 
ranging algorithms, the similar triangle based monocular ranging algorithm and the 
extinction point method based monocular ranging algorithm, were then studied, 
derived and analyzed. The similar triangle based monocular ranging algorithm, which 
fits the application scenario, was simplified and optimized, while an auxiliary 
algorithm based on the ray method was designed as an aid to intrusion detection based 
on the errors that exist under this principle. Running the method, the warning distance 
and alarm distance for intrusion detection of persons in restricted areas can be set 
manually to monitor the real-time image: if the person is outside the safe distance and 
greater than the warning distance, the person distance information is displayed; if the 
person is below the warning distance but greater than the safe distance, the warning 
alert is given; if the person enters within the safe distance, the alarm alert is triggered; 
if the person intrudes into the manually drawn restricted area, the If a person intrudes 
into a manually drawn restricted area, an alarm is immediately issued. 
This thesis is based on the computer vision technology designed by the 
substation restricted area personnel intrusion detection to achieve a hierarchy of 
personnel intrusion alarm and manual drawing restricted area alarm. According to the 
analysis of the overall test results of the method, the accuracy rate of intruder 
detection can reach 84.7%, the detection speed can reach 23 frames per second on a 
computer with GTX1060 graphics card, and it can make fast distance judgement and 
alarm processing for the personnel in the real-time screen, the overall real-time 
performance of the method is stronger and more reliable, which basically meets the 
performance requirements of the method and has certain practical and economic 
significance for the safe and stable operation of substations. It is of practical and 
economic significance for the safe and stable operation of substations. 
