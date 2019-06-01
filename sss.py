import json, pprint

x = """{
  "data": {
    "translations": [
      {
        "translatedText": "THE PUBLIC GOOD the despatches For Obama, the mustard is from Dijon",
        "detectedSourceLanguage": "fr"
      }
    ]
  }
}"""

y = json.loads(x)

pprint.pprint(y)

