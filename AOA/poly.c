#include<stdio.h>
#include<malloc.h>
#include<conio.h>
struct node
{
    int num;
    int coeff;
    struct node *next;
}


struct node START1=NULL;
struct node START2=NULL;
struct node START3=NULL;
struct node START4=NULL;
struct node LAST1=NULL;
struct node *create_poly(struct node*);
struct node *display_poly(struct node*);
struct node *add_poly(struct node*,struct node*);
struct node *sub_poly(struct node*,struct node*);
struct node *add_node(struct node*,int,int);

int main()
{
    int option;
    do
    {
        printf("1. enter the first polynomial \n");
        printf("2. display the first polynomial \n");
        printf("3. enter the second polynomial \n");
        printf("4. display the second polynomial \n");
        printf("5. add the polynomials \n");
        printf("6. display the results \n \n");
        printf("7. subtract the polynomials \n");
        printf("8. display the result \n");
        printf("enter your option \n");
        scanf("%d",&option);
        switch(option)
        {
            case 1:
            START1=create_poly(START1);
            break;
            case 2:
            START1=display_poly(START1);
            break;
            case 3:
            START2=create poly(START2);
            break;
            case 4:
            START2=display_poly(START2);
            break;
            case 5:
            START3=add_poly(START3);
            break;
            case 6:
            START3=display_poly(START3);
            break;
            case 7:
            START4=sub_poly(START4);
            break;
            case 8:
            START4=display_poly(START4);
            break;
        }

    }while(option!=9);

    return 0;
}

struct node *create_poly(struct node *START)
{
    struct node=new_node, *ptr;
    int n,c;
    printf("enter the number: \n");
    scanf("%d",&n);
    printf("enter the coefficient \n");
    scanf("%d",&c);
    while(n!=-1)
    {
        if(START==NULL)
        {
            new_node=(struct node *)malloc(sizeof(struct node));
            new_node->num=n;
            new_node->coeff=c;
            new_node->next=NULL;
            START=new_node;
        }

        else{
            ptr=START;
            while(ptr->next!=NULL)
            ptr=ptr->next;
            new_node=(struct node *)malloc(sizeof(struct node));
            new_node->num=n;
            new_nodw->coeff=c;
            new_node->next=-NULL;
            ptr->next=new_node;
        }
    printf("enter the number: \n");
    scanf("%d",&n);
    if(n==-1)
    break;
    printf("enter its coeffiecient \n");
    scanf("%d",&c);
    }
    return START;
}

struct node *display_poly(struct node *START)
{
    struct node *ptr;
    ptr=START;
    while(ptr!=NULL)
    {
        printf("%d x %d \t",ptr->num,ptr->coeff);
        ptr=ptr->next;
    }
    return START;
}

struct node add_poly(struct node *START1,struct node *START2,,struct node*START3)
{
struct node *ptr1,*ptr2;
int sum_num,c;
ptr1=START1,ptr2=START2;
while(ptr1!=NULL &&ptr2!=NULL)
{
    if(ptr1->coeff==ptr2->coeff)
    {
        sum_num=ptr1->num+ptr2->num;
        START2=add_node(START3,sum_num,ptr1->coeff);
        ptr1=ptr1->next;
        ptr2=ptr2->next;
    }
    else if(ptr1->coeff > ptr2->coeff)
    {
        START3=add_node(START3,ptr1->num,ptr1->coeff);
        ptr1=ptr1->next;
    }
    else if(ptr1->coeff < ptr2->coeff)
    {
       START3=add_node(START3,ptr2->num,ptr2->coeff); 
       ptr2=ptr2->next;
    }
}
if(ptr1==NULL)
{
    while(ptr2!=NULL)
    {
        START3=add_node(START3,ptr2->num,ptr2->coeff); 
       ptr2=ptr2->next;
    }
}
if(ptr2==NULL)
{
    while(ptr1!=NULL)
    {
     START3=add_node(START3,ptr1->num,ptr1->coeff);
        ptr1=ptr1->next;
    }
}
return START3;
}


struct node sub_poly(struct node *START1,struct node *START2,struct node *START4)
{
    struct node *ptr1,*ptr2;
int sub_num,c;
ptr1=START1,ptr2=START2;
do
{
    if(ptr1->coeff==ptr2->coeff)
    {
        sub_num=ptr1->num-ptr2->num;
        START2=add_node(START4,sub_num,ptr1->coeff);
        ptr1=ptr1->next;
        ptr2=ptr2->next;
    }
    else if(ptr1->coeff > ptr2->coeff)
    {
        START4=add_node(START4,ptr1->num,ptr1->coeff);
        ptr1=ptr1->next;
    }
    else if(ptr1->coeff < ptr2->coeff)
    {
       START4=add_node(START4,ptr2->num,ptr2->coeff); 
       ptr2=ptr2->next;
    }

}
while(ptr1!=NULL || ptr2!=NULL);
if(ptr1==NULL)
{
    while(ptr2!=NULL)
    {
        START4=add_node(START4,ptr2->num,ptr2->coeff); 
       ptr2=ptr2->next;
    }
}
if(ptr2==NULL)
{
    while(ptr1!=NULL)
    {
     START4=add_node(START4,ptr1->num,ptr1->coeff);
        ptr1=ptr1->next;
    }
}
return START4;

}

struct node add_node(struct node *START,int n,int c)
{
    struct node *ptr,*new_node;
    if(START==NULL)
    {
        new_node=(struct node *)malloc(sizeof(struct node));
        new_node->num=n;
        new_node->coeff=c;
        new_node->next=NULL;
        START=new_node;
    }
    else{
        ptr=START;
        while(ptr->next!=NULL)
        ptr=ptr->next;
        new_node=(struct node *)malloc(sizeof(struct node));
        new_node->num=n;
        new_node->coeff=c;
        new_node->next=NULL;
        START=new_node;
    }
    return START;
    }

}


/* OUTPUT
1.enter the first polynomial 
2. display the first polynomial 
3. enter the second polynomial
4. display the second polynomial
5. add the polynomials
6. display the results 
7. subtract the polynomials 
8. display the result
enter your option
1
enter the number
6
enter its coefficient
2
enter the number
5
enter the coefficient
1
enter the number
-1
enter your option
2
6x2 5x1
*/