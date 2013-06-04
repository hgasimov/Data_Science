SELECT count(*) FROM (frequency) where docid = '10398_txt_earn';

SELECT count(*) FROM (frequency) where docid = '10398_txt_earn' and count = 1;

SELECT count(*) FROM 
	(
	 SELECT * FROM (frequency) where docid = '10398_txt_earn' and count = 1
		UNION
	 SELECT * FROM (frequency) where docid = '925_txt_trade' and count = 1
	);

SELECT count(*) FROM (frequency) where term = 'parliament';

SELECT count(*) FROM (
		SELECT docid, SUM(count) total FROM (frequency) GROUP BY docid HAVING total > 300
	);

SELECT count(*) FROM (frequency) where docid IN (
		SELECT docid FROM (frequency) where term = 'transactions'
	) and term = 'world';