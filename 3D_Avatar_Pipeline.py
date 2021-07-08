#!/usr/bin/python

import os
import sys, getopt
import open3d as o3d
import pymeshlab
from glob import glob

#help usage
if(len(sys.argv)<2):
    print("Script Usage: python 3D_Avatar_Pipeline.py <input image location+file_name>")
    sys.exit(0)

#Visualize the generated mesh(.obj) using PIFuHD
def visualize(mesh):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

#remeshing using Quadric Error Metric Decimation by Garland and Heckbert
def remesh(mesh):
    return mesh.simplify_quadric_decimation(target_number_of_triangles=14000)

#<-------------Core Pipeline Begins-------------->

#read input argument
image_path = str(sys.argv[1])
filename = os.path.basename(image_path)
filename_raw = filename.rsplit(".",1)[0]
input_directory = os.path.dirname(image_path)
print('Input Image Path:', image_path)
print('Image Name:', filename)
print('Image Directory:', input_directory)
print('Image Raw name:', filename_raw)
#create directory for image
if not os.path.exists('./Results/'+filename_raw):
    os.mkdir('./Results/'+filename_raw)
output_directory = './Results/'+filename_raw
print('Output Directory:', output_directory)

#clean prior pose txt files
#os.system("rm "+input_directory+"\\*.txt")
for file in glob(input_directory+"\*.txt"):
    os.remove(file)

#TODO: pose estimation
print("Executing preprocessing - cropping and pose estimation")
exit_code = os.system("python preprocess_img_pose.py "+image_path)
if exit_code > 0:
    print("Error running preprocessing")
    sys.exit(exit_code)
os.system("cp ./input/"+filename_raw+"_rect.txt ./Results/"+filename_raw)

#execute pifuHD as a script
print("Executing PIFuHD")
exit_code = os.system("python -m pifuhd.apps.simple_test --use_rect -i "+input_directory+" -o "+output_directory+" -c ./Checkpoints/pifuhd/pifuhd.pt")
if exit_code > 0:
    print("Error running PIFuHD")
    sys.exit(exit_code)

#copy original mesh and rename
os.system("cp "+output_directory+"/pifuhd_final/recon/result_"+filename_raw+"_512.obj "+output_directory)
#if not os.path.exists(output_directory+"/"+filename_raw+"_ori.obj"):
#    os.rename(output_directory+"/result_"+filename_raw+"_512.obj", output_directory+"/"+filename_raw+"_ori.obj")
#mesh_filename.replace("result_"+filename_raw+"_512.obj", filename_raw+"_ori.obj")

#read generate mesh in open3D
mesh = o3d.io.read_triangle_mesh(output_directory+'/result_'+filename_raw+"_512.obj")
 #visualize original mesh
print("Visualizing Original Mesh")
visualize(mesh)

#reduce mesh using Quadratic mesh simplication - to 1k-5k vertices
#print("Remeshing using Quadratic Decimation")
#remesh = remesh(mesh)
#write out the re-meshed obj
#o3d.io.write_triangle_mesh("./Results/suriya_remesh.obj", remesh)

#reduce mesh using PyMeshLab
print("Remeshing using Simplification: Quadric Edge Collapse Decimation by MeshLab")
ms = pymeshlab.MeshSet()
ms.load_new_mesh(output_directory+'/result_'+filename_raw+"_512.obj")
ms.simplification_quadric_edge_collapse_decimation(targetfacenum = 14000)
ms.save_current_mesh(output_directory+'/'+filename_raw+'_remesh.obj')

#visualize remesh
remesh = o3d.io.read_triangle_mesh(output_directory+'/'+filename_raw+'_remesh.obj')
print("Visualizing Re-Mesh")
visualize(remesh)

#TODO: mesh cleaning

#execute RigNet as a script
print("Executing RigNet")
exit_code = os.system("python rignet_script.py "+filename_raw)
if exit_code > 0:
    print("Error running RigNet")
    sys.exit(exit_code)
