### 从0开始给服务器装机和配置docker：


安装linux各种必要的包

    sudo apt install -y apt-transport-https ca-certificates htop curl software-properties-common unzip wget axel make build-essential libcurl4-openssl-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev cmake wget curl llvm libncurses5-dev git net-tools pkg-config libncursesw5-dev libgdbm-dev libdb5.3-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev

安装 pyenv

	git clone https://gitee.com/mirrors/pyenv.git ~/.pyenv

防止服务器的系统盘爆掉，设置软连接：ln -s /home/ronald/develop /data/ronald/develop/ 将D盘的内容挂载到C盘。

安装cuda驱动，可以到nvidia官网下载确保对应显卡的型号
cuda_10.2.89_440.33.01_linux.run

重启服务器

	sudo reboot

加速nvidia-smi：

	sudo nvidia-smi -pmi
	nvidia-smi

运行

	docker-run-all.sh
