#!/usr/bin/env python

class Comment(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'CellName': 'str',
            'Author': 'str',
            'HtmlNote': 'str',
            'Note': 'str',
            'AutoSize': 'bool',
            'IsVisible': 'bool',
            'Width': 'int',
            'Height': 'int',
            'TextHorizontalAlignment': 'str',
            'TextOrientationType': 'str',
            'TextVerticalAlignment': 'str',
            'link': 'Link'

        }

        self.attributeMap = {
            'CellName': 'CellName','Author': 'Author','HtmlNote': 'HtmlNote','Note': 'Note','AutoSize': 'AutoSize','IsVisible': 'IsVisible','Width': 'Width','Height': 'Height','TextHorizontalAlignment': 'TextHorizontalAlignment','TextOrientationType': 'TextOrientationType','TextVerticalAlignment': 'TextVerticalAlignment','link': 'link'}       

        self.CellName = None # str
        self.Author = None # str
        self.HtmlNote = None # str
        self.Note = None # str
        self.AutoSize = None # bool
        self.IsVisible = None # bool
        self.Width = None # int
        self.Height = None # int
        self.TextHorizontalAlignment = None # str
        self.TextOrientationType = None # str
        self.TextVerticalAlignment = None # str
        self.link = None # Link
        