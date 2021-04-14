# Novel-view-generation
## Description about the project  
This project is the implementation of a [**novel view systhesis**](./Project-report:Novel-view-generation.pdf) which aims to generate/systhesize a target view with an arbitrary camera pose from a given source view and its camera pose as shown in figure below[1].

<p align="center">
    <img src="./assets/overarch.png" width="512"/>
</p>

## Overarch of the proposed method
<p align="center">
    <img src="./assets/final_block_diagram_labelled.png" width="1000"/>
</p>

## Requirements  
- Python 3.x
- [Open3D](https://pypi.org/project/open3d-python/)
- [OpenCV](https://docs.opencv.org/master/d2/de6/tutorial_py_setup_in_ubuntu.html)
- [Matplotlib](https://pypi.org/project/matplotlib/)
- [Pillow](https://pypi.org/project/Pillow/)
- [NumPy](http://www.numpy.org/)
- [MATLAB](https://in.mathworks.com/products/matlab.html)

## Usage  

### Generating a novel view from scratch
Calibrate the camera
```bash
$ python calibrate.py
```
Then to generate the point cloud
```bash
$ python disparity1.py
```

After this, the point cloud is generated, which needs to be transformed(rotated to the target view). To do this, head over to MATLAB, and run the [pcd_transformation.m](./pcd_transformation.m)  
You now have the transformed point cloud of the target view.  
This point cloud further needs to be projected to 2D. To do this,  
```bash
$ python 3D_to_2D_open3d_part2.py
``` 
After the point cloud is rendered to 2D, a respective mask needs to be generated to perform Inpainting  

```bash
$ python mask_generator.py
```
```bash
$ python Inpainting.py
```

After this stage, we now have the inpainted image, which is the target view of the given input image.   



References   
[1] Multi-view to Novel View: Synthesizing Novel Views with Self-Learned Confidence,Sun, Shao-Hua et. al.,2018]  
