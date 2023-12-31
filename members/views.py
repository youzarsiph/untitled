""" API endpoints for untitled.members """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from untitled.mixins import OwnerMixin
from untitled.communities.models import Community
from untitled.members.models import Member
from untitled.members.serializers import MemberSerializer


# Create your views here.
class MemberViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete members"""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "user__first_name", "user__last_name"]
    ordering_fields = ["created_at"]
    filterset_fields = ["user", "community", "is_admin", "is_banned"]


class CommunityMembersViewSet(MemberViewSet):
    """Members of a group"""

    def perform_create(self, serializer):
        """Creates a member"""

        community = Community.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, community=community)

    def get_queryset(self):
        """Filter queryset by community"""

        community = Community.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(community=community)


class UserFollowersViewSet(MemberViewSet):
    """Members filtered by user"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
