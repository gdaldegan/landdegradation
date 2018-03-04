from marshmallow import Schema, fields


################################################################################
# Schema for numeric data for plotting within a timeseries object

class TimeSeries(object):
    def __init__(self, time, y, name=None):
        self.time = time
        self.y = y
        self.name = name


class TimeSeriesSchema(Schema):
    time = fields.List(fields.Float())
    y = fields.List(fields.Float())
    name = fields.Str()


class TimeSeriesTable(object):
    def __init__(self, name, table):
        self.type = "TimeSeriesTable"
        self.name = name
        self.table = table


class TimeSeriesTableSchema(Schema):
    type = fields.Str()
    name = fields.Str()
    table = fields.Nested(TimeSeriesSchema(), many=True)


################################################################################
# Schema for downloads

class BandInfo(object):
    def __init__(self, name, add_to_map=False, metadata={}, no_data_value=-32768):
        self.name = name
        self.no_data_value = no_data_value
        self.add_to_map = add_to_map
        self.metadata = metadata


class BandInfoSchema(Schema):
    name = fields.Str()
    no_data_value = fields.Number()
    add_to_map = fields.Boolean()
    metadata = fields.Dict()


class Url(object):
    def __init__(self, url, etag):
        self.url = url
        self.etag = etag


class UrlSchema(object):
    url = fields.Url()
    etag = fields.Str()


class CloudResults(object):
    def __init__(self, name, bands, urls):
        self.type = "CloudResults"
        self.name = name
        self.bands = bands
        self.urls = urls


class CloudResultsSchema(Schema):
    type = fields.Str()
    name = fields.Str()
    bands = fields.Nested(BandInfoSchema(), many=True)
    urls = fields.Nested(UrlSchema())
