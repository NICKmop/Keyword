import re, sys
import firebase_admin

class commonUtil:

    def compareValue(key, value):
         valueBox = [];
         valueBox.append(value);
         return valueBox;

    def deleteDict(dict):
        if '12' in dict: dict.pop('12');
        if '11' in dict: dict.pop('11');
        if '및' in dict: dict.pop('및');
        if '' in dict: dict.pop('');
        return dict;
