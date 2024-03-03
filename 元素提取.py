from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


def fetch_magnet_links_with_selenium(url):
    # 初始化Safari WebDriver
    driver = webdriver.Safari()

    try:
        driver.get(url)

        # 等待第一个元素加载并尝试点击
        try:
            first_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "SexArt"))
            )
            ActionChains(driver).move_to_element(first_element).perform()  # 滚动到元素
            first_element.click()
        except ElementNotInteractableException:
            print("第一个元素不可交互。")
            return

        # 等待第二个元素加载并尝试点击
        try:
            second_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Copy Magnet"))
            )
            ActionChains(driver).move_to_element(second_element).perform()  # 滚动到元素
            second_element.click()
        except ElementNotInteractableException:
            print("第二个元素不可交互。")
            return

        # 提取磁力链接并保存
        # ...（您的提取逻辑）

    except TimeoutException:
        print("页面元素加载超时")
    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    url_input = input("请输入要抓取的网页URL: ")
    fetch_magnet_links_with_selenium(url_input)
