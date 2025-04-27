-- Очистка таблиц перед вставкой (опционально, если хотите чистый старт)
TRUNCATE TABLE votes, question_tags, posts, tags, users, roles RESTART IDENTITY CASCADE;

-- Добавление ролей
INSERT INTO roles (name) VALUES
('user'),
('admin');

-- Добавление пользователей
INSERT INTO users (username, email, hashed_password, role_id, reputation, created_at, last_login, is_visible) VALUES
('john_doe', 'john@example.com', 'hashed_password_1', 1, 50, '2025-02-27 10:00:00', '2025-02-27 12:00:00', TRUE),
('jane_smith', 'jane@example.com', 'hashed_password_2', 1, 150, '2025-02-27 11:00:00', '2025-02-27 13:00:00', TRUE),
('admin_user', 'admin@example.com', 'hashed_password_3', 2, 500, '2025-02-27 09:00:00', '2025-02-27 14:00:00', TRUE);

-- Добавление тегов
INSERT INTO tags (name, description) VALUES
('python', 'Questions about Python programming'),
('sql', 'Questions about SQL databases'),
('fastapi', 'Questions about FastAPI framework'),
('docker', 'Questions about Docker containers'),
('webdev', 'General web development topics');

-- Добавление постов (2 вопроса и 1 ответ)
INSERT INTO posts (title, body, author_id, created_at, updated_at, views, is_closed, is_visible, is_accepted, post_type, vote_count, parent_id) VALUES
('How to use FastAPI with SQLAlchemy?', 'I need help integrating FastAPI with SQLAlchemy async.', 1, '2025-02-27 12:00:00', '2025-02-27 12:00:00', 10, FALSE, TRUE, FALSE, 'question', 2, NULL),
('Dockerizing a Python app', 'What’s the best way to dockerize a Python app?', 2, '2025-02-27 13:00:00', '2025-02-27 13:00:00', 15, FALSE, TRUE, FALSE, 'question', 1, NULL),
('Re: How to use FastAPI with SQLAlchemy?', 'Use create_async_engine and async_session_maker.', 3, '2025-02-27 14:00:00', '2025-02-27 14:00:00', 5, FALSE, TRUE, FALSE, 'answer', 1, 1);

-- Добавление связей вопросов с тегами
INSERT INTO question_tags (question_id, tag_id) VALUES
(1, 1), -- "How to use FastAPI with SQLAlchemy?" -> "python"
(1, 3), -- "How to use FastAPI with SQLAlchemy?" -> "fastapi"
(2, 4); -- "Dockerizing a Python app" -> "docker"

-- Добавление голосов
INSERT INTO votes (user_id, post_id, vote_type) VALUES
(1, 1, 'up'),   -- John голосует за вопрос Jane
(2, 1, 'up'),   -- Jane голосует за свой вопрос
(3, 2, 'down'); -- Admin голосует против вопроса Jane


-- Добавление уведомлений
INSERT INTO notifications (user_id, type, relatedpost_id, relateduser_id, message, created_at) VALUES
(1, 'NewAnswer', 1, 3, 'Your question has a new answer.', '2025-02-27 15:00:00'),
(2, 'NewQuestion', 2, 1, 'A new question has been posted.', '2025-02-27 16:00:00'),
(3, 'NewAnswer', 3, 2, 'Your question has a new answer.', '2025-02-27 17:00:00');

-- Добавление закладок
INSERT INTO bookmarks (user_id, post_id, created_at, is_active) VALUES
(1, 1, '2025-02-27 18:00:00', TRUE),
(2, 2, '2025-02-27 19:00:00', TRUE),
(3, 3, '2025-02-27 20:00:00', FALSE);

-- Добавление подписок
INSERT INTO subscriptions (user_id, type, targetuser_id, targetpost_id, created_at, is_active) VALUES
(1, 'user', 2, NULL, '2025-02-27 21:00:00', TRUE),
(2, 'post', NULL, 1, '2025-02-27 22:00:00', TRUE),
(3, 'user', 1, NULL, '2025-02-27 23:00:00', FALSE);