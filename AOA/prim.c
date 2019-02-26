#include<stdio.h>
#include<stdlib.h>
#define SIZE 10

typedef struct queue
{
	int a[SIZE];
	int front;
	int rear;
}que;

int adj[SIZE][SIZE]={0};

void create_graph(int n)
{
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      adj[i][j] = 1000;
    }
  }
	int s, d, e, i, j, w;
	for(i=0; i<n; i++)
	{
		printf("Enter number edges for %d\n", i);
		scanf("%d", &e);
		for(j=0; j<e; j++)
		{
      printf("Enter destination\n");
			scanf("%d", &d);
      printf("Enter weight\n");
      scanf("%d", &w);
			if(w < adj[i][d]){
				adj[i][d]=w;
			}
			if(i == d){
				adj[i][d] = 0;
			}
		}
	}
}

void testgraph(int n)
{
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      adj[i][j] = 1000;
    }
  }
	adj[0][1] = 3;
	adj[0][5] = 5;
	adj[0][4] = 6;
	adj[1][0] = 3;
	adj[5][0] = 5;
	adj[4][0] = 6;

	adj[1][2] = 1;
	adj[1][5] = 4;
	adj[2][1] = 1;
	adj[5][1] = 4;

	adj[2][3] = 6;
	adj[2][5] = 4;
	adj[3][2] = 6;
	adj[5][2] = 4;

	adj[3][5] = 5;
	adj[3][4] = 8;
	adj[5][3] = 5;
	adj[4][3] = 8;

	adj[4][5] = 2;
	adj[5][4] = 2;
}

void display_adjmat(int n)
{
    int i,j;
    printf("Adjacency matrix is\n");
           for(i=0; i<n; i++)
           {
               for(j=0; j<n; j++)
               {
                   printf(" %d ", adj[i][j]);
               }
               printf("\n");
           }
}


void disp_arr(int arr[], int n, int src){
  int i;
  for(i = 0; i < n; i++){
		if(i == src){
			printf("src ");
		}
		else{
			printf("%d ", arr[i]);
		}
  }
  printf("\n");
}

void display(int pred[], int dist[], int n, int src){
  int i, j, sum = 0;
  printf("\nDistance array is\n");
  disp_arr(dist, n, src);
  printf("Predecessor array is\n");
  disp_arr(pred, n, src);
  printf("\n");
  for(i = 0; i < n; i++){
    if(i == src){
      printf("%d is source node\n", i);
      continue;
    }
    printf("\nFor vertex %d\n", i);
    printf("%d ", i);
    j = i;
    while(pred[j] != src){
      j = pred[j];
      printf("<-%d ", j);
    }
    printf("<-%d ", src);
    printf("\n");
    sum = sum + dist[i];
  }
	printf("Total weight of the graph is %d\n", sum);
}

void prim(int n){
  int src, mindx, mjndx, min, check = 1, i, j;
  int dist[SIZE] = {1000};
  int pred[SIZE] = {0};
  int visited[SIZE] = {0};
  printf("Enter source node\n");
  scanf("%d", &src);
  visited[src] = 1;
  while(check){
		min = 1000;
		mindx = 0;
		mjndx = 0;
		for(i = 0; i < n; i++){
			if(visited[i] == 1){
				for(j = 0; j < n; j++){
					if(visited[j] == 0 && adj[i][j] < min){
						min = adj[i][j];
						mindx = i;
						mjndx = j;
					}
				}
			}
		}
		pred[mjndx] = mindx;
		dist[mjndx] = min;
		visited[mjndx] = 1;
		for(i = 0; i < n; i++){
      if(visited[i] == 1){
        check = 0;
      }
      else{
        check = 1;
				break;
      }
    }
  }
  display(pred, dist, n, src);
}

void main(){
  int n;
  printf("Enter number of vertices\n");
  scanf("%d", &n);
  create_graph(n);
}

/*
Enter number of vertices
4
Enter number edges for 0
4
Enter destination
0
Enter weight
4
Enter destination
1
Enter weight
2
Enter destination
2
Enter weight
2
Enter destination
2
Enter weight
7
Enter number edges for 1
3
Enter destination
3
Enter weight
5
Enter destination
2
Enter weight
1
Enter destination
0
Enter weight
2
Enter number edges for 2
5
Enter destination
0
Enter weight
2
Enter destination
0
Enter weight
7
Enter destination
1
Enter weight
1
Enter destination
3
Enter weight
3
Enter destination
3
Enter weight
8
Enter number edges for 3
3
Enter destination
1
Enter weight
5
Enter destination
2
Enter weight
3
Enter destination
2
Enter weight
8
Enter source node
0

Distance array is
src 2 1 3
Predecessor array is
src 0 1 2

0 is source node

For vertex 1
1 <-0
Total distance to vertex 1 is 2

For vertex 2
2 <-1 <-0
Total distance to vertex 2 is 3

For vertex 3
3 <-2 <-1 <-0
Total distance to vertex 3 is 6
*/
