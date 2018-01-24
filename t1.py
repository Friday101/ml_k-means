'''
Porject:K-means
Date:2018-1-24 10:44
Auther:Friday_13
'''
import random
import matplotlib.pyplot as plt
import math
def cal_dis(dataset,center_point,color_script):
    k = len(center_point)
    cu = {}
    for i in range(k):
        cu[i] = []
    for point in dataset:
        min_dis = float('inf')
        for i in range(k):
            dis = math.sqrt(pow(point[0]-center_point[i][0],2)+pow(point[1]-center_point[i][1],2))
            if(dis < min_dis):
                min_dis = dis
                flag = i
        cu[flag].append(point)

    avg_x = 0.0
    avg_y = 0.0
    new_center_point = []
    for i in range(k):
        avg_x = 0.0
        avg_y = 0.0
        for x,y in cu[i]:
            avg_x += x
            avg_y += y


        avg_x = avg_x/len(cu[i])
        avg_y = avg_y/len(cu[i])
        new_center_point.append([avg_x,avg_y])

    flag = False # stop
    for i in range(k):
        if  new_center_point[i] not in center_point:
            flag = True # continue
            break


    for i in range(k):
        draw(cu[i],color_script,i)
    plt.show()

    return flag,new_center_point


def kmeans(dataset, k,color_script):
    center_point = []
    for i in range(k):
        center_point.append(generate_random_point())
    i = 0
    flag = True
    while i < 20 and flag == True:
        flag,center_point = cal_dis(dataset,center_point,color_script)
        i+=1



def draw(dataset,color_script,i):
    x_ = [x for (x, y) in dataset]
    y_ = [y for (x, y) in dataset]
    colors = ['b','g','r','c','m','y','k','w']
    markers = ['.',',','o','v','^','<','>','1']
    plt.scatter(x_,y_,marker=markers[color_script[i]],color = colors[color_script[i]],label=str(i))


def generate_random_point():
    data = []
    i = 0
    data.append(random.uniform(0, 5))
    data.append(random.uniform(0, 5))
    return data

if __name__ == '__main__':
    k = 5#k-means
    dataset = []
    i = 0
    while i < 50:
        dataset.append(generate_random_point())
        i+=1
    #draw(dataset)
    color_script = random.sample(range(8), k)
    kmeans(dataset,k,color_script)
