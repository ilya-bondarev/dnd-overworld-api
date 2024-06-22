from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Table, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import Config

Base = declarative_base()

# Role model
class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

# User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    registration_date = Column(DateTime, nullable=False)
    photo_path = Column(String)

    role = relationship('Role')
    characters = relationship('Character', back_populates='user')

# Race model
class Race(Base):
    __tablename__ = 'races'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

# Skill model
class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

# Ability model
class Ability(Base):
    __tablename__ = 'abilities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)

# Character model
class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    race_id = Column(Integer, ForeignKey('races.id'), nullable=False)
    char_class = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    strength = Column(Integer, nullable=False)
    dexterity = Column(Integer, nullable=False)
    intelligence = Column(Integer, nullable=False)
    background = Column(Text)
    
    user = relationship('User', back_populates='characters')
    race = relationship('Race')
    items = relationship('Item', back_populates='character')
    spells = relationship('Spell', back_populates='character')
    character_skills = relationship('CharacterSkill', back_populates='character')
    character_abilities = relationship('CharacterAbility', back_populates='character')

# Associative table for Character-Skill relationship
class CharacterSkill(Base):
    __tablename__ = 'character_skills'
    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    
    character = relationship('Character', back_populates='character_skills')
    skill = relationship('Skill')

# Associative table for Character-Ability relationship
class CharacterAbility(Base):
    __tablename__ = 'character_abilities'
    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    ability_id = Column(Integer, ForeignKey('abilities.id'), nullable=False)
    
    character = relationship('Character', back_populates='character_abilities')
    ability = relationship('Ability')

# Game session model
class GameSession(Base):
    __tablename__ = 'game_sessions'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    game_master_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    description = Column(Text)
    status = Column(String, nullable=False)
    
    game_master = relationship('User')
    players = relationship('Player', back_populates='game_session')

# Item model
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    item_type = Column(String, nullable=False)
    stats = Column(Text)
    character_id = Column(Integer, ForeignKey('characters.id'))
    
    character = relationship('Character', back_populates='items')

# Spell model
class Spell(Base):
    __tablename__ = 'spells'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    level = Column(Integer, nullable=False)
    char_class = Column(String, nullable=False)
    effects = Column(Text)
    character_id = Column(Integer, ForeignKey('characters.id'))
    
    character = relationship('Character', back_populates='spells')

# Associative table for players in game sessions
class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    game_session_id = Column(Integer, ForeignKey('game_sessions.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    
    game_session = relationship('GameSession', back_populates='players')
    character = relationship('Character')

# Location model
class Location(Base):
    __tablename__ = 'locations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    coordinates = Column(String)
    
    events = relationship('Event', back_populates='location')

# Event model
class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    date_time = Column(DateTime, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    
    location = relationship('Location', back_populates='events')

# Monster model
class Monster(Base):
    __tablename__ = 'monsters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    health = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))
    
    location = relationship('Location')
    monster_skills = relationship('MonsterSkill', back_populates='monster')
    monster_abilities = relationship('MonsterAbility', back_populates='monster')

# Associative table for Monster-Skill relationship
class MonsterSkill(Base):
    __tablename__ = 'monster_skills'
    
    id = Column(Integer, primary_key=True)
    monster_id = Column(Integer, ForeignKey('monsters.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    
    monster = relationship('Monster', back_populates='monster_skills')
    skill = relationship('Skill')

# Associative table for Monster-Ability relationship
class MonsterAbility(Base):
    __tablename__ = 'monster_abilities'
    
    id = Column(Integer, primary_key=True)
    monster_id = Column(Integer, ForeignKey('monsters.id'), nullable=False)
    ability_id = Column(Integer, ForeignKey('abilities.id'), nullable=False)
    
    monster = relationship('Monster', back_populates='monster_abilities')
    ability = relationship('Ability')

# Create engine and database
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()