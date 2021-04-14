import open3d as o3d

point_cloud = o3d.io.read_point_cloud("/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/reconstructed_rotated_h.ply", format="ply")
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.get_render_option().point_color_option = o3d.visualization.PointColorOption.Color
vis.get_render_option().point_size = 3.0
vis.add_geometry(point_cloud)
vis.capture_screen_image("/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/2D_image_converted_rotated2.jpg", do_render=True)
