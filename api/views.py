from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'POST': ' api/users/token'}
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)