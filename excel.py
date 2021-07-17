import csv
class Excel:
    def __init__(self):
        self.field_names = ['Store Name','Contact Number','Website URL','Address']
        with open('results.csv','a',encoding='utf-8') as leads_csv:
            self.writer = csv.DictWriter(leads_csv, fieldnames=self.field_names,lineterminator='\n')
            self.writer.writeheader()



    
    def append_excel(self,contact,name,website,address):
        with open('results.csv','a',encoding='utf-8') as leads_csv :
            self.writer = csv.DictWriter(leads_csv, fieldnames=self.field_names,lineterminator='\n')
            self.writer.writerow({'Store Name':name,'Contact Number': contact,'Website URL':website,'Address':address})
















