import requests
import requests_cache
from pprint import pprint
from bs4 import BeautifulSoup
from healthDB import DataDiseases

class Spider:
    def __init__(self, url):
        self.url = url

    def requestData(self, url="", title=""):
        requests_cache.install_cache('health')
        if url != "":
            print("     [+] Getting data " + title)
            r = requests.get(url)
        else:
           r = requests.get(self.url)
        return r.content

    def parsingElement(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        mainSection = soup.findAll("section", class_="card-slim")
        return mainSection

    def getDiseasesTop(self, element):
        #list variable for any item
        top_data = []
        for x in range(0, len(element)):
            soup = BeautifulSoup(str(element[x]), 'html.parser')
            diseases_item = soup.findAll('div', class_="hc2-item-col hc2-item-col-3")

            for item in diseases_item:
                diseases = {}

                #Find element a
                url = item.find('a', href=True)

                #Get diseases title
                diseases['title'] = item.text.replace("\n", "")
                #Get diseases url
                diseases['url'] = url['href']
                #Add to list
                top_data.append(diseases)

        return top_data

    def insertSymptoms(self, diseases):
        for x in range(0, len(diseases)):
            print("     [+] Getting symptoms data " + diseases[x]['title'])
            data = self.requestData(url=diseases[x]['url'], title=diseases[x]['title'])
            soup = BeautifulSoup(data, 'html.parser')
            section = soup.findAll('section')

            list_symptoms = []
            definitions = ""
            for sec in section:
                if 'h-ciri-ciri-dan-gejala' in str(sec) or 'h-tanda-tanda-dan-gejala' in str(sec) or 'h-tanda-tanda-gejala' in str(sec):
                    soup = BeautifulSoup(str(sec), 'html.parser')
                    try:
                        ulist = soup.findAll('ul')
                        for ul in ulist:
                            lilist = ul.findAll('li')
                            for li in lilist:
                                list_symptoms.append(li.text)
                    except:
                        list_symptoms.append("")
                elif 'h-definisi' in str(sec):
                    soup = BeautifulSoup(str(sec), 'html.parser')
                    try:
                        definitions = soup.find('p').text 
                    except:
                        definitions = ""                       

            diseases[x]['description'] = definitions
            diseases[x]['symptoms'] = list_symptoms

        return diseases

class HealthCare:
    def __init__(self, diseasesData=""):
        self.diseasesdata = diseasesData
        self.DataDiseases = DataDiseases()

    def syncData(self):
        DB = self.DataDiseases
        #Refresh Join table
        DB.refreshDiseasesSymptoms()
        for x in range(0, len(self.diseasesdata)):
            title = self.diseasesdata[x]['title']
            if self.diseasesdata[x]['description']:
                description = self.diseasesdata[x]['description']
            else:
                description = ""
            if self.diseasesdata[x]['symptoms']:
                symptoms_list = self.diseasesdata[x]['symptoms']

            DB.InsertDiseases(title.capitalize(), description.capitalize())
            diseases_id = DB.getDiseasesID(title)

            if symptoms_list:
                for symptoms in symptoms_list:
                    DB.insertSymptoms(symptoms.capitalize())
                    symptoms_id = DB.getSymptomsID(symptoms.capitalize())

                    #Insert pivot table
                    DB.insertDiseasesSymptoms(diseases_id, symptoms_id)

    def getDiseasesAll(self):
        DB = self.DataDiseases
        diseases = DB.getDiseasesAll()
        return diseases

    def getDiseases(self, name):
        DB = self.DataDiseases
        diseases = DB.getDiseases(name)
        symptomps_list = DB.getSymptoms(name)

        diseases_struct = {}
        diseases_struct['title'] = diseases['name']
        diseases_struct['description'] = diseases['description']
        diseases_struct['symptoms'] = symptomps_list
        return diseases_struct

def crawlingDatabase():
    #Base url for diseases data
    ENDPOINT_URL = 'https://hellosehat.com/kesehatan/penyakit/'

    #Initialzie spider
    spider = Spider(ENDPOINT_URL)

    #Get data request
    data = spider.requestData()

    #Parsing element for every item
    element = spider.parsingElement(data)

    #Get Title and url diseases
    top = spider.getDiseasesTop(element)

    #Get symptoms
    diseasesData = spider.insertSymptoms(top)

    #Uploading data to database
    health = HealthCare(diseasesData=diseasesData)
    health.syncData()

def searchDiseases(diseases):
    health = HealthCare()
    diseases = health.getDiseases(diseases)
    print("")
    print("     ---- DISEASES {} ----".format(diseases['title']))
    print("     Name        : {}".format(diseases['title']))
    print("     Description : {}".format(diseases['description']))
    print("     Symptoms    : ")
    for symptoms in diseases['symptoms']:
        print("                   - {}".format(symptoms['symptoms']))

def getDiseasesAll():
    print("")
    print("     ---- LIST OF DISEASES ----")
    health = HealthCare()
    diseases_list = health.getDiseasesAll()
    for x in range(0, len(diseases_list)):
        print("     [{}] {}".format(str(x+1), diseases_list[x]['name']))

    choose = input("     Which diseases you want to search? [0-{}]: ".format(len(diseases_list)))
    try:
        #Just for validation if input correct number
        index = int(choose)-1
        searchDiseases(diseases_list[index]['name'])
    except Exception as e:
        print("[ERROR]     " + e)

def main():
    print("     ---- HEALTHCARE SYSTEM ----")
    print("     1. Crawling Database")
    print("     2. Search Diseases")
    print("     3. Exit")

    choose = input("     Choose your options: ")
    if choose == "1":
        crawlingDatabase()
    elif choose == "2"  :
        getDiseasesAll()
    else:
        print("     Thank you for using Healthcare System")

if __name__ == "__main__":
    main()
