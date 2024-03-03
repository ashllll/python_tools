from selenium import webdriver
from bs4 import BeautifulSoup
import time

def fetch_magnet_links_with_selenium(url, safari_driver_path):
    # 设置 Safari WebDriver
    driver = webdriver.Safari(safari_driver_path)  # Safari WebDriver 的路径
    driver.get(url)
    time.sleep(5)  # 等待页面加载完成，根据实际情况调整等待时间

    # 使用 Selenium 获取页面源代码
    page_source = driver.page_source
    driver.quit()

    # 使用 BeautifulSoup 解析页面源代码
    soup = BeautifulSoup(page_source, 'html.parser')
    magnet_links = [link.get('href') for link in soup.find_all('a') if link.get('href', '').startswith('magnet:')]

    # 将磁力链接写入文件
    if magnet_links:
        with open('magnet_links.txt', 'w', encoding='utf-8') as file:
            for magnet_link in magnet_links:
                file.write(f"{magnet_link}\n")
        print(f"磁力链接已保存到 magnet_links.txt，共{len(magnet_links)}个链接。")
    else:
        print("未找到磁力链接。")

if __name__ == "__main__":
    url_input = input("请输入要抓取的网页URL: ")
    safari_driver_path = "/System/Volumes/Preboot/Cryptexes/App/usr/bin/safaridriver"  # Safari WebDriver 的路径
    fetch_magnet_links_with_selenium(url_input, safari_driver_path)
