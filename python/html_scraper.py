import bs4
import requests
import os

soup = bs4
archive_url = "https://www.simplyscripts.com/c.html"

def get_names():
    r = requests.get(archive_url)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    for item in soup.select('td[a]'):
        link = item.find('a')
        href = archive_url + link['href']
        print(href)
def download_links(href):
    file_name = href.split('/')[-1]
    print("Downloading file: " + file_name)

    # create response object
    r = requests.get(href, stream = True)

    workingDir = os.getcwd()
    print("current working directory: " + workingDir)
    fileDeposit = os.path.join(workingDir, 'movie-names', file_name)
    print(fileDeposit)

    with open(fileDeposit, 'wb') as f:
        for item in soup.select('td[a]'):
            link = item.find('a')
            href = archive_url + link['href']
            f.write(href)
        return

if __name__ == "__main__":

    get_names = get_names()