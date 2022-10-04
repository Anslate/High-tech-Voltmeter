#include "reg51.h"
#include "intrins.h"
#include "BIN2HEX.h"
#define uchar unsigned char
	
sfr P0M1 = 0x93;
sfr P0M0 = 0x94;
sfr P1M1 = 0x91;
sfr P1M0 = 0x92;
sfr AUXR = 0x8E;
sfr AUXR1 = 0xA2;

uchar count = 0x00;//确定当前串口输入数值是P0还是P1

uchar M2L(uchar in){//因为设计失误，所以端序搞错了，写个函数纠正一下
	uchar i = 0x00;
	uchar out = 0x00;
	for(i=0;i<8;i++){
		out = out<<1;
		out = out|((in>>i)&0x01);
	}
	return out;
}

void UART1_Routine() interrupt 4{
	if(count){//P1
		uchar dat = SBUF;
		P1 = M2L(dat);
		RI = 0;
		count = 0x00;
	}
	else{//P0
		uchar dat = SBUF;
		P0 = M2L(dat);
		RI = 0;
		count = 0x01;
	}
}

void main(){//@35MHz
	//设为推挽输出
	P0M1 = b00000000;
	P0M0 = b11111111;
	P1M1 = b00000000;
	P1M0 = b11111111;
	//初始化串口
	SCON = 0x50;		//8位UART 115200bps
	IE = 0x90;      //启用串口中断
	IP = 0x10;      //串口中断设为最高优先级
	AUXR1 &= 0x7F;   //将串口设在2号位
	AUXR1 |= 0x40;
	AUXR |= 0x40;		//定时器时钟1T模式
	AUXR &= 0xFE;		//选择定时器1为波特率发生器
	TMOD &= 0x0F;		//设置定时器模式
	TL1 = 0xB4;		//设置定时初始值
	TH1 = 0xFF;		//设置定时初始值
	ET1 = 0;		//禁止定时器1中断
	TR1 = 1;		//定时器1开始计时
	
	P1=0xff;
	P0=0xff;
	while(1);
}