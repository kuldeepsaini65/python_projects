from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep  # sleep is used for waiting time to load page(based on net speed) and then next step


def login():
    """     Login Process Started Here      """
    webdriver.get("https://www.instagram.com/accounts/login/")
    sleep(3)
    username = webdriver.find_element_by_name('username')
    username.send_keys('secret__star65')
    sleep(1)
    password = webdriver.find_element_by_name('password')
    password.send_keys('ramram')
    sleep(1)
    login_button = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
    login_button.click()


def do_not_save_login_info():
    """ Save Login Info """
    sleep(4)
    not_now = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    not_now.click()


def notification_turned_off():
    """ Turn Notification Off """
    sleep(4)
    notification_off = webdriver.find_element_by_css_selector(
        'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notification_off.click()


def redirect_to_hashtag():
    """   Redirecting to #tags """
    sleep(3)
    hashtags = ['like4like']
    tag = 0
    tag_link = 'https://www.instagram.com/explore/tags/'
    for line_by_line_tag in hashtags:
        webdriver.get(tag_link + hashtags[0] + '/')
        sleep(5)
        clicker = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['
                                                  '1]/div[1]/a/div')
        clicker.click()
        sleep(1)


def follow_function():
    """ trying to follow """
    sleep(4)
    work_done = 0
    followed = 0
    prev_user_list = []
    while work_done != 10:
        file = open('followed.txt', 'w')
        sleep(4)
        username_name = webdriver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text

        if username_name not in prev_user_list:
            if webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                follow = webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                prev_user_list.append(username_name)

        followed = + 1
        sleep(2)

        next_post2 = webdriver.find_element_by_css_selector(
            'body > div._2dDPU.RnrQH.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        next_post2.click()

        work_done = work_done + 1
        sleep(3)

        with open('logs.txt', 'w') as logs:
            for names in range(len(prev_user_list)):
                logs.write(f"{prev_user_list[names]}\n")

    print(f"Usernames = {prev_user_list}")


def like_function():
    likes = 0
    likes_done = 0
    while likes_done != 10:
        sleep(3)
        username_name = webdriver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
        like = webdriver.find_element_by_css_selector(
            'body > div._2dDPU.RnrQH.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n '
            '> button > div > span > svg')
        like.click()
        likes = likes + 1
        next_post2 = webdriver.find_element_by_css_selector(
            'body > div._2dDPU.RnrQH.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        next_post2.click()
        likes_done = likes_done + 1


def like_and_follow():
    sleep(4)
    work_done = 0
    likes = 0
    followed = 0
    prev_user_list = []
    while work_done != 10:
        file = open('followed.txt', 'w')
        sleep(4)
        username_name = webdriver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text

        if username_name not in prev_user_list:
            if webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                follow = webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                prev_user_list.append(username_name)

        followed = + 1
        sleep(2)

        like = webdriver.find_element_by_css_selector(
            'body > div._2dDPU.RnrQH.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n '
            '> button > div > span > svg')
        like.click()
        likes = likes + 1

        next_post2 = webdriver.find_element_by_css_selector(
            'body > div._2dDPU.RnrQH.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        next_post2.click()

        work_done = work_done + 1
        sleep(3)


if __name__ == '__main__':
    print('****** Welcome To InstaAutoBot *******')
    print("What You Want To Do? \n1 - Follow Only\n2 - Like Only\n3 - Both ")
    user_choice = int(input("PLease Enter Number Of Your Choice As Shown On Above Options   ----> "))
    webdriver = webdriver.Chrome()
    print("\nLogin Processing....")
    if user_choice == 1:
        login()
        do_not_save_login_info()
        sleep(1)
        notification_turned_off()
        sleep(1)
        redirect_to_hashtag()
        sleep(1)
        follow_function()
        sleep(1)


    elif user_choice == 2:
        login()
        do_not_save_login_info()
        sleep(1)
        notification_turned_off()
        sleep(1)
        redirect_to_hashtag()
        sleep(1)
        like_function()
        sleep(1)


    elif user_choice == 3:
        login()
        sleep(4)
        do_not_save_login_info()
        sleep(1)
        notification_turned_off()
        sleep(1)
        redirect_to_hashtag()
        sleep(1)
        like_and_follow()


    else:
        print("You Typed Invalid Option")
        print("Try Again")
