# 05_orm.py
from sqlalchemy import create_engine, String, func, asc, desc
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

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]    # 特に指定がなければmapped_columnは不要。※= Columnは古い。
    address: Mapped[Optional[str]]  # Optionalでnull許容（defaultはNOT NULL）

    # memo:実際に実行されるCREATE文に AUTO INCREMENT の記載がないが、
    # 問題はない。これは、SQLiteが、INTのPRIMARY KEYは自動的に
    # AUTO INCREMENTの扱いになるという仕様による。
    # なので、「, autoincrement=True」自体も不要だが、
    # もし自動採番したくない場合には、これをFalseとする必要がある。

# テーブルの生成
Base.metadata.create_all(bind=engine)

# 登録
# with Session(engine) as session:
#     user = User(name='b', age=25, address='神奈川')
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

    # .all()あり→全件一括取得＝スピード〇、メモリ×
    #  →usersの形で、別のプログラムに受け渡すときに使う（ほぼこっち）。
    # .all()なし→１行ずつ取得＝スピード×、メモリ〇
    #　→データ量がものすごい多い（何千、何万の）ときに使う。
    # ※別件、こっち(.all()なし)はsessionのwith文の中で用いる縛りがある。
    # memo: 遅延closeや、クエリの遅延評価などで、with文の外でも動いてしまう
    # ことがあるが、これはたまたまなのでNG。

    # .first で最初の１件のみ取得
    user = session.query(User).first()
    print(user.id, user.name, user.age, user.address)
    # 0件の場合Noneのため、
    # ガチガチに組むなら if user: といった
    # チェック処理が必要

    # .scalar でスカラー（単一）値取得
    count = session.query(
        func.count(User.id)
        ).scalar()
    print(count)

    # COUNT(*)は↓
    count = session.query(
        # count('*')だと全部の列って意味だからどのテーブルかわからない → .select_from(User) が必要
        func.count('*')
    ).select_from(User).scalar()
    print(count)

    # .limit で取得件数絞り込み
    # 2件まで表示
    users = session.query(User).limit(2).all()
    # .all じゃなくてもOKだけど、つけるなら .all は最後
    for user in users:
        print(user.id, user.name, user.age, user.address)

    # .limit().offset() で途中＆取得件数絞り込み
    # 2件まで表示
    # 0□1□2□3 だから↓だと２番目と３番目が取れる
    # ほしい数-1 * 10 でできる
    users = session.query(User).limit(2).offset(1).all()
    for user in users:
        print(user.id, user.name, user.age, user.address)

    # 列指定取得
    for user in session.query(User.id, User.name).all():
        print(user.id, user.name)

    # .filter で条件指定(WHERE)
    for user in session.query(User).filter(User.id == 2).all():
        print(user.id, user.name, user.age, user.address)
    
    # AND
    for user in session.query(User).filter(User.id == 3, User.name == 'a').all():
        print(user.id, user.name, user.age, user.address)
    
    # IN
    ids = [2, 3, 5]
    for user in session.query(User).filter(User.id.in_(ids)).all():
        print(user.id, user.name, user.age, user.address)
    
    # ORDER BY
    # もし入れるなら.filterの後に書く
    for user in session.query(User).order_by(desc(User.id)).all():
        print(user.id, user.name, user.age, user.address)

    # ORDER BY2
    for user in session.query(User).order_by(desc(User.name), asc(User.id)).all():
        print(user.id, user.name, user.age, user.address)

    # filter & ORDER BY
    for user in session.query(User).order_by(desc(User.id)).all():
        print(user.id, user.name, user.age, user.address)