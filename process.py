from bs4 import BeautifulSoup

def panel_process(content :str):
    page=BeautifulSoup(content)
    return page.findChild(name="ctl00_mainContent_rdMyLesson_C_MyLesson_dlstMyLesson")
