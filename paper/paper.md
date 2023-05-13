---
title: 'LBR FRI ROS 2 Stack: Lightweight FRI ROS 2 Interface'
tags:
  - C++
  - Python
  - ROS 2
  - KUKA LBR Med
  - KUKA LBR IIWA
  - Hard Real-time
header-includes:
  - \usepackage{pifont}
  - \newcommand{\cmark}{\ding{51}}
  - \newcommand{\xmark}{\ding{55}}
authors:
  - name: Martin Huber
    orcid: 0000-0003-4603-6773
    corresponding: true
    affiliation: 1
  - name: Christopher E. Mower
    orcid: 0000-0002-3929-9391
    affiliation: 1
  - name: Sebastien Ourselin
    orcid: 0000-0002-5694-5340
    affiliation: 1
  - name: Tom Vercauteren
    orcid: 0000-0003-1794-0456
    equal-contrib: true
    affiliation: 1
  - name: Christos Bergeles
    orcid: 0000-0002-9152-3194
    equal-contrib: true
    affiliation: 1
affiliations:
 - name: School of Biomedical Engineering and Image Sciences, King's College London, United Kingdom
   index: 1
date: 12 May 2023
bibliography: paper.bib
---


# Summary
The `LBR FRI ROS 2 Stack` is a collection of packages that integrate the `KUKA LBR iiwa7/14` and `KUKA LBR Med7/14` robots into the Robot Operating System (ROS) and ROS 2 ecosystem. The `LBR FRI ROS 2 Stack` supports the Gazebo simulation [@gazebo] as well as communication to the real robots. It is designed for mission critical hard real-time applications and operates through KUKA's Fast Robot Interface (FRI) [@fri]. Following packages are provided:

- **lbr_bringup**: Python library for launching the different components.
- **lbr_description**: Description files for the `iiwa7/14` and `Med7/14` robots.
- **lbr_demos**: Demonstrations for simulation and the real robots.
- **lbr_fri_msgs**: Interface Definition Language (IDL) equivalent of FRI protocol buffers.
- **lbr_fri_ros2**: FRI ROS 2 interface through `realtime_tools` [@ros_control].
- **lbr_hardware_interface**:  `ros2_control` [@ros2_control]
- **lbr_moveit_config**:

- **fri**

<!-- [@ros2] -->

<!-- 
KUKA channels and un-modified client side source code
designed for stream-lined research to production

It is built on top of the Fast Robot Interface (FRI) [@fri] -->

<!-- - **lbr_fri_ros2_stack_doc** -->

# Statement of need


| Framework       | iiwa | Med | ROS | ROS 2  | RT | FRIs | Pos | Imp | Cart Imp | HW IF  | 
| --------------- | ---- |---- | --- | ------ | -- | ---- | --- | --- | -------- | ------ |
|[lbr_fri_ros2_stack](https://github.com/kCL-BMEIS/lbr_fri_ros2_stack)             | \bullet | \bullet | \bullet | \bullet | \bullet | \bullet | \bullet | \bullet | \bullet | \bullet |
| [iiwa_ros](https://github.com/epfl-lasa/iiwa_ros)                                | \bullet |         | \bullet |         | \bullet |         | \bullet | \bullet |         | \bullet |
| [iiwa_ros2](https://github.com/ICube-Robotics/iiwa_ros2)                         | \bullet |         |         | \bullet | \bullet |         | \bullet | \bullet |         | \bullet |
| [iiwa-stack](https://github.com/IFL-CAMP/iiwa_stack)                             | \bullet |         | \bullet |         |         | N/A     | \bullet | \bullet | \bullet |         |
| [libiiwa](https://github.com/Toni-SM/libiiwa)                                    | \bullet |         | \bullet | \bullet |         | N/A     | \bullet | \bullet | \bullet |         |
| [KST-KUKA-Sunrise-Toolbox](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox) |         |         |         |         |         | N/A     |         |         |         |         |

Table: Overview of existing frameworks for interfacing the KUKA LBRs. A square indicates support for the respective feature. List of abbreviations: Real-time (**RT** ), Position (**Pos**), Impedance (**Imp**), Cartesian Impedance (**Cart Imp**), Hardware Interface (**HW IF**). 

libiiwa: [@libiiwa]
iiwa_ros: [@iiwa_ros]
KST-KUKA-Sunrise-Toolbox: [@kuka_sunrise_toolbox]
iiwa_ros2: [@iiwa_ros2]
iiwa_stack: [@iiwa_stack]
fri: [@fri]

# Acknowledgement
This work was supported by core and project funding from the Wellcome/EPSRC [WT203148/Z/16/Z; NS/A000049/1; WT101957; NS/A000027/1]. This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 101016985 (FAROS project).

# References