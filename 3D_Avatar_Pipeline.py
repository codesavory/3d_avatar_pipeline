#!/usr/bin/python

import os
import sys, getopt

#Visualize the generated mesh(.obj) using PIFuHD
import open3d as o3d
def visualize(mesh):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

#remeshing using Quadric Error Metric Decimation by Garland and Heckbert
def remesh(mesh):
    return mesh.simplify_quadric_decimation(target_number_of_triangles=14000)

#TODO: pose estimation

#execute pifuHD as a script
print("Executing PIFuHD")
os.system("python -m pifuhd.apps.simple_test --use_rect -i ./pifuhd/sample_images -o ./pifuhd/results -c ./pifuhd/checkpoints/pifuhd.pt")

#read generate mesh in open3D
mesh = o3d.io.read_triangle_mesh("./pifuhd/results/pifuhd_final/recon/result_IMG_3392.2_512.obj")
 #visualize original mesh
print("Visualizing Original Mesh")
visualize(mesh)

#reduce mesh using Quadratic mesh simplication - to 1k-5k vertices
#print("Remeshing using Quadratic Decimation")
#remesh = remesh(mesh)
#write out the re-meshed obj
#o3d.io.write_triangle_mesh("./Results/suriya_remesh.obj", remesh)

#reduce mesh using PyMeshLab
import pymeshlab
print("Remeshing using Simplification: Quadric Edge Collapse Decimation by MeshLab")
ms = pymeshlab.MeshSet()
ms.load_new_mesh('./pifuhd/results/pifuhd_final/recon/result_IMG_3392.2_512.obj')
ms.simplification_quadric_edge_collapse_decimation(targetfacenum = 14000)
ms.save_current_mesh('./Results/suriya_remesh.obj')
#visualize remesh
remesh = o3d.io.read_triangle_mesh("./Results/suriya_remesh.obj")
print("Visualizing Re-Mesh")
visualize(remesh)

#TODO: mesh cleaning

#execute RigNet as a script
print("Executing RigNet")
os.system("python ./RigNet/quick_start.py")
