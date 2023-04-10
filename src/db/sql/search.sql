

create table search(
 id integer primary key autoincrement,
 created datetime default current_timestamp,
 database text check( database in ("pubmed") )
);
