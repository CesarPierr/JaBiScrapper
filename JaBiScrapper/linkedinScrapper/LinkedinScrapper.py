import scrapy
import pandas as pd

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://www.linkedin.com/in/johndoe']

    def parse(self, response):
        name = response.css('li.inline.t-24.t-black.t-normal.break-words::text').get()
        headline = response.css('h2.mt1.t-18::text').get()
        location = response.css('li.t-16.t-black.t-normal.inline-block::text').get()
        summary = response.css('p.inline-show-more-text::text').get()
        experience = []

        for item in response.css('ul.pv-profile-section__section-info.section-info.pb2'):
            company_name = item.css('p.pv-entity__secondary-title.t-14.t-black.t-normal::text').get()
            job_title = item.css('h3.t-16.t-black.t-bold::text').get()
            date_range = item.css('h4.pv-entity__date-range.t-14.t-black--light.t-normal::text').get()
            description = item.css('p.pv-entity__description.t-14.t-black.t-normal::text').get()
            experience.append({'Company': company_name, 'Title': job_title, 'Date': date_range, 'Description': description})

        data = {'Name': name, 'Headline': headline, 'Location': location, 'Summary': summary, 'Experience': experience}
        df = pd.DataFrame(data=[data])

        yield df