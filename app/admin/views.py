from sqladmin import ModelView
from app.bookmark.models import Bookmark
from app.database import Base
from app.notification.models import Notification
from app.posts.models import Post
from app.questiontags.models import QuestionTag
from app.subscription.models import Subscription
from app.users.models import User
from app.users.roles.models import Role
from app.tags.models import Tag
from app.votes.models import Vote




class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.reputation, User.role]
    column_labels = {User.role: "Название роли"} # Способ отображения Роли не по цифре а по Имени
    column_searchable_list = [User.username, User.email]
    column_sortable_list = [User.id, User.reputation]
    column_details_exclude_list = [User.hashed_password]

    page_size = 20
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    can_delete = False


class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title, Post.body, Post.author_id, Post.post_type, Post.vote_count]
    column_searchable_list = [Post.title, Post.post_type]
    column_filters = [Post.post_type, Post.is_visible]
    page_size = 20
    name = "Пост"
    name_plural = "Посты"
    icon = "fa-solid fa-file-alt"


class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name]
    name = "Роль"
    name_plural = "Роли"
    page_size = 20
    icon = "fa-solid fa-shield-alt"


class TagsAdmin(ModelView, model=Tag):
    column_list = [Tag.id, Tag.name, Tag.description]
    name = "Тэг"
    name_plural = "Тэги"
    page_size = 20
    icon = "fa-regular fa-clipboard"


class QuestionTagsAdmin(ModelView, model=QuestionTag):
    column_list = [QuestionTag.id, QuestionTag.question_id, QuestionTag.tag_id]
    name = "Вопрос/Ответ"
    name_plural = "Вопросы/Ответы"
    page_size = 20
    icon = "fa-regular fa-chart-bar"


class VotesAdmin(ModelView, model=Vote):
    column_list = [Vote.id, Vote.user_id, Vote.post_id, Vote.vote_type]
    name = "Голос"
    name_plural = "Голоса"
    page_size = 20
    icon = "fa-regular fa-thumbs-up"    


class NotificationAdmin(ModelView, model=Notification):
    column_list = [Notification.id, Notification.user_id, Notification.type, Notification.relatedpost_id, Notification.relateduser_id, Notification.message, Notification.created_at]
    column_searchable_list = [Notification.message, Notification.type]
    column_sortable_list = [Notification.created_at]
    page_size = 20
    name = "Уведомление"
    name_plural = "Уведомления"
    icon = "fa-solid fa-bell"


class BookmarkAdmin(ModelView, model=Bookmark):
    column_list = [Bookmark.id, Bookmark.user_id, Bookmark.post_id, Bookmark.created_at, Bookmark.is_active]
    column_searchable_list = [Bookmark.user_id, Bookmark.post_id]
    column_sortable_list = [Bookmark.created_at]
    page_size = 20
    name = "Закладка"
    name_plural = "Закладки"
    icon = "fa-solid fa-bookmark"


class SubscriptionAdmin(ModelView, model=Subscription):
    column_list = [Subscription.id, Subscription.user_id, Subscription.type, Subscription.targetuser_id, Subscription.targetpost_id, Subscription.created_at, Subscription.is_active]
    column_searchable_list = [Subscription.user_id, Subscription.type]
    column_sortable_list = [Subscription.created_at]
    page_size = 20
    name = "Подписка"
    name_plural = "Подписки"
    icon = "fa-solid fa-rss"