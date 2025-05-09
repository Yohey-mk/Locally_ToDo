#Locally_ToDo
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# メモリ上にToDoリストを保持（起動中のみ）
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todo_list):
        todo_list.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)




#Check List
#Things to work on
#Local環境でシェアできるToDoList
#たとえば、同じWi-Fiに接続している、またはユニークIDを生成して、そのIDを共有するとToDoListの中身がシェアされるイメージ
#✅ 実現方法の概要
#
#1. Webアプリとして作成する
#
#PythonのFlaskやFastAPIを使ってWebアプリを立てます。
#→ 他のデバイスも、同じネットワーク内でブラウザからアクセス可能になります。
#
#2. ToDoデータを共有するしくみ
#
#以下のいずれかの方法で共有可能です：
#	•	🔗 共有ID方式
#ユーザーがタスクを追加したときに、ユニークなID（例：6桁の英数字）を生成し、そのIDでタスクリストを管理。
#他の人がそのIDを使ってアクセスすれば、同じToDoリストを閲覧・編集できる。
#	•	📡 IPアドレス方式（ローカル限定）
#Flaskアプリをhost='0.0.0.0'で立ち上げれば、同じWi-Fi内の他のPCやスマホからhttp://あなたのIPアドレス:ポート番号でアクセス可能です。
#
#⸻
#
#🔧 使用技術の候補
#Webアプリ:Flask / FastAPI
#フロントエンド: HTML + JavaScript + Bootstrap（簡易）
#データ保存: Pythonの辞書（開発中）or SQLite or JSONファイル
#ID生成・共有: uuidモジュール or 短縮ID生成ライブラリ
#同時編集対策: 単純にロック処理、またはリアルタイム化したければ SocketIO
#💡 ユースケース例（流れ）
#	1.	ユーザーAがToDoリストを作る → 自動で「共有ID」が生成される（例：abc123）
#	2.	同じWi-Fi内のユーザーBが、スマホやPCで http://192.168.1.20:5000/abc123 にアクセス
#	3.	双方が同じリストを編集・確認できる
#
#⸻
#
#🚀 最初の一歩
#
#以下のようなステップで開発を始められます：
#	1.	Flaskで簡単なToDoリストを作る（ローカルで動作）
#	2.	複数リストに対応し、「IDごとに別リストを持つ」機能を追加
#	3.	host='0.0.0.0' で起動し、同ネットワーク内で共有できるようにする
#	4.	必要に応じてデータ保存やセキュリティを追加
#
#✨ ボーナスアイデア（将来的に）
#	•	👥 同時アクセスに備えたリアルタイム更新（Socket.IO）
#	•	🔒 編集権限のパスコード（読み取り専用モードなど）
#	•	☁️ 最終的にクラウド化（HerokuやRenderにデプロイ）
#	•	☁️ iOS App化とかもできる？