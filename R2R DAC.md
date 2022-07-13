# R-2R数模转换

虽说知识不嫌多，但效率更重要，不要死磕在一处，善用Github的目录！  
因为插图是白底的，所以建议白底黑字观看
## 前言
这是一篇关于R-2R式数模转换器（以下简称R-2R）的文章.  
我的`High-tech Voltmeter`项目使用到了R-2R，但是关于R-2R的中文资料质量不佳，于是就有了此文章.  
我最开始是不想写的，直接复制一篇标个转载算了.  
但在网上找了一圈，但这些中文资料，嗯，说难听点就是在垃圾桶里找资料，干脆自己写吧（无意冒犯）.  
~~这不是论文，引用和参考双双失踪了.~~

## 基础复习
_**（以下所写的仅是是本文需要的知识，想要深入了解请自行查阅资料并学习）**_  
### [电压分配定则](https://en.wikipedia.org/wiki/Voltage_divider)
在初中，我们都学过欧姆定律$I=\frac{U}{R}$，然后老师会教我们推导出电压分配定则。  
那我们不妨再推导一次，复习一下，活络下脑子.  
这是一个很简单的串联电路：  
<img alt="Image" src=".\Images\1.svg">  
其总电压为$U_0$，两个电阻阻值分别为$R_1$和$R_2$.  
这样可以轻松的算出电流 $I=\frac{U_0}{R_1+R_2}$.  
从而得出电阻$R_1$分配到的电压$U_1=IR_1=\frac{U_0R_1}{R_1+R_2}$.  
此时可以整理出$U_1$，$U_2$与$U_0$，$R_1$，$R_2$的关系：  
$U_1=\frac{U_0R_1}{R_1+R_2}$  
$U_2=\frac{U_0R_2}{R_1+R_2}$  
这就是电压分配定则.  
实际中会遇到更多串联电阻，此时可以用整体思想将其化简.  
_（说句题外话，大部分中文资料上对于电压分配定则的解释都是 **在串联电路中，各负载分到的电压与其阻抗成正比关系** 但是根据推导式来看好像有误.）_

### [电压源](https://en.wikipedia.org/wiki/Voltage_source)  
<img alt="Image" src=".\Images\2.svg">

我们在生活中见到的电源大多数都是电压源，例如电池，市电.  
电压源也有直流和交流之分，称为为**直流电压源**和**交流电压源**.  
理想电压源有许多性质：  
1. 两端的电压保持不变，而电流会改变.  
2. 内阻为0.  
3. ......

但因为各种因素，没有真正的电压源是理想的.  

### [电流源](https://en.wikipedia.org/wiki/Current_source)
<img alt="Image" src=".\Images\3.svg">

生活中很少能见到电流源，并且R-2R也用不上，所以我也不详细解释，把他当作一个模型就好.  
理想电流源有许多性质，且大多数与理想电压源相反：  
1. 其电流保持不变，而两端的电压会改变.  
2. 内阻为无穷大.  
3. ......

但因为各种因素，没有真正的电流源是理想的.   
还有个违背直觉的特性，虽然没什么用，但我还是想说一说：  
电流源不能开路，如果开路，意味着电流为0，与其性质相悖（现实中的电流源开路会因为电压过大而损坏元器件）.

### 电阻的化简
两个电阻串联：$R_总=R_1+R_2$  
两个电阻串联：$R_总=\frac{R_1R_2}{R_1+R_2}$  
可以自己通过欧姆定律算出来，这里就不赘述了

## 理论支撑
_**（以下所写的仅是是本文需要的知识，想要深入了解请自行查阅资料并学习）**_  
### [戴维南定理](https://en.wikipedia.org/wiki/Th%C3%A9venin%27s_theorem)
戴维南定理（Thevenin's theorem）又称等效电压源定律，由[Hermann von Helmholtz](https://en.wikipedia.org/wiki/Hermann_von_Helmholtz)在1853年以及[Léon Charles Thévenin](https://en.wikipedia.org/wiki/L%C3%A9on_Charles_Th%C3%A9venin)在1883年分别独立提出.  
其内容为 **对于任何仅包含电压源，电流源和电阻的线性电网，都可以等效为一个电压源$U_{th}$与一个串联电阻$R_{th}$.**  
当然，电压源和电流源都是独立的 _（如果你不知道什么是**独立**电压、电流源的话，就当作是我上面写的那种，无论外界条件变化，电压源的电压永远不变，电流源的电流永远不变.）_  
关于戴维南定理的证明以及推导请自行了解，这玩意比较难以理解，所以我这边只把它当作工具使用  

废话了这么多，这定理能干什么？  
<img alt="Image" src=".\Images\4.svg">  
这是一个电路，而且还比较复杂，但它却只由电压源与电阻组成，所以它是在戴维南定理的适用范围之内的.  
那就可以通过某些魔法，把它变成一个电压源与一个串联电阻：  
<img alt="Image" src=".\Images\5.svg">   
先不说有没有用，反正十分赏心悦目  
问题来了，怎么施这个“魔法”呢？  
分为两步：  
- 计算等效电压源  
- 计算等效电阻  

#### 计算等效电压源

不分先后顺序，但我更喜欢先计算等效电压源.   
为了方便，我在电路图的节点上标了字母，若无特殊说明，电压测量的负极皆为GND节点  
<img alt="Image" src=".\Images\6.svg">    
_例如：$U_A$就是GND节点到A节点之间的电压，$U_{AB}$就是A节点到B节点之间的电压._  
接下来就是等效电压$U_{th}$计算过程：  
$U_{th}=U_D=U_B=\frac{U_A*R_B}{R_{AB}+R_B}=\frac{U_0(R_2+R_3)}{R_1+R_2+R_3}=\frac{1.5V*(1Ω+1Ω)}{2Ω+1Ω+1Ω}=0.75V$  

#### 计算等效电阻

接下来就该是等效电阻$U_{th}$，在计算等效电阻时，先要将电压源和电流源换算成电阻，而阻值就是其内阻.  
说人话就是用导线代替电压源，用开路代替电流源 _（听上去有些怪怪的但好像又没问题）_.  
所以原电路图就成了这个样子：
<img>
此时等效电阻$R_{th}=R_D$.  
这样计算起来就方便了，给出过程:

此时等效电压源$U_{th}$和等效电阻$R_{th}$都算出来了，那么其等效电路也就水落石出了.  

#### 动画回顾

用个动画回顾下全过程：

不过有人要问了：“你这示例都没出现电流源啊”，其实呢，因为R-2R没有电流源，我也就一笔带过了，还是那句话“以下所写的仅是是本文需要的知识，想要深入了解请自行查阅资料并学习”.  
当然，在实践中的话，一个万用表，一个计算器和一张草稿纸 ~~（足够聪慧的大脑也行）~~ ，就可以直接测量出结果，不用上面这么繁琐的步骤了，但精确度就一言难尽了.

## 构建推导
## 实际应用
## 回顾

## 版权相关
要复制请提供出处以及作者（作者就是我本人 **Anslate** ），不能商用.  
本文章的文字以及插图所有权归属于：Anslate Anslate2020@outlook.com.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">知识共享署名-非商业性使用 4.0 国际许可协议</a>进行许可.  