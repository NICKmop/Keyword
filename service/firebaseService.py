from typing import Type
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
   
class firebase_con:
    cred = credentials.Certificate('/Users/yeon/StudioProjects/pythoncra/crawling/dbbox/dbcurd-67641-firebase-adminsdk-ax50d-0e1098879e.json')
    # cred = credentials.Certificate('./dbcurd-67641-firebase-adminsdk-ax50d-0e1098879e.json')
    firebase_admin.initialize_app(cred,{ 'databaseURL' : 'https://dbcurd-67641-default-rtdb.firebaseio.com/'});

    def selectKeyword():
        spdataList = [];
        db = firestore.client();
        doc_ref = db.collection(u'crawlingData');
        doc = doc_ref.get();

        for i in doc:
            print(i.reference);

