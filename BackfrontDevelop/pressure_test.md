# Pressure test

## Python Locust

    with open('../test/check_list.txt', 'r') as file:
        check_list = file.readlines()
    
    class QuickstartUser(HttpUser):
        wait_time = between(1, 2)




    @task(1)
    def test_post(self):

        word = 'bags'
        body_dict = {"source": "en","target": "zh","word": word}
        body = json.dumps(body_dict)
        responses = self.client.post(url='',json=body_dict)
        if responses.status_code == 200:
            logger.info(f'{responses} | word = "{word}"')
        else:
            logger.error(f'{responses} | word = "{word}"')

    @task(3)
    def test_post_random(self):
        word = choice(check_list)
        word = word.strip()
        body_dict = {"source": "en","target": "ko","word": word}
        body = json.dumps(body_dict)
        responses = self.client.post(url='',json=body_dict)
        if responses.status_code == 200:
            logger.info(f'{responses} | word = "{word}"')
        else:
            logger.error(f'{responses} | word = "{word}"')



    if __name__ == '__main__':
        url = 'https://rosetta-nlp-api-dev.yy.com/api/v1/hawkeye-dictionary/dictionary'
        # url = 'http://0.0.0.0:10081/api/v1/hawkeye-dictionary/dictionary'
        cmd = f'locust -f locust_exp.py --host {url}'
        os.system(cmd)

## Linux AB command

https://blog.csdn.net/chenggong2dm/article/details/51850923

https://www.jianshu.com/p/4c599c4c338d