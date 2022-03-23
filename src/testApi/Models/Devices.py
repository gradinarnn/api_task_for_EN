
from sqlalchemy import Column, Integer, String, ForeignKey, Text, BigInteger
from sqlalchemy.dialects.postgresql import MACADDR
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index



# class Device(Base):
#     __tablename__ = 'device'
#     id = Column(BigInteger, primary_key=True)
#     dev_id = Column(String(17), nullable=False)
#     dev_type = Column(String(120), nullable=False)
#
#
# Index('devices_dev_id_dev_type_index', Device.dev_id, Device.dev_type)


def create_table_device():
    return """create table IF NOT EXISTS devices
(
    id       bigserial    not null
        constraint devices_pk
            primary key,
    dev_id   varchar(200) not null,
    dev_type varchar(120) not null
);

alter table devices
    owner to postgres;

create index IF NOT EXISTS devices_dev_id_dev_type_index
    on devices (dev_id, dev_type);"""


