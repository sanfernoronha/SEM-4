#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<GL/glut.h>


void ellipse(){
    glBegin(GL_POINTS);
    float x1, y1, p1, p2, rx, ry, x, y;
    printf("Enter Rx\n");
    scanf("%f", &rx);
    printf("Enter Ry\n");
    scanf("%f", &ry);
    printf("Enter center of ellipse\n");
    scanf("%f%f", &x1, &y1);
    x = 0;
    y = ry;
    p1 = (ry*ry) - (rx*rx)*ry + (rx*rx)*(1/4);

    do{
        glVertex2f(x1 + x, y1 + y);
        glVertex2f(x1 - x,y1 + y);
        glVertex2f(x1 - x,y1 - y);
        glVertex2f(x1 + x,y1 - y);

        if(p1 < 0){
            x = x + 1;
            p1 = p1 + 2*(ry*ry)*x + (ry*ry);
        }
        else{
            x = x + 1;
            y = y - 1;
            p1 = p1 + 2*(ry*ry)*x - 2*(rx*rx)*y + (ry*ry);
        }

    }while(2*(ry*ry)*x < 2*(rx*rx)*y);

    p2 = (ry*ry)*(x + 0.5)*(x + 0.5) + (rx*rx)*(y-1)*(y-1) -(rx*rx)*(ry*ry);
    do{
        glVertex2f(x1 + x, y1 + y);
        glVertex2f(x1 - x,y1 + y);
        glVertex2f(x1 - x,y1 - y);
        glVertex2f(x1 + x,y1 - y);

        if(p2 <= 0){
            x = x + 1;
            y = y - 1;
            p2 = p2 - 2*(rx*rx)*y + (rx*rx) + 2*(ry*ry)*x;
        }
        else{
            y = y - 1;
            p2 = p2 - 2*(rx*rx)*y + (rx*rx);
        }
    }while(y > 0);


    glEnd();
}

void disp()
{
    glClearColor(1,1,1,1);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0,0,0);
    ellipse();//Call function
    glFlush();
}


int main(int argv,char **argc)
{
    glutInit(&argv,argc);
    glutInitWindowSize(300,300);
    glutCreateWindow("window");
    gluOrtho2D(0,300,0,300);
    glutDisplayFunc(disp);
    glutMainLoop();
    return 0;
}
