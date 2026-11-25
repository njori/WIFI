class BaseService:

    repository = None

    @classmethod
    def all(cls):

        return [
            item.to_dict()
            for item in cls.repository.get_all()
        ]

    @classmethod
    def get(cls, object_id):

        obj = cls.repository.get_by_id(object_id)

        if obj is None:
            raise Exception("Resource not found.")

        return obj.to_dict()

    @classmethod
    def delete(cls, object_id):

        obj = cls.repository.get_by_id(object_id)

        if obj is None:
            raise Exception("Resource not found.")

        cls.repository.delete(obj)