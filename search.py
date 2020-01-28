import json
import requests
import os
import random
from time import sleep

applicationId = os.environ["LINE_GOHAN_RAKUTEN_RECIPE_ID"]

url_category = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&formatVersion=2&elements=categoryName%2CcategoryId%2CparentCategoryId&categoryType=medium&applicationId=" + applicationId

url_ranking = lambda categoryId: "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&formatVersion=2&categoryId=" + categoryId + "&applicationId=" + applicationId


def getRecipe(word):

    id_imfor = requests.get(url_category).json()
    id_imfor_list = id_imfor["result"]["medium"]

    result_list = []

    if word == "使い方":
        result = "キーワードを送信するとレシピを1つ返信します。\n多くの候補がある場合、返信に時間がかかります。\n \n何にしよう　でランダムにレシピを表示させます。"

    elif word == "何にしよう":
        recipe_id = random.choice(id_imfor_list)
        categoryId = str(recipe_id["parentCategoryId"]) + "-" + str(recipe_id["categoryId"])

        url = url_ranking(categoryId)

        recipe_imfor = requests.get(url).json()
        recipe_imfor_list = recipe_imfor["result"]
        sleep(0.5)

        for recipe_ranking in recipe_imfor_list:

            results = recipe_ranking["recipeTitle"] + "\n" + recipe_ranking["recipeUrl"]

            result_list.append(results)

        result = random.choice(result_list)

    else:
        for id in id_imfor_list:
            if word in id["categoryName"]:
                categoryId = str(id["parentCategoryId"]) + "-" + str(id["categoryId"])

                url = url_ranking(categoryId)

                recipe_imfor = requests.get(url).json()
                recipe_imfor_list = recipe_imfor["result"]
                sleep(0.5)

                for recipe_ranking in recipe_imfor_list:

                    results = recipe_ranking["recipeTitle"] + "\n" + recipe_ranking["recipeUrl"]

                    result_list.append(results)

        if len(result_list) == 0:
            result = word + " のレシピはありません。" + "\n" + "別の文字表記でも試してみてください。"

        else:
            result = random.choice(result_list)

    return result
