from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer

# Register a new user
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if username and password and email:
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)

# Login to get JWT token
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({'error': 'Invalid credentials!'}, status=status.HTTP_400_BAD_REQUEST)

# View list of tasks
@api_view(['GET'])
def task_list(request):
    if request.method == 'GET':
        print("43 : ",request)
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# View a single task
@api_view(['GET'])
def task_detail(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk, user=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

# Create a new task
@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        completed = request.data.get('completed', False)

        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            user=request.user
        )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Update an existing task
@api_view(['PUT'])
def update_task(request, pk):
    if request.method == 'PUT':
        task = Task.objects.get(pk=pk, user=request.user)
        task.title = request.data.get('title', task.title)
        task.description = request.data.get('description', task.description)
        task.completed = request.data.get('completed', task.completed)
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

# Delete a task
@api_view(['DELETE'])
def delete_task(request, pk):
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk, user=request.user)
        task.delete()
        return Response({'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
