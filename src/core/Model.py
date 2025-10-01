class Model():

    tableName = ""

    columns = {}

    primaryKey = "id"

    createdAt = "created_at"

    modifiedAt = "modified_at"

    validations = []

    def before():
        pass

    def after():
        pass

    def beforeInsert():
        pass

    def afterInsert():
        pass

    def beforeUpdate():
        pass

    def afterUpdate():
        pass

    def beforeDelete():
        pass

    def afterDelete():
        pass
