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
# Install and configure the required packages for two-factor authentication using google authenticator pam module
sudo apt install libpam-google-authenticator
sudo pico /etc/pam.d/sshd
# add the following line to the end of the file
auth required pam_google_authenticator.so
# save and exit
# restart the sshd service
sudo systemctl restart sshd.service
# configure the sshd service to use google authenticator
sudo pico /etc/ssh/sshd_config
# find the line that says "ChallengeResponseAuthentication no" and change it to "ChallengeResponseAuthentication yes"
# save and exit
# restart the sshd service
sudo systemctl restart sshd.service
# configure the google authenticator
google-authenticator
```
![image](https://user-images.githubusercontent.com/39824083/207256931-02557dbf-65aa-4858-ab55-46c59d03d84b.png)
![image](https://user-images.githubusercontent.com/39824083/207258033-fde4c51e-ee1d-4008-a961-7ca9b827d962.png)
![image](https://user-images.githubusercontent.com/39824083/207258712-d2586c18-6294-434a-92ed-88b0c5304a0c.png)

![image](https://user-images.githubusercontent.com/39824083/207258880-cfdb29d1-e812-4ad4-91d9-717a5de55f7b.png)
![image](https://user-images.githubusercontent.com/39824083/207260161-8b165587-dbe6-4f90-8a3f-4389af40d2cf.png)
![1670919843442](https://user-images.githubusercontent.com/39824083/207264865-08ed6f48-cc05-4237-8291-663ac9f7cc33.JPEG)
