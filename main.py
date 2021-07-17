import os
from api import ApiResponse
class Main:

    @staticmethod
    def clean_input(input_name):
        return input_name.capitalize()


    @staticmethod
    def check_file():
        current_directory =os.getcwd()
        if os.path.exists(os.path.join(current_directory,'results.csv')):
            os.remove('results.csv')























if __name__ == '__main__':
    industry_name = input("What is the indutry you want to generate leads on?\n")
    # check file if results.csv file exisits
    Main.check_file()
    api_call = ApiResponse(Main.clean_input(industry_name))
    api_call.scrape_data()


