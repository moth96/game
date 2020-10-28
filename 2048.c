#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define X 4
#define Y 4

//打印2048游戏
void print_game(int array[X][Y])
{
    printf("---------------------------------\n");
    for (int j = 0; j < Y; j++)
    {
        printf("|");
        if ( array[0][j] )
        {
            printf("%d\t", array[0][j]);
        }
        else
        {
            printf("\t");
        }
    }
    printf("|\n");
    printf("---------------------------------\n");
    for (int j = 0; j < Y; j++)
    {
        printf("|");
        if (array[1][j])
        {
            printf("%d\t", array[1][j]);
        }
        else
        {
            printf("\t");
        }
    }
    printf("|\n");
    printf("---------------------------------\n");
    for (int j = 0; j < Y; j++)
    {
        printf("|");
        if (array[2][j])
        {
            printf("%d\t", array[2][j]);
        }
        else
        {
            printf("\t");
        }
    }
    printf("|\n");
    printf("---------------------------------\n");
    for (int j = 0; j < Y; j++)
    {
        printf("|");
        if (array[3][j])
        {
            printf("%d\t", array[3][j]);
        }
        else
        {
            printf("\t");
        }
    }
    printf("|\n");
    printf("---------------------------------\n");
}
//初始化数组
void init_array(int array[X][Y])
{
    for (int i = 0; i < X; i++)
    {
        for (int j = 0; j < Y; j++)
        {
            array[i][j] = 0;
        }
    }
    srand((unsigned)time(NULL));
    for (int k = 0; k < 3; k++)
    {

        int i = rand() % 4;
        int j = rand() % 4;
        array[i][j] = ((rand() % 2) + 1) * 2;
    }
}

//判断数组是否已满
//如果满了 返回 0 否则 返回 正数
int isfilled(int array[X][Y])
{
    int num = 0;
    for (int i = 0; i < X; i++)
    {
        for (int j = 0; j < Y; j++)
        {
            if (!array[i][j])
            {
                num++;
            }
        }
    }
    return num;
}

//操作结束后，更新数组，在 0 处加入随机的 2 和 4 
void update_array(int array[X][Y])
{
    srand((unsigned)time(NULL));
    int k = 1;
    while (k)
    {
        int i = rand() % 4;
        int j = rand() % 4;
        if (!array[i][j])
        {
            array[i][j] =  ((rand() % 2) + 1) * 2;
            k--;
        }
    }
}

//顺时针转置 num 次矩阵, 用于进行 w a s d 操作
//当为 a 时 num = 0
//当为 s 时 num = 1
//当为 d 时 num = 2
//当为 w 时 num = 3
void array_trans(int array[X][Y], int num)
{
    while(num--)
    {
        int temp[X][Y];
        for (int i = 0; i < X; i++)
        {
            for (int j = 0; j < Y; j++)
            {
                temp[i][j] = array[i][j];
            }
        }
        for (int i = 0; i < X; i++)
        {
            for (int j = 0; j < Y; j++)
            {
                array[i][j] = temp[Y-1-j][i];
            }
        }
    }
}

//根据 w a s d 命令对数字进行加减
void add_num(int array[X][Y])
{
    for (int i = 0; i < X; i++)
    {
        int cal[4] = {0, 0, 0, 0};
        int k = 0;
        for (int j = 0; j < Y; j++)
        {
            //将所有非 0 元素移动到左侧
            if (array[i][j])
            {
                cal[k] = array[i][j];
                k++;
            }
        }
        if (cal[0] == cal[1])
        {
            cal[0] += cal[1];
            if (cal[2] == cal[3])
            {
                cal[1] = cal[2] + cal[3];
                cal[2] = cal[3] = 0;
            }
            else
            {
                cal[1] = cal[2];
                cal[2] = cal[3];
                cal[3] = 0;
            }
        }
        else
        {
            if (cal[1] == cal[2])
            {
                cal[1] += cal[2];
                cal[2] = cal[3];
                cal[3] = 0;
            }
            else
            {
                if (cal[2] == cal[3])
                {
                    cal[2] += cal[3];
                    cal[3] = 0;
                }
            }
        }
        for (int j = 0; j < Y; j++)
        {
            array[i][j] = cal[j];
        }
    }
}

//根据 w a s d 命令移动
void move(int array[X][Y])
{
    print_game(array);
    printf("请输入命令(WASD):\n");
    char order;
    scanf("%c", &order);
    getchar();
    switch (order)
    {
    case 'A':
        add_num(array);
        break;
    case 'S':
        array_trans(array, 1);
        add_num(array);
        array_trans(array, 3);
        break;
    case 'D':
        array_trans(array, 2);
        add_num(array);
        array_trans(array, 2);
        break;
    case 'W':
        array_trans(array, 3);
        add_num(array);
        array_trans(array, 1);
        break;
    default:
        break;
    }
    update_array(array);
}


int main()
{
    int array[X][Y];
    init_array(array);
    while(isfilled(array))
    {
        move(array);
    }
    printf("游戏结束\n");
    return 0;
}
