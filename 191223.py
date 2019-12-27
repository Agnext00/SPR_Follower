・パワーメータ
PM320E：インタフェースはUSB
・ステージコントローラ
CSG-602R：インタフェース　RS232C
シリアルUSB変換ケーブルでUSBに変換する必要がある。
【外部装置入出力の基本】
基本：USBにしろ何にしろ、PCのポートでインタフェースを抽象化する
ポートをファイル的に扱う
ポートを開く（ファイルを開く的な）
ポートに書き込む（ファイルに書き込む）
ポートを読む（ファイルを読む）
ポートを閉じる（ファイルを閉じる）
Windowsの場合
シリアルポートは、往々にしてCOMポートとして扱われます。
基本はCOMポート番号で指定するのがセオリー、、、だが。
Windowsはデバイスマネージャーでポートの状態を確認
ATEN USB to Serial Bridge(COM6)　ただし、COM番号は機器依存　⇒　ステージコントローラ
ただし、PM320EはUSBでつないでいるけど、エラーが。。。
⇒NI（National Instruments）が作った、VISAというインターフェス規格に則り、アクセス可能。
PythonでVISA関連のモジュールをインポートして、PCにつながっているVISA機器のリストを出してくれる関数がある
これを使うと、PM320Eに、どのような名前でアクセスすればよいかわかる。
---------------Python環境・PM320E-------------------------------------------------------------
Anaconda >> JupyterLab
でファイル（拡張子 .ipynb）を開く
そのプログラムが書いてあるセルにカーソルを合わせて、Shift+Controlでプログラムが実行されます。
# PM320Eとの交信プログラム
import visa #呪文です。
path = 'data.txt' #保存先のテキストファイルのパス。
rm = visa.ResourceManager('C:/Program Files (x86)/IVI Foundation/VISA/WinNT/agvisa/agbin/visa32.dll')
# 良く変わらないけれど、リソースマネージャのオブジェクトが生成されます。
# C:/Program　以降は環境依存。PM320E関連のソフトをThorlabsでインストールする。dllはインストールされる。
# たぶんhttps://www.thorlabs.co.jp/software_pages/viewsoftwarepage.cfm?code=PM300　の何かをインストールする必要がある。
print(rm.list_resources()) # rm.list_resources()　でVISA接続リストを出してくれる。PM320Eもこれで出てくる。
dso = rm.open_resource('USB0::0x1313::0x8022::M00512252::INSTR') # 装置をファイル的にOPENする。OPENの文法はVISA書式に準じる。
s = dso.query("*IDN?")　# dso.query('命令名')　命令名は装置のマニュアルを読む。
print(type(s))
with open(path, mode='w') as f:
    f.write(s)
with open(path) as f:
    print(f.read())
-----------------Python環境・ステージコントローラ--------------------------------------------
import serial
import time
ser = serial.Serial("COM6", baudrate=9600, parity=serial.PARITY_NONE,
                    bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE,
                    timeout = None, xonxoff = 0, rtscts = 0,)
# ここらへんは動かさなくてもよいだろう。
本日の技術移転のログ
