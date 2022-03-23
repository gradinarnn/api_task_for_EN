from sqlalchemy import Column, Integer, String, ForeignKey, Text, BigInteger




# class Endpoint(Base):
#     __tablename__ = 'endpoint'
#     id = Column(BigInteger, primary_key=True)
#     device_id = Column(Integer, ForeignKey('device.id', ondelete='CASCADE', onupdate='CASCADE'))
#     comment = Column(Text)

def create_table_endpoint():
    return """create table IF NOT EXISTS endpoints
(
    id        bigserial not null
        constraint endpoints_pk
            primary key,
    device_id integer
        constraint endpoints_devices_id_fk
            references devices
            on update cascade on delete cascade,
    comment   text
);

alter table endpoints
    owner to postgres;"""