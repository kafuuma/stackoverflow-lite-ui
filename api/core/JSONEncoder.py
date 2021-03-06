from flask.json import JSONEncoder as BaseJSONEncoder
from api.core.models import Model
from api.core.models.collections import ModelCollection


class JSONEncoder(BaseJSONEncoder):
    def default(self, o):
        if isinstance(o, (Model, ModelCollection)):
            return o.to_json()
        if isinstance(o, bytes):
            return o.decode("UTF-8")
        return BaseJSONEncoder.default(self, o)
