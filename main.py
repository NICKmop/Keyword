import keywordGet.Totalkeyword as keywrodGet
import keywordGet.keywordSet.util.csvtojson as csvtojson

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ));
        csvtojson.csvTojson.checkFile();
        # keywrodGet.keyword.keywordData();