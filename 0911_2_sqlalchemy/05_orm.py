# 05_orm.py
from sqlalchemy import create_engine, String, func, desc
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from typing import Optional

# engineの作成(DB接続の必要情報定義)
engine = create_engine(
    'sqlite:///user2.db',
    echo=True
)

# モデルの元クラスを作成
class Base(DeclarativeBase):
    pass

# Baseクラスを継承して、
# テーブル用のクラスを定義する
class User(Base):
    __tablename__ = 'user'

    # autoincrementが以下でないと有効化されない。
    # ※officialに書かれていない。officialではmapped_column(primary_key=True, autoincrement=True)だけど、効かない。
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]    # 特に指定がなければmapped_columnは不要。※= Columnは古い。
    address: Mapped[Optional[str]]  # Optionalでnull許容（defaultはNOT NULL）

# テーブルの生成
Base.metadata.create_all(bind=engine)

# 登録
# with Session(engine) as session:
#     user = User(name='a', age=20, address='東京')
#     session.add(user)
#     session.commit()

# 抽出
with Session(engine) as session:
    # session.queryを使って１行ずつ取得する
    for user in session.query(User):
        print(user.id, user.name, user.age, user.address)
    
    # .all()付与で全件取得
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name, user.age, user.address)