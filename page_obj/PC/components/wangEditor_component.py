#富文本组件

from page_obj.selenium_page import SeleniumPage


class WangEditor(SeleniumPage):


    wangEditor_input_loc = "//div[@title='%s']//div[@class='wangEditor-txt']"

    #给富文本组件输入值
    def sendkeysToWangEditor(self,fieldName,key):
        self.sendkeysElemByCSS_Visibility(self.wangEditor_input_loc.replace('%s',fieldName),key)

