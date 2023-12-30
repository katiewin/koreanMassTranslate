# translate/api_calls/api_call.py
import requests
import xml.etree.ElementTree as ET
import logging

class APICall:
    @staticmethod
    def search_korean_dictionary(api_key, search_query, part_of_speech=None):
        base_url = "https://krdict.korean.go.kr/api/search"
        api_key = api_key
        search_query = search_query
        part_of_speech = part_of_speech

        params = {
            "key": api_key,
            "type_search": "search", 
            "part": "word", 
            "q": search_query,
            "advanced": "y",
            "pos": part_of_speech,
            "sort": "dict",
            "translated": "y"
        }

        response = requests.get(base_url, params=params)

        if response.status_code != 200:
            logging.error(f"Error: {response.status_code}")
            return None, None

        try:
            root = ET.fromstring(response.content)
            item = root.find(".//item")

            if item is None:
                logging.debug("No item found in the XML.")
                return "word not found", "word not found"

            sense = item.find(".//sense")
            translation = sense.find(".//translation[1]")

            if translation is None:
                logging.debug("No translation found in the XML.")
                return "word not found", "word not found"

            etrans = translation.find(".//trans_word").text
            e_sentence = translation.find(".//trans_dfn").text
            return etrans, e_sentence

        except ET.ParseError as e:
            logging.error(f"Error parsing XML: {e}")

        return "word not found", "word not found"

    @staticmethod
    def getWords(k_word, kpos):
        logging.debug(k_word)
        logging.debug(kpos)
        search_query = k_word
        part_of_speech = kpos
        api_key = 'ED007AAB75E7A6DE59A63430BD209C74'
        translation, example_sentence = APICall.search_korean_dictionary(api_key, search_query, part_of_speech)
        
        return translation, example_sentence
