# Selenium Crawler

## 1. installation and configuration 

https://www.itread01.com/content/1543109607.html

linux condition:

    pip install selenium

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb

IF error cause lack of dependency:

    sudo apt-get install -f

install chrome driver:

    wget https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver
    sudo mv chromedriver /usr/bin/

if error status code 127:

    sudo apt-get install libnss3-dev
    sudo apt-get install libgconf-2-4

## 2. crawlers

https://blog.51cto.com/xsboke/2352856

wait for a while during crawling can handle the situation of ajax web page 

    opt = webdriver.ChromeOptions()          # 创建chrome对象
    opt.add_argument('--no-sandbox')          # 启用非沙盒模式,linux必填,否则会报错:(unknown error: DevToolsActivePort file doesn't exist)......
    opt.add_argument('--disable-gpu')          # 禁用gpu，linux部署需填，防止未知bug
    opt.add_argument('headless')          # 把chrome设置成wujie面模式，不论windows还是linux都可以，自动适配对应参数
    driver = webdriver.Chrome(executable_path=r'/root/chromedriver',options=opt)    # 指定chrome驱动程序位置和chrome选项
    driver.get('https://baidu.com')          # 访问网页
    time.sleep(5)           # 等待5秒
    content = driver.page_source 