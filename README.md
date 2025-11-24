# lbr_stack_doc
[![Documentation Status](https://readthedocs.org/projects/lbr-stack/badge/?version=latest)](https://lbr-stack.readthedocs.io/en/latest/?badge=latest) [![status](https://joss.theoj.org/papers/c43c82bed833c02503dd47f2637192ef/status.svg)](https://joss.theoj.org/papers/c43c82bed833c02503dd47f2637192ef)

This repository holds the documentation for the [LBR-Stack](https://github.com/lbr-stack).

## Build Documentation Locally
To build locally:
1. Clone this repository

    ```shell
    git clone --recursive git@github.com:lbr-stack/lbr_stack_doc.git
    cd lbr_stack_doc
    ```

2. Create a virtual environment

    ```shell
    python3 -m venv ./lbr_stack_doc_venv
    source lbr_stack_doc_venv/bin/activate
    ```

3. Install dependencies

    ```shell
    pip3 install -r requirements.txt
    ```

4. Clone the `lbr_fri_ros2_stack`, e.g. via (this uses [vcs](https://github.com/dirk-thomas/vcstool#how-to-install-vcstool))

    ```shell
    wget https://raw.githubusercontent.com/lbr-stack/lbr_fri_ros2_stack/jazzy/lbr_fri_ros2_stack/repos-fri-1.15.yaml
    vcs import doc/source < repos-fri-1.15.yaml
    ```

5. Clone `pyfri`

    ```shell
    git clone https://github.com/lbr-stack/pyfri.git doc/source/pyfri
    ```

6. In [conf.py](doc/source/conf.py) change

    ```python
    f"doxysphinx build . $READTHEDOCS_OUTPUT/html {doxyfile}", shell=True
    ```

    to 

    ```python
    f"doxysphinx build . html {doxyfile}", shell=True
    ```

7. Finally, go to [doc/source](doc/source/) and run

    ```shell
    python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . html
    ```

8. Open and browse the documentation by opening `doc/source/html/index.html`.

## Build Paper Locally
To build the [paper](paper/paper.md) via [Docker](https://joss.readthedocs.io/en/latest/submitting.html#docker), run

```shell
docker run --rm -it \
    -v $PWD:/data \
    -u $(id -u):$(id -g) \
    openjournals/inara \
    -o pdf,crossref,preprint \
    paper/paper.md
```

inside the `lbr_stack_doc` repository.

## Citation
If you enjoyed using this repository for your work, we would really appreciate ❤️ if you could leave a ⭐ and / or cite it, as it helps us to continue offering support.

```
@misc{huber2023lbrstack,
      title={LBR-Stack: ROS 2 and Python Integration of KUKA FRI for Med and IIWA Robots}, 
      author={Martin Huber and Christopher E. Mower and Sebastien Ourselin and Tom Vercauteren and Christos Bergeles},
      year={2023},
      eprint={2311.12709},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```

## Acknowledgements
<img src="https://www.kcl.ac.uk/newimages/Wellcome-EPSRC-Centre-medical-engineering-logo.xa827df3f.JPG?f=webp" alt="wellcome" height="45" width="65" align="left">

This work was supported by core and project funding from the Wellcome/EPSRC [WT203148/Z/16/Z; NS/A000049/1; WT101957; NS/A000027/1]. 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/1920px-Flag_of_Europe.svg.png" alt="eu_flag" height="45" width="65" align="left" >

This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 101016985 (FAROS project).
