# simple-app
 
## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
  - [Docker Deployment](#docker-deployment)
  - [Kubernetes Deployment](#kubernetes-deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description
simple Area App python program do the following  -The user is asked for an area type -if  't' for triangle ,'r' for rectangle , 'c' for Circle ,'s' for Square -user can choise , 1 : For Try Again , 2 : For Exit From App -problems will be triangle , rectangle , Circle and Square
![image](https://github.com/soliman141119/simple-app/assets/72981030/ede46364-5379-4234-8a38-c9e599536e20)

### Docker Deployment

1. Clone the repository:

   ```bash
   git clone https://github.com/soliman141119/simple-app.git
2. Navigate to the project directory:
    ```bash
   cd project
4. Build the Docker image:
    ```bash
   docker image build -t < username docker hub >/smiple area  .
6. Check that image is existed:
    ```bash
   docker images
    ```
   ![image](https://github.com/soliman141119/simple-app/assets/72981030/19ec882d-9319-48cd-b7d4-832ee27c83e0)
8. Make tag for image like :
    ```bash
   docker tag < username docker hub >/smiple-area < username docker hub >/smiple-area:v1
10. Run the Docker container:
```bash
   docker container run -it soliman14/area-app
```
![image](https://github.com/soliman141119/simple-app/assets/72981030/ede46364-5379-4234-8a38-c9e599536e20)
12. login on docker hub  account
 ```bash
   docker login -u < username docker hub >
```
13. for upload or push image on docker hub repo
   ```bash
  docker push < username docker hub >/area-app:v1
   ```
  https://hub.docker.com/repository/docker/soliman14/smiple-area/general
### Kubernetes Deployment
1. Ensure you have a Kubernetes cluster set up and configured.
2. Apply the Kubernetes deployment YAML:
    ```bash
   kubectl apply -f  k8s-deploy-app.yaml
4. Verify the deployment:
```bash
  kubectl get deployments
  kubectl get pods
  kubectl get services

   


   
