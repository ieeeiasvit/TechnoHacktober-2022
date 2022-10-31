// Implementation of BFS and DFS in C

#include<stdio.h>
#include<conio.h>

struct node
{
	int vertex;
	struct node* next;
};

struct z
{
	int r, f;
	int data[100];
};

struct node* g[20];
int n;
int visited[100];

void creategraph();
void insert(int vi, int vj);
void bfs(int i);
void dfs(int i);
void enquee(struct z*, int);
int dequee(struct z*);
int empty(struct z*);
int full(struct z*);

void main()
{
	printf("**** DFS and BFS ****\n");
	int i, choice;
	char c;
	do
	{
		printf("1.Create a Graph\n2.DFS\n3.BFS\n4.Quit");
		printf("\nEnter your choice : ");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			creategraph();
			break;
		case 2:
			for (i = 0; i < n; i++)
				visited[i] = 0;
			printf("\nEnter the start node : ");
			scanf(" %c", &c);
			i = (int)c - 64;
			printf("\nDFS : \n");
			dfs(i);
			printf("\n\n");
			break;
		case 3:
			printf("\nEnter the start node : ");
			scanf(" %c", &c);
			i = (int)c - 64;
			printf("\nBFS : \n");
			bfs(i);
			printf("\n\n");
			break;

		}
	} while (choice != 4);
}

void creategraph()
{
	int vi, vj, no;

	printf("\nEnter the no. of vertices : ");
	scanf("%d", &n);
	for (int counter = 0; counter < n; counter++)
		g[counter] = NULL;

	printf("\nEnter the no. of edges : ");
	scanf("%d", &no);
	printf("\n");
	for (int counter = 0; counter < no; counter++)
	{
		char v1, v2;
		printf("Enter the edge(u,v) :\n");
		scanf(" %c %c", &v1, &v2);
		vi = (int)v1 - 64;
		vj = (int)v2 - 64;
		insert(vi, vj);
		insert(vj, vi);
	}
	printf("\n");
}

void insert(int vi, int vj)
{
	struct node* p;
	struct node* q;
	q = (struct node*)malloc(sizeof(struct node));
	q->vertex = vj;
	q->next = NULL;

	if (g[vi] == NULL)
		g[vi] = q;
	else
	{
		p = g[vi];
		while (p->next != NULL)
			p = p->next;
		p->next = q;
	}
}

void dfs(int i)
{
	struct node* p;
	char v;
	p = g[i];
	visited[i] = 1;
	v = (char)(i + 64);
	printf("%c\t", v);
	while (p != NULL)
	{
		i = p->vertex;
		if (!visited[i])
			dfs(i);
		p = p->next;
	}
}

void bfs(int v)
{
	int i, w;
	char t;
	struct z x;
	struct node* p;
	x.r = x.f = -1;
	for (i = 0; i < n; i++)
		visited[i] = 0;
	enquee(&x, v);
	t = (char)(v + 64);
	printf("%c\t", t);
	visited[v] = 1;
	while (!empty(&x))
	{
		v = dequee(&x);
		for (p = g[v]; p != NULL; p = p->next)
		{
			w = p->vertex;
			if (visited[w] == 0)
			{
				char t;
				enquee(&x, w);
				visited[w] = 1;
				t = (char)(w + 64);
				printf("%c\t", t);
			}
		}
	}
}

int empty(struct z* p)
{
	if (p->r == -1 && p->f == -1)
		return(1);
	return(0);
}

int full(struct z* p)
{
	if (p->r == 100 - 1)
		return(1);
	return(0);

}

void enquee(struct z* p, int x)
{

	if (p->r == -1)
	{
		p->r = p->f = 1;
	}
	else
		p->r = p->r + 1;
	p->data[p->r] = x;
}

int dequee(struct z* p)
{
	int x;
	x = p->data[p->f];
	if (p->f == p->r)
		p->r = p->f = -1;
	else
		p->f = p->f + 1;
	return(x);
}