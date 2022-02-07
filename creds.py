email_id = "DANIELGNASCIMENTO7@gmail.com"

password = "prontocor"

chromeDriverPath = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\~hromedriver_binary\\chromedriver.exe'

website = 'https://netflix.com'

series_name = "Two and a half men"

sign_in_xpath = '/html/body/div[1]/div/div/div/div/div/div[1]/div/a'

email_xpath = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input'

pass_xpath = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input'

signin_xpath = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button'

sann_profile_xpath = '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div'

search_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button'

searchbox_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div'

content_tile_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/a/div[2]'

player_info_close_button = '/html/body/div[4]/div/button'

windows_users='DELL'

pc_ss_dir_path = 'C:\\Users\\DELL\\Pictures\\Screenshots'

ss_dir_path = '/src/Netflix_image_subtitle_crawler/Screenshots'

ss_dir_path_win = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\Screenshots\\'

filename_clean_hindi = 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler\\Screenshots\\pilot_ep_1.xlsx'



class newName:
    
    newname = ''
    
    def __init__(self, name):
        self.newname = name.replace('.','_')

    def getNewName(self):
        return self.newname

    def UpdateNewName(self,name):
        self.newname = name
    

