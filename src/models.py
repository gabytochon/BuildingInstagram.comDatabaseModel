import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column (String(250), nullable=False)
    password = Column (String(250), nullable=False)
    posts = relationship("Post")
    stories = relationship("Story")
    comentarios = relationship("Comentario")
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column (String(250), nullable=False)
    texto = Column (String(250), nullable=True)
    locacion = Column (String(250), nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_comentario = Column(Integer, ForeignKey('comentario.id'))
class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    image = Column (String(250), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_comentario = Column(Integer, ForeignKey('comentario.id'))
class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    texto = Column (String(250), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'))
    id_story = Column(Integer, ForeignKey('story.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    posts = relationship("Post")
    stories = relationship("Story")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')