#!/usr/bin/python

import sys
import xml.sax
import io
import MySQLdb

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="trowel", db="registerdb2011")
        self.cursor = self.db.cursor()
        self.buffer = []
        self.ctrlId = 0
        self.purposeId = 0
    
    def getCharacters(self):
        data = ''.join(self.buffer).strip()
        self.buffer = []
        return data.strip()
    
    def characters(self, name):
        self.buffer.append(name)
        
    def endElement(self, name):
        data = self.getCharacters()
        if name == "DATA_CTLR_NAME":
            self.ctrlId = self.ctrlId +1  
            self.insertDatactrl(data)
            
        elif name == "OTHER_NAME":
            self.insertOthername(data)
        
        elif name == "PURPOSE" and data != "":
            self.purposeId = self.purposeId +1
            self.insertPurpose(data)
            
        elif name == "PURPOSE_TEXT":
            self.insertPurposeOthername(data)
        
        elif name == "CLASS":
            self.insertPurposeClass(data)
            
        elif name == "RECIPIENT":
            self.insertPurposeRecipient(data)
        
        elif name == "TRANSFER":
            self.insertPurposeTransfer(data)
            
        elif name == "SUBJECT":
            self.insertPurposeSubject(data)
        
    def insertDatactrl(self, data):
        self.cursor.execute('insert into datactrl(datactrl_id, datactrl_name) values("%s", "%s")' % (self.ctrlId, data))
        self.db.commit()
        sys.stdout.write("inserted datactrl %s %s\n" % (self.ctrlId, data))

    def insertOthername(self, data):
        self.cursor.execute('insert into datactrl_othernames(datactrl_id, othername) values("%s", "%s")' % (self.ctrlId, data))
        
    def insertPurpose(self, data):
        self.cursor.execute('insert into purpose(purpose_id, datactrl_id, purpose_name) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data))

    def insertPurposeClass(self, data):
        self.cursor.execute('insert into purpose_classes(purpose_id, datactrl_id, class) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data))
            
    def insertPurposeOthername(self, data):
        self.cursor.execute('insert into purpose_othernames(purpose_id, datactrl_id, othername) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data))
        
    def insertPurposeRecipient(self, data):
        self.cursor.execute('insert into purpose_recipients(purpose_id, datactrl_id, recipient) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data))
   
    def insertPurposeSubject(self, data):
        self.cursor.execute('insert into purpose_subjects(purpose_id, datactrl_id, subject) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data))
  
    def insertPurposeTransfer(self, data):
        self.cursor.execute('insert into purpose_transfers(purpose_id, datactrl_id, transfer) values("%s", "%s", "%s")' % (self.purposeId, self.ctrlId, data)) 

handler = MyHandler()

stream = io.open("register_31072011.xml", "r")

xml.sax.parse(stream, handler)
