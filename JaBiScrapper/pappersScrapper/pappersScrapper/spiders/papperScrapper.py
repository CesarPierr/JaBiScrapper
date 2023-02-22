import scrapy
import pandas as pd
import json
class PapperscrapperSpider(scrapy.Spider):
    name = "papperScrapper"
    allowed_domains = ["www.pappers.fr"]
    start_urls = [
        "https://www.pappers.fr/entreprise/google-france-443061841",
    ]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Obtenir le contenu de la div ayant l'identifiant "resume"
        resume = response.css("#resume").extract_first()

        # Extraire les données de la div "resume"
        nom = response.css("h1.big-text::text").get()
        siren = response.css(".siren-to-copy::text").get()
        status = response.css(".status .actif::text").get()
        adresse = response.css("tr:nth-child(1) td::text").get()
        activite = response.css("tr:nth-child(2) td::text").get()
        effectif = response.css("tr:nth-child(3) td::text").get()
        creation = response.css("tr:nth-child(4) td::text").get()
        dirigeants = response.css("tr:nth-child(5) td .info-dirigeant a::text").getall()
        print("#################################")

        data = json.loads(response.css('div.content.finances-bloc').css("finances")[0].attrib[':data'])
        df = pd.DataFrame(data)
        for year in data :
            yield year
        print("#################################")
        for dirigeant in response.xpath('//section[@id="dirigeants"]/div/ul/li'):
            yield {
                'nom': dirigeant.xpath('.//a/text()').get(),
                'qualite': dirigeant.xpath('.//span[@class="qualite"]/text()').get(),
                'date_de_naissance': dirigeant.xpath('.//div[@class="age-siren"]/span[2]/text()').get(),
                'date_debut': dirigeant.xpath('.//span[contains(@class, "age-siren")]/text()').get(),
            }


        print("#################################")
        # Formater les données
        effectif = effectif.strip() if effectif else None
        dirigeants = ", ".join(dirigeants) if dirigeants else None

        # Renvoyer les données dans un dictionnaire
        yield {
            "nom": nom.strip() if nom else None,
            "siren": siren.strip() if siren else None,
            "status": status.strip() if status else None,
            "adresse": adresse.strip() if adresse else None,
            "activite": activite.strip() if activite else None,
            "effectif": effectif,
            "creation": creation.strip() if creation else None,
            "dirigeants": dirigeants,
        }