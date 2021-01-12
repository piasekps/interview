from sqlalchemy import asc, desc


class BaseSortingAPI:
    model = None
    sorting_mapper = None

    def __init__(self):
        name = self.__class__.__name__
        if self.model is None:
            raise ValueError(f'Model on {name} is not defined')

        if self.sorting_mapper is None:
            raise ValueError(f'Sorting mapper on {name} is not defined')

    def get_objects(self, db_session, params):
        """
        Retrieve objects of given model base on provided parameters

        Args:
            db_session (Session): DB Session object
            params (dict): Query parameters

        Returns:
            (tuple): List of filtered, sorted and paginated objects of defined model, total number of all objects
        """
        page = params.get('page')
        size = params.get('size')
        sorting = params.get('sorting')

        filters = self.build_query_filters(params)
        sorting_value = self.get_sorting_parameter(sorting)
        objects = db_session.query(
            self.model
        ).filter(
            *filters
        ).order_by(
            sorting_value
        )
        paginated_objects = self.paginate_result(
            query=objects,
            size=size,
            page=page
        ).all()

        return paginated_objects, objects.count()

    def get_sorting_parameter(self, sorting):
        """
        Get value which will be used to order transactions

        Args:
            sorting (str): Sorting value, e.g. -name

        Returns:
            (sqlalchemy.sql.elements.UnaryExpression): Sorting value
        """
        order = asc
        if sorting and sorting.startswith('-'):
            order = desc
            sorting = sorting[1:]

        # By default sort by ID
        return order(self.sorting_mapper.get(sorting, self.model.id))

    @staticmethod
    def paginate_result(query, size, page):
        """
        Paginate query result

        Args:
            query (sqlalchemy.orm.query.Query): Query object
            size (int): Desired page size
            page (int): Page number

        Returns:
            (sqlalchemy.orm.query.Query): Paginated query object
        """
        return query.slice(size * page, size * (page + 1))
