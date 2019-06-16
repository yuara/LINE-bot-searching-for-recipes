import json
import requests

applicationId = os.environ["LINE_GOHAN_RAKUTEN_RECIPE_ID"]

url_category = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&formatVersion=2&elements=categoryName%2CcategoryId%2CparentCategoryId&categoryType=medium&applicationId=" + applicationId

url_recipe = lambda categoryId: "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&formatVersion=2&categoryId=" + categoryId + "&applicationId=" + applicationId


def getMenus(word):
    serch = requests.get(url_category).json()
    #print(res)
    id_imfor = serch["result"]["medium"]
    for id in id_imfor:
        if id["categoryName"] == word:
            categoryId = str(id["parentCategoryId"]) + "-" + str(id["categoryId"])
            #print(categoryId)
            break

    url = url_recipe(categoryId)
    recipe_list = []

    re = requests.get(url).json()
    #print(re["result"][0]["recipeTitle"])
    result = re["result"][0]["recipeTitle"]
    #result = [re["result"]["recipeTitle"], re["result"]["recipeUrl"]]


    #print(result)

    #result = '\n'.join(list)
    return result
