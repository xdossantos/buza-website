# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

from buza.models import User
from project.vote.models import VoteModel


# Shortcuts:
_ForeignKey = partial(models.ForeignKey, on_delete=models.CASCADE)


class Board(models.Model):
    '''the model for each class'''

    title = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False)
    users_count = models.IntegerField(default=0)  # number of active users
    questions_count = models.IntegerField(default=0)  # number of questions

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)


class Question(VoteModel, models.Model):
    '''each class has list of questions'''

    title = models.CharField(max_length=100, blank=False)
    description = HTMLField()
    media = models.ImageField(upload_to='questions')  # inside of media
    board = _ForeignKey(Board, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    user = _ForeignKey(User, related_name='asked_by')
    slug = models.SlugField(editable=False)

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def update(self, title, description, media, board, tags, *args, **kwargs):
        self.title = title
        self.description = description
        self.media = media
        self.board = board
        self.slug = slugify(title)
        self.tags = tags
        self.updated_at = timezone.now()
        super(Question, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)


class Answer(VoteModel, models.Model):
    '''users can post questions that will display on the classroom'''

    answer = HTMLField()
    media = models.ImageField(upload_to='answers/')
    question = _ForeignKey(Question, related_name="answers")
    user = _ForeignKey(User, related_name='answered_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('created_at',)


class Comment(models.Model):
    '''a comment can be for a question or an answer'''

    comment = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)


class QuestionComment(Comment):
    '''a comment for a question'''
    user = _ForeignKey(User, related_name='question_commented_by')
    question = _ForeignKey(Question, related_name="question_comments")

    class Meta:
        ordering = ('created_at',)


class AnswerComment(Comment):
    '''a comment for a question'''
    user = _ForeignKey(User, related_name='answer_commented_by')
    answer = _ForeignKey(Answer, related_name="reply_comments")

    class Meta:
        ordering = ('created_at',)
