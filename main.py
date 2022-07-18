import pandas as pd
from flask import Flask, request
from flask_restful import Api, Resource
import json
from json import JSONEncoder






# >>> import requests
# >>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# >>> r.status_code
# 200
# >>> r.headers['content-type']
# 'application/json; charset=utf8'
# >>> r.encoding
# 'utf-8'
# >>> r.text
# '{"authenticated": true, ...'
# >>> r.json()
# {'authenticated': True, ...}


app = Flask(__name__)
api = Api(app)

df_2016 = pd.read_csv("2016.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2017 = pd.read_csv("2017.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2018 = pd.read_csv("2018.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2019 = pd.read_csv("2019.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2020 = pd.read_csv("2020.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2021 = pd.read_csv("2021.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])
df_2022 = pd.read_csv("2022.csv", sep=",", header=None,
                      names=["Detached", "Sales", "Semidet", "Sales2", "Terraced", "Sales3", "Flat", "Sales4",
                             "Overall average", "Total sales"])


class ikibinonaltı(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2016, "Average Detached House Price in £": df_2016.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2016.loc[n].tolist()[1],
                "Average Semi-Detached House Price in £": df_2016.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2016.loc[n].tolist()[3],
                "Average Terraced House Price in £": df_2016.loc[n].tolist()[4],
                "Number of Terraced House Sales": df_2016.loc[n].tolist()[5],
                "Average Flat Price in £": df_2016.loc[n].tolist()[6],
                "Number of Flate Sales": df_2016.loc[n].tolist()[7],
                "Overall Average Prices in £": df_2016.loc[n].tolist()[8],
                "Total Number of Sales": df_2016.loc[n].tolist()[9]}


class ikibinonyedi(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2017, "Average Detached House Price in £": df_2017.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2017.loc[n].tolist()[1],
                "Average Semi-Detached House Price in £": df_2017.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2017.loc[n].tolist()[3],
                "Average Terraced House Price in £": df_2017.loc[n].tolist()[4],
                "Number of Terraced House Sales in £": df_2017.loc[n].tolist()[5],
                "Average Flat Price in £": df_2017.loc[n].tolist()[6],
                "Number of Flate Sales": df_2017.loc[n].tolist()[7],
                "Overall Average Prices in £": df_2017.loc[n].tolist()[8],
                "Total Number of Sales": df_2017.loc[n].tolist()[9]}


class ikibinonsekiz(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2018, "Average Detached House Price in £": df_2018.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2018.loc[n].tolist()[1],
                "Average Semi-Detached House Price in £": df_2018.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2018.loc[n].tolist()[3],
                "Average Terraced House Price in £": df_2018.loc[n].tolist()[4],
                "Number of Terraced House Sales": df_2018.loc[n].tolist()[5],
                "Average Flat Price in £": df_2018.loc[n].tolist()[6],
                "Number of Flate Sales": df_2018.loc[n].tolist()[7],
                "Overall Average Prices in £": df_2018.loc[n].tolist()[8],
                "Total Number of Sales": df_2018.loc[n].tolist()[9]}


class ikibinondokuz(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2019, "Average Detached House Price in £ ": df_2019.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2019.loc[n].tolist()[1],
                "Average Semi-Detached House Price in £": df_2019.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2019.loc[n].tolist()[3],
                "Average Terraced House Price in £": df_2019.loc[n].tolist()[4],
                "Number of Terraced House Sales": df_2019.loc[n].tolist()[5],
                "Average Flat Price in £": df_2019.loc[n].tolist()[6],
                "Number of Flate Sales": df_2019.loc[n].tolist()[7],
                "Overall Average Prices in £": df_2019.loc[n].tolist()[8],
                "Total Number of Sales": df_2019.loc[n].tolist()[9]}


class ikibinyirmi(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2020, "Average Detached House Price": df_2020.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2020.loc[n].tolist()[1],
                "Average Semi-Detached House Price": df_2020.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2020.loc[n].tolist()[3],
                "Average Terraced House Price": df_2020.loc[n].tolist()[4],
                "Number of Terraced House Sales": df_2020.loc[n].tolist()[5],
                "Average Flat Price": df_2020.loc[n].tolist()[6],
                "Number of Flate Sales": df_2020.loc[n].tolist()[7],
                "Overall Average Prices": df_2020.loc[n].tolist()[8],
                "Total Number of Sales": df_2020.loc[n].tolist()[9]}


class ikibinyirmibir(Resource):
    def get(self, n):
        return {"PostCode": n, "Year:": 2021, "Average Detached House Price in £": df_2021.loc[n].tolist()[0],
                "Number of Detached House Sales": df_2021.loc[n].tolist()[1],
                "Average Semi-Detached House Price in £": df_2021.loc[n].tolist()[2],
                "Number of Semi-Detached House Sales": df_2021.loc[n].tolist()[3],
                "Average Terraced House Price in £": df_2021.loc[n].tolist()[4],
                "Number of Terraced House Sales": df_2021.loc[n].tolist()[5],
                "Average Flat Price in £": df_2021.loc[n].tolist()[6],
                "Number of Flate Sales": df_2021.loc[n].tolist()[7],
                "Overall Average Prices in £": df_2021.loc[n].tolist()[8],
                "Total Number of Sales": df_2021.loc[n].tolist()[9]}


class ikibinyirmiiki(Resource):
    def get(self, n):
        dic_2022 = {"PostCode": n, "Year:": 2022, "Average Detached House Price in £": df_2022.loc[n].tolist()[0],
                    "Number of Detached House Sales": df_2022.loc[n].tolist()[1],
                    "Average Semi-Detached House Price in £": df_2022.loc[n].tolist()[2],
                    "Number of Semi-Detached House Sales": df_2022.loc[n].tolist()[3],
                    "Average Terraced House Price in £": df_2022.loc[n].tolist()[4],
                    "Number of Terraced House Sales": df_2022.loc[n].tolist()[5],
                    "Average Flat Price in £": df_2022.loc[n].tolist()[6],
                    "Number of Flate Sales": df_2022.loc[n].tolist()[7],
                    "Overall Average Prices in £": df_2022.loc[n].tolist()[8],
                    "Total Number of Sales": df_2022.loc[n].tolist()[9]
                    }

        'One Year Price Trend'

        if df_2022.loc[n].tolist()[8] > df_2021.loc[n].tolist()[8]:
            dic_2022["region.priceTrend.price1YearIncDec"] = "Increasing"
            dic_2022["region.priceTrend.price1YearPercent "] = ((df_2022.loc[n].tolist()[8] - df_2021.loc[n].tolist()[
                8]) / df_2021.loc[n].tolist()[8]) * 100
        else:
            dic_2022["Average.region.priceTrend.price1YearIncDec"] = "Decreasing"
            dic_2022["region.priceTrend.price1YearPercent "] = ((df_2022.loc[n].tolist()[8] - df_2021.loc[n].tolist()[
                8]) / df_2021.loc[n].tolist()[8]) * 100


        'Five Years Price Trend'

        previousFiveyearsaverage_2022 = (df_2021.loc[n].tolist()[8] + df_2020.loc[n].tolist()[8] +
                                        df_2019.loc[n].tolist()[8] + df_2018.loc[n].tolist()[8] +
                                        df_2017.loc[n].tolist()[8]) / 5

        if df_2022.loc[n].tolist()[8] > previousFiveyearsaverage_2022:
            dic_2022["Average.region.priceTrend.price5YearIncDec"] = "Increasing"

        else:
            dic_2022["Average.region.priceTrend.price5YearIncDec"] = "Decreasing"

        dic_2022["region.priceTrend.price5YearPercent "] = ((df_2022.loc[n].tolist()[
                                                                 8] - previousFiveyearsaverage_2022)
                                                            /previousFiveyearsaverage_2022) * 100

        'Ten Years Price Trend'

        # previousTenyearsaverage_2022 = (previousFiveyearsaverage_2022*5 +df_2016.loc[n].tolist()[8] + df_2015.loc[n].tolist()[8] +
        #                                 df_2014.loc[n].tolist()[8] + df_2013.loc[n].tolist()[8] +
        #                                 df_2012.loc[n].tolist()[8]) / 10
        #
        # if df_2022.loc[n].tolist()[8] > previousTenyearsaverage_2022:
        #     dic_2022["Average.region.priceTrend.price10YearIncDec"] = "Increasing"
        #
        # else:
        #     dic_2022["Average.region.priceTrend.price10YearIncDec"] = "Decreasing"
        #
        # dic_2022["region.priceTrend.price10YearPercent "] = ((df_2022.loc[n].tolist()[
        #                                                          8] - previousTenyearsaverage_2022)
        #                                                     / previousTenyearsaverage_2022) * 100

        return dic_2022

api.add_resource(ikibinonaltı, "/2016/<string:n>")
api.add_resource(ikibinonyedi, "/2017/<string:n>")
api.add_resource(ikibinonsekiz, "/2018/<string:n>")
api.add_resource(ikibinondokuz, "/2019/<string:n>")
api.add_resource(ikibinyirmi, "/2020/<string:n>")
api.add_resource(ikibinyirmibir, "/2021/<string:n>")
api.add_resource(ikibinyirmiiki, "/2022/<string:n>")

if __name__ == "__main__":
    app.run()

print(response.status_code)
