INSERT INTO category_info (id, name, is_delete) VALUES (1, '科幻', 0);
INSERT INTO category_info (id, name, is_delete) VALUES (2, '学习', 0);

INSERT INTO authinfo (id, name, is_delete) VALUES (1, 'pcw', 0);

INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (1, 'python3核心编程', 68, '2015-10-10', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (2, '流畅的python', 98, '2017-07-15', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (3, 'mysql高性能', 229, '2018-07-09', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (4, 'golang学习笔记', 139, '2017-05-29', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (6, 'linux学习宝典2', 119, '2009-08-13', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (7, '自学python', 98, '2017-07-15', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (8, 'python入门到精通', 168, '2017-07-15', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (9, 'python高级教程', 188, '2017-07-15', 0, 0, 0, 1, 1);
INSERT INTO book (id, title, price, pub_date, commentcount, is_delete, readcount, auth_id, category_id) VALUES (10, '代码架构整洁', 96, '2010-05-15', 0, 0, 0, 1, 2);