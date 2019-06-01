import helper
import random

# 任务1：在如下代码中，请写代码获得这些值：
# 1. 模拟环境的长和宽
# 2. 模拟环境中第3行第6列元素

# 模拟环境数据
env_data = helper.fetch_maze()

# 1模拟环境的行数
rows = len(env_data)

# 2模拟环境的列数
columns = len(env_data[0])

# 3取出模拟环境第三行第六列的元素
row_3_col_6 = env_data[2][5]

print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)


# 任务2：在如下代码中，请计算模拟环境中，第一行和第三列的障碍物个数。

# 0: 普通格子（可通行）
# 2: 障碍物（不可通行）
ordinary_mark = 0
barrier_mark = 2

# 4计算模拟环境中，第一行的的障碍物个数。
number_of_barriers_row1 = env_data[0].count(barrier_mark)

# 5计算模拟环境中，第三列的的障碍物个数。
number_of_barriers_col3 = [l[2] for l in env_data].count(barrier_mark)

print("迷宫中，第一行共有", number_of_barriers_row1, "个障碍物，第三列共有", number_of_barriers_col3, "个障碍物。")


# 任务3：在如下代码中：
# 1. 创建一个名为 loc_map 的字典，它有两个键值，分别为 start 和 destination，对应的值分别为起点和目标点的坐标，它们以如 (0,0) 的形式保存为元组。
# 2. 从字典中取出 start 对应的值，保存在 robot_current_loc 对应的变量中，这个变量表示小车现在的位置。

# 1: 机器人的起点（可通行）
# 3: 宝藏箱（目标点）
start_mark = 1
target_mark = 3


def find_row_col_index(mark, data):
    """
    根据节点值，寻找节点坐标
    :param mark: 节点值
    :param data: 模拟环境
    :return: 节点坐标
    """
    row_index = 0
    col_index = 0
    for mark_list in data:
        if mark in mark_list:
            col_index = mark_list.index(mark)
            break
        else:
            row_index += 1
    return row_index, col_index


# 6按照上述要求创建字典
loc_map = {'start': find_row_col_index(start_mark, env_data),
           'destination': find_row_col_index(target_mark, env_data)}

# 7保存机器人当前的位置
robot_current_loc = loc_map['start']


# 我们的机器人能够执行四个动作：向上走 u、向下走 d、向左走 l、向右走 r。
# 但是，由于有障碍，很多时候机器人的行动并不能成功。所以在这里，你需要实现一个函数，来判断机器人在某个位置，执行某个移动动作是否可行。
# 任务4：在下方代码中，实现名为 is_move_valid_special 的函数，它有两个输入，分别为机器人所在的位置坐标 loc，以及即将执行的动作 act，
# 如 (1,1) 及 u。接着它的返回是一个布尔值，表明小车在 loc 位置下，是否可以执行动作 act
def is_move_valid_special(loc, act):
    """
    判断机器人在某位置，是否可执行某动作
    :param loc: tuple，位置坐标
    :param act: string，动作标示
    :return: boolean，是否可执行
    """
    row_index = loc[0]
    col_index = loc[1]
    if 'u' == act:
        row_index -= 1
    elif 'd' == act:
        row_index += 1
    elif 'l' == act:
        col_index -= 1
    elif 'r' == act:
        col_index += 1
    else:
        print("unknown act:{}, please check the args", act)

    if row_index < 0 or row_index > len(env_data) - 1:
        return False
    if col_index < 0 or col_index > len(env_data[0]) - 1:
        return False
    if env_data[row_index][col_index] == barrier_mark:
        return False
    return True


# 任务5：在下方代码中，重新实现一个名为 `is_move_valid` 的函数，
# 它有三个输入，分别为模拟环境的数据 `env_data`、机器人所在的位置坐标 `loc`、以及即将执行的动作 `act`。
# 它的返回值与此前一样，是一个布尔值，表明小车在给定的虚拟环境中的 `loc` 位置下，是否可以执行动作 `act`。
def is_move_valid(env_data, loc, act):
    """
    判断机器人在某位置，是否可执行某动作
    :param env_data: list，模拟环境
    :param loc: tuple，位置坐标
    :param act: string，动作标示
    :return: boolean，是否可执行
    """
    row_index = loc[0]
    col_index = loc[1]
    if 'u' == act:
        row_index -= 1
    elif 'd' == act:
        row_index += 1
    elif 'l' == act:
        col_index -= 1
    elif 'r' == act:
        col_index += 1
    else:
        print("unknown act:{}, please check the args", act)

    if row_index < 0 or row_index > len(env_data) - 1:
        return False
    if col_index < 0 or col_index > len(env_data[0]) - 1:
        return False
    if env_data[row_index][col_index] == barrier_mark:
        return False
    return True

# 任务6：请回答：
#
# 在任务4及任务5中的实现的两个函数中，env_data 这个变量有什么不同？
# 调用is_move_valid函数，参数为env_data_、loc_、act_，如果在函数内修改env_data是否会改变env_data_的值？为什么？
# 提示：可以尝试从变量作用域的角度回答该问题1。
# 问题1，答：任务4的函数中的env_data为全局变量，任务5的函数中的env_data为传递参数变量，是局部变量

# 提示：可以尝试从可变类型变量和不可变类型变量的角度回答该问题2。
# 问题2，答：会，list是可变类型，函数中的传参是传递引用，所以改变env_data会修改env_data_的值。
#          如果是非可变类型，那么是传递值，等于复制了一份给函数使用，如int，string等等


# 任务7：编写一个名为 valid_actions 的函数。
# 它有两个输入，分别为虚拟环境的数据 env_data，以及机器人所在的位置 loc，输出是一个列表，表明机器人在这个位置所有的可行动作。

def valid_actions(env_data, loc):
    """
    获取机器人所在位置的所有可行动作列表
    :param env_data: list, 模拟环境
    :param loc: tuple, 机器人所在的位置 loc
    :return: list, 机器人在这个位置所有的可行动作列表
    """
    action_list = ['u', 'd', 'l', 'r']
    return [action for action in action_list if is_move_valid(env_data, loc, action)]


# 任务8：编写一个名为 move_robot 的函数，它有两个输入，分别为机器人当前所在的位置 loc 和即将执行的动作 act。
# 接着会返回机器人执行动作之后的新位置 new_loc
def move_robot(loc, act):
    """
    移动机器人，返回移动后的新位置
    :param loc: tuple, 机器人所在位置
    :param act: string, 移动动作
    :return: tuple, 移动后的新位置
    """
    if is_move_valid(env_data, loc, act):
        if 'u' == act:
            return loc[0] - 1, loc[1]
        elif 'd' == act:
            return loc[0] + 1, loc[1]
        elif 'l' == act:
            return loc[0], loc[1] - 1
        elif 'r' == act:
            return loc[0], loc[1] + 1
        else:
            print("unknown act:{}, please check the args", act)
    else:
        # 如果不能移动，则返回原位置
        return loc


# 任务9：编写一个名为 random_choose_actions 的函数，它有两个输入，分别为虚拟环境的数据 env_data，以及机器人所在的位置 loc。
# 机器人会执行一个300次的循环，每次循环，他会执行以下任务：
#
# 利用上方定义的 valid_actions 函数，找出当前位置下，机器人可行的动作；
# 利用 random 库中的 choice 函数，从机器人可行的动作中，随机挑选出一个动作；
# 接着根据这个动作，利用上方定义的 move_robot 函数，来移动机器人，并更新机器人的位置；
# 当机器人走到终点时，输出“在第n个回合找到宝藏！”。
# 提示：如果机器人无法在300个回合内找到宝藏的话，试试看增大这个数字，也许会有不错的效果 :P

def do_random_choose(round_num, loc, target):
    """
    随机选择机器人移动动作，可传递执行回合数
    :param round_num: int, 回合数
    :param loc: tuple, 机器人位置
    :param target: void，无返回
    :return:
    """
    loc_now = loc
    for step in range(round_num):
        if loc_now == target:
            print("在第{}个回合找到宝藏！".format(step + 1))
            break
        else:
            valid_action_list = valid_actions(env_data, loc_now)
            action = random.choice(valid_action_list)
            loc_now = move_robot(loc_now, action)
            print("robot现在在位置{}, 回合{}".format(loc_now, step + 1))

def random_choose_actions(env_data, loc):
    """
    随机选择机器人移动动作，尝试达到目标找到宝藏
    :param env_data: list，模拟环境
    :param loc: tuple, 机器人位置
    :return: void，无返回
    """
    target = find_row_col_index(target_mark, env_data)
    do_random_choose(300, loc, target)
    do_random_choose(1000, loc, target)


# 任务10：尝试实现一个算法，能够对给定的模拟环境，输出机器人的行动策略，使之能够走到终点。

def cal_f_path(start, target):
    """
    由于该robot只支持单格上下左右移动，距离一致，所以A*算法的距离F=G(某点到上下左右距离均为1)+H，只需要计算H即可
    :param start: tuple, 开始位置
    :param target: tuple, 终点位置
    :return: int, 路径长度值
    """
    return abs(target[0] - start[0]) + abs(target[1] - start[1])


def find_min_f_node(node_list, target):
    """
    寻找队列中f路径值最小的节点
    :param node_list: list, 节点列表
    :param target: tuple, f路径要到达的节点
    :return: tuple, f路径最小节点
    """
    f_path_list = [cal_f_path(node, target) for node in node_list]
    return node_list[f_path_list.index(min(f_path_list))]


def valid_action_node(env_data, loc):
    """
    寻找当前位置可移动的节点
    :param env_data: list, 模拟环境
    :param loc: tuple, 当前位置
    :return: list, 可移动节点
    """
    valid_node_list = []
    valid_action_list = valid_actions(env_data, loc)
    for valid_action in valid_action_list:
        if 'u' == valid_action:
            valid_node_list.append((loc[0] - 1, loc[1]))
        elif 'd' == valid_action:
            valid_node_list.append((loc[0] + 1, loc[1]))
        elif 'l' == valid_action:
            valid_node_list.append((loc[0], loc[1] - 1))
        elif 'r' == valid_action:
            valid_node_list.append((loc[0], loc[1] + 1))
    return valid_node_list


def act_between_nodes(node1, node2):
    """
    查询节点1到节点2的移动动作
    :param node1: tuple, 节点1坐标
    :param node2: tuple, 节点2坐标
    :return: string, 'u'/'d'/'l'/'r'
    """
    row_cal = node2[0] - node1[0]
    col_cal = node2[1] - node1[1]
    if row_cal == -1 and col_cal == 0:
        return 'u'
    if row_cal == 1 and col_cal == 0:
        return 'd'
    if row_cal == 0 and col_cal == -1:
        return 'l'
    if row_cal == 0 and col_cal == 1:
        return 'r'
    return 'unknown action!'


def reach_destination_quickly(env_data):
    """
    快速寻找宝藏
    :param env_data: list, 模拟环境
    :return: void, 返回空
    """
    start_node = find_row_col_index(start_mark, env_data)
    target_node = find_row_col_index(target_mark, env_data)
    open_list = []
    close_list = []
    node_path = []
    act_path = []
    from_node = ()

    open_list.append(start_node)
    while True:
        min_f_node = find_min_f_node(open_list, target_node)
        node_path.append(min_f_node)
        # from_node空则跳过判定
        if from_node:
            act_path.append(act_between_nodes(from_node, min_f_node))

        open_list.remove(min_f_node)
        close_list.append(min_f_node)
        if min_f_node == target_node:
            # 到达终点
            break

        # 存在valid_action_node中，并且不在close_list和open_list中, 才准备加入open_list
        node_list_to_append_open = [node for node in valid_action_node(env_data, min_f_node)
                                    if node not in close_list and node not in open_list]
        open_list += node_list_to_append_open
        from_node = min_f_node

    print("起点为:{}, 终点为:{}".format(start_node, target_node))
    print("预测路径为:{}".format(node_path))
    print("预测动作:{}".format(act_path))
    if node_path[-1] == target_node:
        print("预测动作可寻找到宝藏位置:{}".format(node_path[-1]))

reach_destination_quickly(env_data)
