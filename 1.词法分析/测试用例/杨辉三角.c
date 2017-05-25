#include<stdio.h>
3main() {
	int i,j,n=0,a[17][17]= {0};
	while(n<1 || n>16) {
		printf("请输入杨辉三角形的行数:");
		scanf("%d",&n);
	}