#!/usr/bin/env python

class WorkbookReplaceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'Matches': 'int',
            'Workbook': 'LinkElement',
            'Code': 'str',
            'Status': 'str'

        }

        self.attributeMap = {
            'Matches': 'Matches','Workbook': 'Workbook','Code': 'Code','Status': 'Status'}       

        self.Matches = None # int
        self.Workbook = None # LinkElement
        self.Code = None # str
        self.Status = None # str
        
