import json
import requests
import os

applicationId = os.environ["LINE_GOHAN_RAKUTEN_RECIPE_ID"]

url_category = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&formatVersion=2&elements=categoryName%2CcategoryId%2CparentCategoryId&categoryType=medium&applicationId=" + applicationId

url_recipe = lambda categoryId: "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&formatVersion=2&categoryId=" + categoryId + "&applicationId=" + applicationId


def getMenus(word):
    id_imfor = requests.get(url_category).json()
    id_imfor_list = id_imfor["result"]["medium"]
    for id in id_imfor_list:
        if id["categoryName"] == word:
            categoryId = str(id["parentCategoryId"]) + "-" + str(id["categoryId"])
            break

    url = url_recipe(categoryId)
    recipe_list = []

    re = requests.get(url).json()
    result = re["result"][0]["recipeTitle"] + "\n" + re["result"][0]["recipeUrl"]

    return result
