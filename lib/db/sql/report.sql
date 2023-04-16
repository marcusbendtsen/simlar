

create table report(
 id integer primary key autoincrement,
 search integer not null,
 title text not null,

 foreign key(search) references search(id)
);

