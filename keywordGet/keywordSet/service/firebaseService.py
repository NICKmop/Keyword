import json
import re, sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ..util.commonUtil import commonUtil
from ..model.datamodel import datasmodel
   
class firebase_con:
    cred = credentials.Certificate('/Users/yeon/StudioProjects/pythoncra/crawling/dbbox/dbcurd-67641-firebase-adminsdk-ax50d-0e1098879e.json')
    # cred = credentials.Certificate('./dbcurd-67641-firebase-adminsdk-ax50d-0e1098879e.json')
    firebase_admin.initialize_app(cred,{ 'databaseURL' : 'https://dbcurd-67641-default-rtdb.firebaseio.com/'});
    db = firestore.client();

    def selectKeyword():
        returnStrBox = [];
        doc_ref = firebase_con.db.collection(u'crawlingData');
        doc = doc_ref.get();

        # 전체
        for i in doc:
            returnStrBox.append(firebase_con.selectKeywordData1(i.id));
        # 일부
        # cnt = 0;
        # stopCount = 4;
        # for i in doc:
        #     cnt += 1;
        #     if(cnt != stopCount):
        #         returnStrBox.append(firebase_con.selectKeywordData1(i.id));
        #     else:
        #         break;
        
        result = {};
        for i in range(len(returnStrBox)):
            todict = dict((x, y) for x, y in returnStrBox[i]);
            for k in todict.keys():
                result[k] = result.get(k, 0) + todict[k]

        N = 20
        res = sorted(result.items(), key = lambda x: x[1], reverse = True)[:N];
        firebase_con.updateKewrod(res);

    def selectKeywordData1(id):
        strBox = [];
        splitBox = [];

        doc_ref = firebase_con.db.collection(u'crawlingData').document(id);
        doc = doc_ref.get().to_dict();

        for i in doc.values():
            new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", " ", i['title']);
            splitBox.append(new_str.split(' '));

        tuple_arr = [tuple(i) for i in splitBox];
        
        for i in range(len(tuple_arr)):
            for j in range(len(tuple_arr[i])):
                strBox.append(tuple_arr[i][j])
        # 배열안의 중복값들에 대한 카운트
        counter = {}
        counterList = [];
        for value in strBox:
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1

        counter = commonUtil.deleteDict(counter);
        
        print(counter);


        # TOP10 추출
        N = 20
        res = sorted(counter.items(), key = lambda x: x[1], reverse = True)[:N];
            
        return res;

    # 키워드 db로 업데이트 
    def updateKewrod(keyword):
        doc_ref = firebase_con.db.collection(u'banner').document('keyword');
        todict = dict((x, y) for x, y in keyword);
        doc_ref.update(todict);

        # for i in keyword:
        #     print(todict);
        # doc_ref.update("{}:{}".format(i[0] , i[1]));
        
        