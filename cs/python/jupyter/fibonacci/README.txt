sudo apt update
sudo apt install python3-pip python3-dev

sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

mkdir ~/my_project_dir
cd ~/my_project_dir

#virtualenv my_project_env
virtualenv cs

source my_project_env/bin/activate

Seu prompt deverá mudar para indicar que você agora está operando em um ambiente virtual Python. Agora, você verá em seu prompt de comando algo parecido com isto: (my_project_env)user@host:~/my_project_dir$.

(my_project_env)sammy@your_server:~/my_project_dir$ pip install jupyter

(my_project_env)sammy@your_server:~/my_project_dir$ jupyter notebook



O tunelamento SSH pode ser feito executando o seguinte comando SSH em uma nova janela de terminal local:

$ ssh -L 8888:localhost:8888 your_server_username@your_server_ip

$ ssh -L 8888:localhost:8888 sammy@203.0.113.0


(my_project_env)sammy@your_server:~/my_project_dir$ jupyter notebook




