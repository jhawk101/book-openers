-- name: get-books
SELECT
    gutenbergbookid,
    t.name
FROM
    subjects s
    LEFT JOIN book_subjects bs ON s.id = bs.subjectid
    LEFT JOIN books b ON bs.bookid = b.id
    LEFT JOIN titles t ON b.id = t.bookid
    LEFT JOIN languages l ON l.id = b.languageid
WHERE
    s.name LIKE '%fiction%'
    AND l.name = 'en';

