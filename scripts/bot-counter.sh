zcat *.gz | \
	cat - *.log *.log.1 | \
	cut -d' ' -f12- | \
	grep -i "bot" | \
	sort | \
	uniq -c | \
	sort -rn | \
	head
