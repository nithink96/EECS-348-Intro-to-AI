int queue[MAP_WIDTH*MAP_HEIGHT][2];
int path_x[MAP_HEIGHT][MAP_WIDTH];
int path_y[MAP_HEIGHT][MAP_WIDTH];
bool dfs_recursive( int **map, int y, int x)
{
      bool flag,path;
//	printf("%d %d ", y,x);
      if(y<0 || x<0 || y>= MAP_HEIGHT || x>= MAP_WIDTH || map[y][x] == 1 || map[y][x] == 4 )
          flag = false;
      else
      {
          if(map[y][x] == 3)
          {
            map[y][x] = 5;
            flag = true;
          }
	else
	{

          map[y][x] = 4;
          if(dfs_recursive(map, y, x + 1) || dfs_recursive(map, y + 1, x) || dfs_recursive(map, y, x - 1) || dfs_recursive(map, y - 1, x))  
	{
            map[y][x] = 5;
            flag = true;
          }
          else
            flag = false;
        }
      }
        return flag;
}
bool df_search(int **map)
{
        bool found = false;
        int x,y,i,j = 0;
        // PUT YOUR CODE HERE
        // access the map using "map[y][x]"
        // y between 0 and MAP_HEIGHT-1
        // x between 0 and MAP_WIDTH-1
        for( i=0; i<MAP_HEIGHT; i++)
        {       
        	 for( j = 0; j<MAP_WIDTH; j++)
                 {       
   			 if(map[i][j] == 2)
                         {
				 y = i; x = j;                                       
                          }                                                                                                                                                                                                   }
	}
     found = dfs_recursive(map, y, x);
	printf("%d ", found);      
      	return found;
}                                                                                                                                  
		
void enqueue(int y, int x, int &front, int &rear)
{	
	if(front == -1 || rear == -1)
		front = rear = 0;
	else
		rear = rear + 1;
	queue[rear][0] = y;
	queue[rear][1] = x;

}
void dequeue(int &y, int &x, int &rear, int &front)
{	
	
//	parent = front;
	y = queue[front][0];
	x = queue[front][1];
	if(front == rear)
		front = rear = -1;
	else
		front = front + 1;

}
	
bool bf_search(int **map)
{
	bool found = false;
	int x,y,i,j = 0;
	int start_x,start_y;
	// PUT YOUR CODE HERE
	// access the map using "map[y][x]"
	// y between 0 and MAP_HEIGHT-1
	// x between 0 and MAP_WIDTH-1
	 for( i=0; i<MAP_HEIGHT; i++)
        {
                for( j = 0; j<MAP_WIDTH; j++)
                {
                        if(map[i][j] == 2)
                        {
                                y = i; x = j;
				start_y = i; start_x = j;			
                        }
                }
        }
	int front, rear;
	queue[0][0] = y;
	queue[0][1] = x;
	front = 0; rear = 0; i = 0;
	int new_x,new_y;
	while(front != -1 && rear!= -1 && front <= rear && rear < MAP_HEIGHT*MAP_WIDTH)
	{	
		int parent_id = rear;
		dequeue(y, x, rear, front);
		if(map[y][x] == 3)
		{
			found = true;	
			new_x = x; new_y = y;
			while(!(start_y ==  y ))
			{	
				y = new_y; x = new_x;
				map[y][x] = 5;	
				new_y = path_y[y][x];
				new_x = path_x[y][x];
			} 
			break;
		}
		
		else
		{
			map[y][x] = 4;
			if(!(y<0 || x+1<0 || y>= MAP_HEIGHT || x+1>=MAP_WIDTH || map[y][x+1] == 1 || map[y][x+1] == 4))
			{
				enqueue(y, x+1, front, rear);
				path_y[y][x+1] = y;
				path_x[y][x+1] = x;			
			}		
			if(!(y+1<0 || x<0 || y+1>= MAP_HEIGHT || x>=MAP_WIDTH || map[y+1][x] == 1 || map[y+1][x] == 4))
			{
				enqueue(y+1, x, front, rear);
				path_y[y+1][x] = y;  
                                path_x[y+1][x] = x;
			
			}
			if(!(y<0 || x-1<0 || y>= MAP_HEIGHT || x-1>=MAP_WIDTH || map[y][x-1] == 1 || map[y][x-1] == 4))
			{
				 enqueue(y, x-1, front, rear);
				path_y[y][x-1] = y;  
                                path_x[y][x-1] = x;	
			}
			if(!(y-1<0 || x<0 || y-1>= MAP_HEIGHT || x>=MAP_WIDTH || map[y-1][x] == 1 || map[y-1][x] == 4))
		        {
			         enqueue(y-1, x, front, rear);
				path_y[y-1][x] = y;  
                                path_x[y-1][x] = x;
			}	
		}
		
	}
	
	
				
	return found;
}
