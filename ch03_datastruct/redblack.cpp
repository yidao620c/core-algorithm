#include <iostream>
using namespace std;

#define BLACK 0
#define RED 1

//红黑树结点结构
struct node
{
        node *left;
        node *right;
        node *p;
        int key;
        bool color;
        node(node *init, int k):left(init),right(init),p(init),key(k),color(BLACK){}
};
//红黑树结构
class Red_Black_Tree
{
public:
        node *root;//根结点
        node *nil;//哨兵
        Red_Black_Tree(){nil = new node(NULL, -1);root = nil;};
        //13.2旋转
        void Left_Rotate(node *x);
        void Right_Rotate(node *x);
        //13.3插入
        void RB_Insert_Fixup(node *z);
        void RB_Insert(node *z);
        //13.4删除
        void RB_Delete_Fixup(node *x);
        node *RB_Delete(node *z);
        //else
        void Print();
        void Print(node *x);
        node *RB_Search(node *x, int k);
        node *Tree_Successor(node *x);
        node *Tree_Minimum(node *x);
};
//左旋，令y = x->right, 左旋是以x和y之间的链为支轴进行旋转
//涉及到的结点包括：x,y,y->left，令node={p,l,r},具体变化如下：
//x={x->p,x->left,y}变为{y,x->left,y->left}
//y={x,y->left,y->right}变为{x->p,x,y->right}
//y->left={y,y->left->left,y->left->right}变为{x,y->left->left,y->left->right}
void Red_Black_Tree::Left_Rotate(node *x)
{
        //令y = x->right
        node *y = x->right;
        //按照上面的方式修改三个结点的指针，注意修改指针的顺序
        x->right = y->left;
        if(y->left != nil)
                y->left->p = x;
        y->p = x->p;
        if(x->p == nil)//特殊情况：x是根结点
                root = y;
        else if(x == x->p->left)
                x->p->left = y;
        else
                x->p->right = y;
        y->left = x;
        x->p = y;
}
//右旋，令y = x->left, 左旋是以x和y之间的链为支轴进行旋转
//旋转过程与上文类似
void Red_Black_Tree::Right_Rotate(node *x)
{
        node *y = x->left;
        x->left = y->right;
        if(y->right != nil)
                y->right->p = x;
        y->p = x->p;
        if(x->p == nil)
                root = y;
        else if(x == x->p->right)
                x->p->right = y;
        else
                x->p->left = y;
        y->right = x;
        x->p = y;
}
//红黑树调整
void Red_Black_Tree::RB_Insert_Fixup(node *z)
{
        node *y;
        //唯一需要调整的情况，就是违反性质2的时候，如果不违反性质2，调整结束
        while(z->p->color == RED)
        {
                //p[z]是左孩子时，有三种情况
                if(z->p == z->p->p->left)
                {
                        //令y是z的叔结点
                        y = z->p->p->right;
                        //第一种情况，z的叔叔y是红色的
                        if(y->color == RED)
                        {
                                //将p[z]和y都着为黑色以解决z和p[z]都是红色的问题
                                z->p->color = BLACK;
                                y->color = BLACK;
                                //将p[p[z]]着为红色以保持性质5
                                z->p->p->color = RED;
                                //把p[p[z]]当作新增的结点z来重复while循环
                                z = z->p->p;
                        }
                        else
                        {
                                //第二种情况：z的叔叔是黑色的，且z是右孩子
                                if(z == z->p->right)
                                {
                                        //对p[z]左旋，转为第三种情况
                                        z = z->p;
                                        Left_Rotate(z);
                                }
                                //第三种情况：z的叔叔是黑色的，且z是左孩子
                                //交换p[z]和p[p[z]]的颜色，并右旋
                                z->p->color = BLACK;
                                z->p->p->color = RED;
                                Right_Rotate(z->p->p);
                        }
                }
                //p[z]是右孩子时，有三种情况，与上面类似
                else if(z->p == z->p->p->right)
                {
                        y = z->p->p->left;
                        if(y->color == RED)
                        {
                                z->p->color = BLACK;
                                y->color = BLACK;
                                z->p->p->color = RED;
                                z = z->p->p;
                        }
                        else
                        {
                                if(z == z->p->left)
                                {
                                        z = z->p;
                                        Right_Rotate(z);
                                }
                                z->p->color = BLACK;
                                z->p->p->color = RED;
                                Left_Rotate(z->p->p);
                        }
                }
        }
        //根结点置为黑色
        root->color = BLACK;
}
//插入一个结点
void Red_Black_Tree::RB_Insert(node *z)
{
        node *y = nil, *x = root;
        //找到应该插入的位置，与二叉查找树的插入相同
        while(x != nil)
        {
                y = x;
                if(z->key < x->key)
                        x = x->left;
                else
                        x = x->right;
        }
        z->p = y;
        if(y == nil)
                root = z;
        else if(z->key < y->key)
                y->left = z;
        else
                y->right = z;
        z->left = nil;
        z->right = nil;
        //将新插入的结点转为红色
        z->color = RED;
        //从新插入的结点开始，向上调整
        RB_Insert_Fixup(z);
}
//对树进行调整，x指向一个红黑结点，调整的过程是将额外的黑色沿树上移
void Red_Black_Tree::RB_Delete_Fixup(node *x)
{
        node *w;
        //如果这个额外的黑色在一个根结点或一个红结点上，结点会吸收额外的黑色，成为一个黑色的结点
        while(x != root && x->color == BLACK)
        {
                //若x是其父的左结点（右结点的情况相对应）
                if(x == x->p->left)
                {
                        //令w为x的兄弟，根据w的不同，分为三种情况来处理
                        //执行删除操作前x肯定是没有兄弟的，执行删除操作后x肯定是有兄弟的
                        w = x->p->right;
                        //第一种情况：w是红色的
                        if(w->color == RED)
                        {
                                //改变w和p[x]的颜色
                                w->color = BLACK;
                                x->p->color = RED;
                                //对p[x]进行一次左旋
                                Left_Rotate(x->p);
                                //令w为x的新兄弟
                                w = x->p->right;
                                //转为2.3.4三种情况之一
                        }
                        //第二情况：w为黑色，w的两个孩子也都是黑色
                        if(w->left->color == BLACK && w->right->color == BLACK)
                        {
                                //去掉w和x的黑色
                                //w只有一层黑色，去掉变为红色，x有多余的一层黑色，去掉后恢复原来颜色
                                w->color = RED;
                                //在p[x]上补一层黑色
                                x = x->p;
                                //现在新x上有个额外的黑色，转入for循环继续处理
                        }
                        //第三种情况，w是黑色的,w->left是红色的,w->right是黑色的
                        else
                        {
                                if(w->right->color == BLACK)
                                {
                                        //改变w和left[x]的颜色
                                        w->left->color = BLACK;
                                        w->color = RED;
                                        //对w进行一次右旋
                                        Right_Rotate(w);
                                        //令w为x的新兄弟
                                        w = x->p->right;
                                        //此时转变为第四种情况
                                }
                                //第四种情况：w是黑色的,w->left是黑色的,w->right是红色的
                                //修改w和p[x]的颜色
                                w->color =x->p->color;
                                x->p->color = BLACK;
                                w->right->color = BLACK;
                                //对p[x]进行一次左旋
                                Left_Rotate(x->p);
                                //此时调整已经结束，将x置为根结点是为了结束循环
                                x = root;
                        }
                }
                //若x是其父的左结点（右结点的情况相对应）
                else if(x == x->p->right)
                {
                        //令w为x的兄弟，根据w的不同，分为三种情况来处理
                        //执行删除操作前x肯定是没有兄弟的，执行删除操作后x肯定是有兄弟的
                        w = x->p->left;
                        //第一种情况：w是红色的
                        if(w->color == RED)
                        {
                                //改变w和p[x]的颜色
                                w->color = BLACK;
                                x->p->color = RED;
                                //对p[x]进行一次左旋
                                Right_Rotate(x->p);
                                //令w为x的新兄弟
                                w = x->p->left;
                                //转为2.3.4三种情况之一
                        }
                        //第二情况：w为黑色，w的两个孩子也都是黑色
                        if(w->right->color == BLACK && w->left->color == BLACK)
                        {
                                //去掉w和x的黑色
                                //w只有一层黑色，去掉变为红色，x有多余的一层黑色，去掉后恢复原来颜色
                                w->color = RED;
                                //在p[x]上补一层黑色
                                x = x->p;
                                //现在新x上有个额外的黑色，转入for循环继续处理
                        }
                        //第三种情况，w是黑色的,w->right是红色的,w->left是黑色的
                        else
                        {
                                if(w->left->color == BLACK)
                                {
                                        //改变w和right[x]的颜色
                                        w->right->color = BLACK;
                                        w->color = RED;
                                        //对w进行一次右旋
                                        Left_Rotate(w);
                                        //令w为x的新兄弟
                                        w = x->p->left;
                                        //此时转变为第四种情况
                                }
                                //第四种情况：w是黑色的,w->right是黑色的,w->left是红色的
                                //修改w和p[x]的颜色
                                w->color =x->p->color;
                                x->p->color = BLACK;
                                w->left->color = BLACK;
                                //对p[x]进行一次左旋
                                Right_Rotate(x->p);
                                //此时调整已经结束，将x置为根结点是为了结束循环
                                x = root;
                        }
                }
        }
        //吸收了额外的黑色
        x->color = BLACK;
}
//找最小值
node *Red_Black_Tree::Tree_Minimum(node *x)
{
    //只要有比当前结点小的结点
        while(x->left != nil)
        x = x->left;
    return x;
}
//查找中序遍历下x结点的后继，后继是大于key[x]的最小的结点
node *Red_Black_Tree::Tree_Successor(node *x)
{
    //如果有右孩子
        if(x->right != nil)
        //右子树中的最小值
        return Tree_Minimum(x->right);
    //如果x的右子树为空且x有后继y，那么y是x的最低祖先结点，且y的左儿子也是
    node *y = x->p;
    while(y != NULL && x == y->right)
    {
        x = y;
        y = y->p;
    }
    return y;
}
//递归地查询二叉查找树
node *Red_Black_Tree::RB_Search(node *x, int k)
{
    //找到叶子结点了还没找到，或当前结点是所查找的结点
        if(x->key == -1 || k == x->key)
        return x;
    //所查找的结点位于当前结点的左子树
    if(k < x->key)
        return RB_Search(x->left, k);
    //所查找的结点位于当前结点的左子树
    else
        return RB_Search(x->right, k);
}
//红黑树的删除
node *Red_Black_Tree::RB_Delete(node *z)
{
        //找到结点的位置并删除，这一部分与二叉查找树的删除相同
        node *x, *y;
        if(z->left == nil || z->right == nil)
                y = z;
        else y = Tree_Successor(z);
        if(y->left != nil)
                x = y->left;
        else x = y->right;
        x->p = y->p;
        if(y->p == nil)
                root = x;
        else if(y == y->p->left)
                y->p->left = x;
        else
                y->p->right = x;
        if(y != z)
                z->key = y->key;
        //如果被删除的结点是黑色的，则需要调整
        if(y->color == BLACK)
                RB_Delete_Fixup(x);
        return y;
}
void Red_Black_Tree::Print(node *x)
{
        if(x->key == -1)
                return;
        Print(x->left);
        cout<<x->key<<' '<<x->color<<endl;
        Print(x->right);
}
void Red_Black_Tree::Print()
{
        Print(root);
        cout<<endl;
}

