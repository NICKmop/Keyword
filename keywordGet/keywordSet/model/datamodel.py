class datasmodel:
    keyword = "";

    def __init__(self, keyword):
        self.keyword = keyword;

    def toJson(self, keyword):
        dataModel = {
            self : keyword,
        }
        return dataModel;


        