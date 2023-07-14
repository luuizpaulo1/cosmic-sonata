import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserScore:
    name: str
    score: int
    created_at: datetime


class DB:
    def __init__(self):
        self.con = sqlite3.connect("db.db")
        self.cur = self.con.cursor()

    def create_user_score_table(self, ):
        self.cur.execute("CREATE TABLE IF NOT EXISTS scores(name , score, created_at)")
        self.con.commit()

    def get_top_5(self, ) -> list[UserScore]:
        stmt = f"SELECT name, score, created_at FROM scores ORDER BY score DESC LIMIT 5"
        res = self.cur.execute(stmt)
        fetch = res.fetchall()
        user_scores = []
        for i in fetch:
            user_scores.append(UserScore(*i))
        return user_scores

    def save_user_score(self, user_score: UserScore):
        stmt = f"INSERT INTO scores VALUES('{user_score.name}', {user_score.score}, '{user_score.created_at}')"
        self.cur.execute(stmt)
        self.con.commit()
        print("Saved successfully")
