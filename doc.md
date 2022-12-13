```bash
# enable the firewall, set port 20 and 80 are the only ports allowed on the network, then check the status of the network.
sudo ufw enable
sudo ufw allow 20/tcp
sudo ufw allow 80/tcp
sudo ufw status
```
![image](https://user-images.githubusercontent.com/39824083/207233069-118fb797-cf95-4807-b148-1b134afda57a.png)

```bash
# Install webserver nginx and access the webserver show the web page that you created.
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```
![image](https://user-images.githubusercontent.com/39824083/207233987-7e141f7a-2393-452b-a826-ea533f25c662.png)

```bash
# get the ip address
ip a
```
![image](https://user-images.githubusercontent.com/39824083/207249356-ef44dd43-42e1-43e2-9261-207b14a22b08.png)
![image](https://user-images.githubusercontent.com/39824083/207250893-a341af9a-a94c-40c5-a15b-4e29e7ca4cf7.png)

```bash

```
