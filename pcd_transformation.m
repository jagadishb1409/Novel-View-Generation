%reading and displaying a point cloud
pcd = pcread('/home/lucciffer/WORK/Machine Learning/CVG/novel-view-generation/camera_perspective_warp/outputs/reconstructed_human2.ply')
figure;
pcshow(pcd)
xlabel('X')
ylabel('Y')
zlabel('Z')

%transform the point cloud 45 deg along Z-axis
% n = input('Enter the rotation value: ')
theta = pi/10;
% rot = [cos(theta) sin(theta) 0; ...
%       -sin(theta) cos(theta) 0; ...
%                0          0  1];

rot_y = [ cos(theta)      0  sin(theta); ... 
                   0      1           0; ...
          -sin(theta)     0  cos(theta)];

trans = [0, 0, 0];
tform = rigid3d(rot_y,trans);

%transform the point cloud 
pcd_out = pctransform(pcd, tform);
% xyz = readXYZ(pcd_out);
pcwrite(pcd_out,'outputs/reconstructed_rotated_h','PLYFormat','binary');
figure;
pcshow(pcd_out)
xlabel('X')
ylabel('Y')
zlabel('Z')


%rendering point cloud to image
% I = pointcloud2image( 0.21977945, -1.19558152,  0.0024334, 250, 250 );
% figure;  
% imshow(I,[]);

