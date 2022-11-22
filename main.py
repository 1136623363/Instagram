import requests
import json
import time
import random
import os
import urllib3

global false, null, true,count
false = null = true = '' #出现NameError: name 'false' is not defined这个错误时，是因为在使用eval转化为字典时，中间的false，null等区分大小写导致

class instagram():
    def __init__(self,name,img_path):
        self.name=name
        self.img_path=img_path
        self.url_list= []
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
        self.headers= {'User-Agent': random.choice(user_agent_list)}

    def parse(self,max_id):
        #url = 'https://www.instagram.com/api/v1/feed/user/2950756662/?count=12&max_id=2933656732534507495_2950756662'
        #The lastest one is
        #https://scontent-mia3-1.cdninstagram.com/v/t51.2885-15/12747584_1049645628432234_577740114_n.jpg?stp=dst-jpg_e35&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=106&_nc_ohc=LnkTvVtO1dgAX9zl4Yh&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=MTE4NjI2MjE3MDY2NzE4ODAxMA==.2-ccb7-5&oh=00_AfDNf6U0V3h5tkmNAmc4wG_3EVimgcUKoodARNFxL6Yn3Q&oe=63803C50&_nc_sid=6136e7
        print("\rnext_max_id= "+max_id,end='')
        url = f'https://www.instagram.com/api/v1/feed/user/{self.name}/username/?count=12&max_id='+max_id
        headers = {
            #'accept':' */*',
            #'accept-encoding': 'gzip, deflate, br',
            #'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': r'ig_nrcb=1; mid=Y3tXWwALAAEXul-EKxeDXGhm1CL4; ig_did=5AF81308-3432-49A0-A6EC-33268147DCB6; datr=WVd7Y4UPCFdxMHwrdqzxOlGf; csrftoken=hBVdpE6jwPqXMljwn3N4nni6LBVxwT2S; ds_user_id=44353525392; sessionid=44353525392%3AiAvPhrPGWRwJzX%3A12%3AAYcOag-5Pgwd3XyT5stuHvFYbtv0I0jNUP7h8-B5ng; shbid="18530\05444353525392\0541700563731:01f73477c4680e68240ff3e95d4223ec5ef796a3533d4fbf9aad530e083609c379434124"; shbts="1669027731\05444353525392\0541700563731:01f76ba95b52960e3ee0c31e9b416ee7b6c9912ed1877e98a1b5139b8c82fef22bf7b2a1"; rur="EAG\05444353525392\0541700564277:01f7f81692e187e2396ca8d0d16b968076fcd09f9acb5ff8f59c56f3e336e189cb80efa5"',
            'referer': 'https://www.instagram.com/iu_leejieun516/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '915',
            'x-asbd-id': '198387',
            'x-csrftoken': 'hBVdpE6jwPqXMljwn3N4nni6LBVxwT2S',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1IWCZPP4AHHJxgQml46ZQRQ8rRdBC1rMx9oxu_ZQJzbJ8H',
            'x-instagram-ajax': '1006631267',
            #'x-requested-with': r'XMLHttpRequesties':r'ig_nrcb=1; mid=Y3tXWwALAAEXul-EKxeDXGhm1CL4; ig_did=5AF81308-3432-49A0-A6EC-33268147DCB6; datr=WVd7Y4UPCFdxMHwrdqzxOlGf; csrftoken=hBVdpE6jwPqXMljwn3N4nni6LBVxwT2S; ds_user_id=44353525392; sessionid=44353525392:iAvPhrPGWRwJzX:12:AYcOag-5Pgwd3XyT5stuHvFYbtv0I0jNUP7h8-B5ng; shbid="18530\05444353525392\0541700563731:01f73477c4680e68240ff3e95d4223ec5ef796a3533d4fbf9aad530e083609c379434124"; shbts="1669027731\05444353525392\0541700563731:01f76ba95b52960e3ee0c31e9b416ee7b6c9912ed1877e98a1b5139b8c82fef22bf7b2a1"; rur="EAG\05444353525392\0541700564277:01f7f81692e187e2396ca8d0d16b968076fcd09f9acb5ff8f59c56f3e336e189cb80efa5"'
        }

        try:
            response = requests.get(url=url,headers=headers)
        except:
            print('\rget url fail and try again after 2 second',end='')
            time.sleep(2)
            response = requests.get(url=url, headers=headers)

        return response.text

    def dealText(self,text):
        resp_dict = eval(text)
        # print(resp_dict.keys())
        # for i in resp_dict.items():
        #     print(i)
        next_max_id = resp_dict['next_max_id']
        resp_items = resp_dict['items']
        #print(len(resp_items))
        for i in resp_items:
            if 'carousel_media' in i.keys():
                for j in i['carousel_media']:
                    self.url_list.append(j['image_versions2']['candidates'][0]['url'])
        return next_max_id

    def downlaod_img(self,url_list):
        count = 1
        if not os.path.exists(self.img_path):
            os.mkdir(self.img_path)
        for img_url in url_list:
            filename = self.img_path+f'\{count}.jpg'
            if os.path.exists(filename) == False:
                try:
                    img_resp = requests.get(url=img_url, headers=self.headers,timeout=3)
                except:
                    try:
                        # print('Download fail and try again after 2 second')
                        time.sleep(2)
                        img_resp = requests.get(url=img_url, headers=self.headers,timeout=3)
                    except (TimeoutError,ConnectionResetError,requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError,
                            urllib3.exceptions.ReadTimeoutError,urllib3.exceptions.ProtocolError):
                        print('\nPlease check your network')
                        #break
                    # finally:
                    #     print('\nDownload Done')

                self.ProgressBar(len(url_list),count)

                with open(filename,'wb') as f:
                        f.write(img_resp.content)
            elif os.path.exists(filename) == True:
                print(end='')
            count += 1


    def ProgressBar(self,sum,count):
        length = 50
        i = round(count / sum * length)
        flag = 1-int(int(count / sum * 100)/100)
        print(f"\r{count}/{sum}         " + "[" + "=" * i + ">"*flag+" " * (length - i) + "]" + str(int(count / sum * 100)) + "%", end="")

    def loadjson(self):
        if os.path.exists(f'{self.name}.json') == True:
            f=open(f'{self.name}.json','r')
            img_url = json.load(f)
            f.close()
            print(f'load {len(img_url)} img_url in total')
            return img_url
        elif os.path.exists(f'{self.name}.json') == False:
            return ''

    def run(self,max_id):
        text = self.parse(max_id)  # 发送url请求
        max_id = self.dealText(text)  # 处理文本：1.添加url 2.返回max_id
        try:
            self.run(max_id)
        except:
            print('\rget url completely')
            fp = open(f'{self.name}.json', 'w')
            json.dump(self.url_list, fp)
            fp.close()

def main():
    #name = '2213235565'
    name = 'cristiano' #更改为你需要爬取的博主的username
    img_dir = f'D:\Desktop\{name}' #img path
    a = instagram(name, img_dir)
    a.run('')
    a.downlaod_img(a.loadjson())

if __name__ == '__main__':
    main()
