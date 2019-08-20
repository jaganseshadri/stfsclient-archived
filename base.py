import grpc
from google.protobuf import text_format

def _unwrap_pb(obj):
    if isinstance(obj, Message):
        return obj._protobuf
    return obj


def _wrap_pb(wp, pb):
    wp._protobuf.CopyFrom(pb)
    return wp


class Message(object):
    def __init__(self, protobuf, **kwargs):
        self._protobuf = protobuf
        self.update(**kwargs)
    
    def update(self, **kwargs):
        if kwargs is None:  
            return
        
        for attr, val in kwargs.items():
            val = self.unwrap_pb(val)
            if val is not None:
                # use the class attribute setter method
                setattr(self, attr, val)

    def __str__(self):
        return str(self._protobuf)

    def __repr__(self):
        return repr(self._protobuf)
            
    def from_text(self, path):
        with open(path, 'r+') as f: 
            text_format.Merge(text=f.read(), message=self._protobuf)           

    def to_text(self, path):
        with open(path, 'w+') as f:
            f.write(text_format.MessageToString(message=self._protobuf))

    def from_pb(self, path):
        with open(path, 'rb') as f:
            self._protobuf.ParseFromString(f.read())

    def to_pb(self, path):
        with open(path, 'wb') as f:
            f.write(self._protobuf.SerializeToString())       

    def copy(self, obj):
        obj = self.unwrap_pb(obj)
        self._protobuf.CopyFrom(obj)

    def merge(self, obj):
        obj = self.unwrap_pb(obj)
        self._protobuf.MergeFrom(obj)

    @property
    def is_initialized(self):
        return self._protobuf.IsInitialized()
    
    @property
    def byte_size(self):
        return self._protobuf.ByteSize()

    @staticmethod
    def unwrap_pb(obj):
        return _unwrap_pb(obj)

    @staticmethod
    def wrap_pb(wp, pb):
        return _wrap_pb(wp, pb)


class GRPCService(object):
    def __init__(self, server):
        self.channel = self.create_insecure_channel(server)

    def create_secure_channel(self):
        raise NotImplementedError

    def create_insecure_channel(self, server):
        return grpc.insecure_channel(server)

    @staticmethod
    def unwrap_pb(obj):
        return _unwrap_pb(obj)

    @staticmethod
    def wrap_pb(wp, pb):
        return _wrap_pb(wp, obj)


# TODO: A class for message map containers
class MessageMap(object):
    def __init__(self, **kwargs):
        pass