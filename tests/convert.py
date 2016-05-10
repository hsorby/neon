
import os
import json


node_ids = []
points = {}
plane_attitudes = {"0": node_ids}
node_planes = {}
point_cloud = {'_basic_points': points, '_plane_attitudes': plane_attitudes, '_nodes': node_planes}

with open('d:/work/data/femur_pointcloud_part.exlike') as f:
    lines = f.readlines()
    while lines:
        node_id = lines.pop(0)[7:].rstrip()
        x = float(lines.pop(0).rstrip())
        y = float(lines.pop(0).rstrip())
        z = float(lines.pop(0).rstrip())
        node_ids.append(int(node_id))
        node_planes[node_id] = 0
        points[node_id] = [x, y, z]

with open('d:/work/data/test.node_state.json', 'w') as o:
    json.dump(point_cloud, o)



