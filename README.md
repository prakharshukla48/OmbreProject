# OmbreProject
 Web scraping of bandsintown website.

>This is project web scrapes the websote bandsintown to get the nname of artist of event and other details.
---
## Installation:
* download and Install the python from [link](python.org) and make sure to select ADD PATH .cmd during installation
>Then install important packages needed for scraping in command prompt using the package manager [pip](https://pip.pypa.io/en/stable/) .
```bash
* pip install requests
* pip install HTML5lib
* pip install bs4
```
## Usage
```python
import requests
from bs4 import BeautifulSoup
r = requests.get(url)
soup = BeautifulSoup(content,'Html.parser')
```
## License
>[MIT](https://choosealicense.com/licenses/mit/)
