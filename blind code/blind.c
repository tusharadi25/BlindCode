#include<stdio.h>
#include<time.h>
#include<conio.h>
#include<windows.h>
void loading();
char name[50], dept[10];
void getdata();
void postdata();
																//just to set text color
void ClearConsoleToColors(int ForgC, int BackC){  
 WORD wColor = ((BackC & 0x0F) << 4) + (ForgC & 0x0F);
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD coord = {0, 0};
    DWORD count;
	CONSOLE_SCREEN_BUFFER_INFO csbi;
    SetConsoleTextAttribute(hStdOut, wColor);
    if(GetConsoleScreenBufferInfo(hStdOut, &csbi))
    {	FillConsoleOutputCharacter(hStdOut, (TCHAR) 32, csbi.dwSize.X * csbi.dwSize.Y, coord, &count);
		FillConsoleOutputAttribute(hStdOut, csbi.wAttributes, csbi.dwSize.X * csbi.dwSize.Y, coord, &count );
        SetConsoleCursorPosition(hStdOut, coord);
     }
}

void main ()
{  	int i, z;
	time_t sec1,sec2;
	FILE *tr;
	char x, ch;
    SetConsoleTitle("Blind Code - Transmission 2017 ");			//for title name
	ClearConsoleToColors(10,0);									// text-Green(15) background-Black(0)
	system("cls");
	getdata();  												//getting info of participant
	loading();													//just tp :P
	
	tr = fopen("code.c","w");
	printf("\n\tEnter The code:\n");
	sec1 = time(NULL);											//starting time
	sec2 = time(NULL);
	while(1)
	{	if((sec2-sec1)>300)
		{	printf("Time = 5min\n");
			break;
		}
		x=getch();
		sec2 = time(NULL);										//ending time
		if(x == 26 )											//for ending program before 5min
			break;
		if(x!= 26 )												//putting char in file
			putc(x,tr);
		
	}
	fclose(tr);
	getch();
	system("cls");
	postdata();
	printf("\n\nTime = %d min %d sec\n\n",(sec2-sec1)/60,(sec2-sec1)%60 );					//time used by participant
	system("gcc code.c -o trial");								//Compiling the code
	printf("\noutput:\n");
	system("trial");											//output if no error in code
	printf("\nDo you wan't to see code? (1/0) ");
	scanf("%d",&z);
	if(z)
	{	tr = fopen("code.c","r");
		if( tr == NULL )
		{	perror("Error while opening the file.\n");
			exit(EXIT_FAILURE);
		}
		printf("\ncode:\n");
		while( ( ch = fgetc(tr) ) != EOF )
			printf("%c",ch);
 		fclose(tr);
	}		
}


void loading()
{	time_t t1,t2;
	char c[]="aLOADING.....";
	char (*go[5])[]={"a","Get","set","Code","\a\a"};			//beap for starting typing 
	int i=1;
	system("cls");
	t1 = time(NULL);
	t2 = time(NULL);
	printf("\n\n\t");
	while(c[i]!='\0')
	{	t2 = time(NULL);
		if((t2-t1)==i)
			printf("%c",c[i++]);
	}
	system("cls");
	i=1;
	printf("\n\n\t");
	t1 = time(NULL);
	while(i<5)
	{	t2 = time(NULL);
		if((t2-t1)==i)
			printf(" %s",go[i++]);
	}
	system("cls");
}

void getdata()
{	printf("\nEnter name: ");
	scanf("%s",name);
	printf("Dept name: ");
	scanf("%s",dept);
}

void postdata()
{	printf("---Data collected by Volunteer---");
	printf("\nName : %s",name);
	printf("\nDept : %s", dept);	

}