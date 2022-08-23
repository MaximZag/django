from rest_framework.views import APIView
from rest_framework.response import Response

users = [
    {'id': 1, 'name': 'max', 'age': 15},
    {'id': 2, 'name': 'kira', 'age': 25},
    {'id': 3, 'name': 'karina', 'age': 19},
    {'id': 4, 'name': 'oleh', 'age': 30},
]


class UserListCreateView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        new_user = self.request.data
        users.append(new_user)
        return Response(new_user)


class UserFindUpdateDelete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                return Response(user)
        return Response('Not Found')
