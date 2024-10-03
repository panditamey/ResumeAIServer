# Resume AI Server

This project sets up a Dockerized application for Resume AI, running on port 5000, with Nginx configured as a reverse proxy.

## Setup Instructions

### 1. Update and Install Docker

```bash
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker $USER
```

### 2. Configure Firewall

```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw status
```

### 3. Clone the Project and Build the Docker Image

```bash
mkdir ~/projects
cd ~/projects
sudo git clone https://github.com/panditamey/ResumeAIServer.git
cd ResumeAIServer
sudo docker build -t resume-ai-server .
```

### 4. Run the Docker Container

```bash
sudo docker run -d -p 5000:5000 --name resume-ai-server-instance-1 resume-ai-server
```

### 5. Install and Configure Nginx

```bash
sudo apt install nginx
```

Edit the Nginx configuration:

```bash
sudo nano /etc/nginx/sites-available/default
```

Add the following configuration:

```nginx
server {
    listen 80;

    server_name your_domain_or_ip;

    location /resumeai-api/ {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 6. Test and Restart Nginx

```bash
sudo nginx -t
sudo systemctl restart nginx
```

Alternatively, reload Nginx:

```bash
sudo nginx -s reload
```
