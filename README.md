# ticke-bot

## Instructions
- Create a virtual python environment with the requirements.txt file
- Activate the environment
- CD to `/tickebot/`
- RUN `scrapy crawl license`
- the results are found in the `/tickebot/rmv.txt` file


## References
- https://doc.scrapy.org/en/latest/intro/tutorial.html

### Initial creation of the environment
```
source venv/bin/activate        # activate the virtual environment
pip freeze > requirements.txt   # export the python requirements for the project
deactivate                      # deactivate the virtual environment
```