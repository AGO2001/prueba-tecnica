create table if not exists tasks(

    id serial primary key,
    title varchar(120) not null,
    priority varchar(10) not null default 'medium' check (priority in ('low', 'medium', 'high')),
    done boolean not null default false,
    created_at timestamp with time zone default current_timestamp
)