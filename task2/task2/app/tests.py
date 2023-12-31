from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile, Project, Task, Document, Comment

User = get_user_model()

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("testpassword"))

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, role="manager")

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.role, "manager")

class ProjectModelTestCase(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(title="Test Project", description="Test Description", start_date="2023-01-01", end_date="2023-02-01")
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.description, "Test Description")

class TaskModelTestCase(TestCase):
    def test_task_creation(self):
        project = Project.objects.create(title="Test Project", description="Test Description", start_date="2023-01-01", end_date="2023-02-01")
        task = Task.objects.create(title="Test Task", description="Test Task Description", status="open", project=project)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "open")

class DocumentModelTestCase(TestCase):
    def test_document_creation(self):
        project = Project.objects.create(title="Test Project", description="Test Description", start_date="2023-01-01", end_date="2023-02-01")
        document = Document.objects.create(name="Test Document", description="Test Document Description", version="1.0", project=project)
        self.assertEqual(document.name, "Test Document")
        self.assertEqual(document.version, "1.0")

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpassword")
        self.project = Project.objects.create(title="Test Project", description="Test Description", start_date="2023-01-01", end_date="2023-02-01")

    def test_comment_creation(self):
        comment = Comment.objects.create(text="Test Comment", author=self.user, project=self.project)
        self.assertEqual(comment.text, "Test Comment")
