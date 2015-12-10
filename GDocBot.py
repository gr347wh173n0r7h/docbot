from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from bs4 import BeautifulSoup
from urllib import urlopen

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

def gSearch(title):
  id = ''
  for file_list in drive.ListFile({'maxResults': 10}):
    for file1 in file_list:
      if file1['title'] == title:
        id = file1['id']
        print(file1['title'])
        print(file1['id'])
        return id

def genHTML(id):
  file6 = drive.CreateFile({'id': id}) # Initialize GoogleDriveFile instance with file id
  file6.GetContentFile('test.html', mimetype='text/html')

def prettyHTML():
  webpage = urlopen('test.html').read().decode('utf-8')
  soup = BeautifulSoup(webpage)
  # print(soup.prettify())
  f = open("doc.html",'w')
  f.write(soup.prettify("utf-8"))
  f.close()

def parseHTML(list):
  webpage = urlopen('doc.html').read().decode('utf-8')
  soup = BeautifulSoup(webpage)
  plist = soup.find_all('span')
  for p in plist:
    # print(p.getText())
    list.append(p.getText().encode("utf8").strip())
  return list

def writeList(list):
  f = open("doc.txt",'w')
  for p in list:
    f.write(str(p))
    f.write('\n')
  f.close()

def main():
  list = []
  id = gSearch('#COP21Tracker')
  genHTML(id)
  prettyHTML()
  list = parseHTML(list)
  writeList(list)

if __name__ == '__main__':
    main()