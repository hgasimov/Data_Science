SELECT SUM(doc1.count * doc2.count)
FROM frequency doc1, frequency doc2
WHERE doc1.docid = '10080_txt_crude' and
	  doc2.docid = '17035_txt_earn' and
	  doc1.term = doc2.term;

SELECT MAX(sim_mat.similarity)	  
FROM (
	SELECT doc1.docid, SUM(doc1.count * doc2.count) similarity
	FROM frequency doc1, (	
		SELECT 'q' as docid, 'washington' as term, 1 as count 
		UNION
		SELECT 'q' as docid, 'taxes' as term, 1 as count
		UNION 
		SELECT 'q' as docid, 'treasury' as term, 1 as count
	) doc2
	WHERE doc1.term = doc2.term
	GROUP BY
		  doc1.docid
) sim_mat;