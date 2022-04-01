# ML

## Docker Notes

### Build (from folder in install/ directory)
```
sudo docker build -t myproject install/ -f install/Dockerfile
```

### Run GPU w/ [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
```
sudo docker run --gpus all -u $(id -u):$(id -g) -v $(pwd):/tf -it --rm -p 8888:8888 projectname
```

### Run and share files in Windows
```
docker run -v ${PWD}:/tf -it --rm -p 8888:8888 projectname
```
