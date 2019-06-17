import json
import requests
import os
import random

applicationId = os.environ["LINE_GOHAN_RAKUTEN_RECIPE_ID"]

url_category = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&formatVersion=2&elements=categoryName%2CcategoryId%2CparentCategoryId&categoryType=medium&applicationId=" + applicationId

url_ranking = lambda categoryId: "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&formatVersion=2&categoryId=" + categoryId + "&applicationId=" + applicationId


def getMenus(word):

    id_imfor = requests.get(url_category).json()
    id_imfor_list = id_imfor["result"]["medium"]

    result_list = []

    for id in id_imfor_list:
        if word in id["categoryName"]:
            categoryId = str(id["parentCategoryId"]) + "-" + str(id["categoryId"])

            url = url_ranking(categoryId)

            recipe_imfor = requests.get(url).json()
            recipe_imfor_list = recipe_imfor["result"]

            for recipe_ranking in recipe_imfor_list:

                result = recipe_ranking["recipeTitle"] + "\n" + recipe_ranking["recipeUrl"]

                result_list.append(result)


    result =  random.choice(result_list)

    return result
