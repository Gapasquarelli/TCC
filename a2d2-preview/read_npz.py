from os.path import join
import glob
import numpy as np

# get the list of files in lidar directory
file_name = "20180807145028_lidar_frontcenter_000000091.npz"

# select the lidar point clo
# read the lidar data
lidar_front_center = np.load(file_name)

print(list(lidar_front_center.keys()))

# get the point cloud
'''col = lidar_front_center['col']
print(col.shape)
print(col[0:10])

row = lidar_front_center['row']
print(row.shape)
print(row[0:10])

lidar_id = lidar_front_center['lidar_id']
print(lidar_id.shape)
print(lidar_id[0:10])'''

'''points = lidar_front_center['points']
print(points.shape)
print(points[0:10])

col = lidar_front_center['col']
print(col.shape)
print(col[0:10])

row = lidar_front_center['row']
print(row.shape)
print(row[0:10])

depth = lidar_front_center['depth']
print(depth.shape)
print(depth[0:10])

distance = lidar_front_center['distance']
print(distance.shape)
print(distance[0:10])

azimuth = lidar_front_center['azimuth']
print(azimuth.shape)
print(azimuth[0:10])'''


reflectance = lidar_front_center['reflectance']
print(reflectance.shape)
print(reflectance[0:10])