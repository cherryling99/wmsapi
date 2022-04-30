# WMS API
請先看過MetaAPI的說明影片：\
https://youtube.com/playlist?list=PLMnYs2gmXPpjZzZNBYTUZNpS82PrF0pY6

本次說明影片:\
https://youtube.com/playlist?list=PLMnYs2gmXPphbviYQXfj1zQuvmHHmjNCz

## 1. 系統架構
請參考 docs/WmsAPI.pptx

## 2. 目錄結構
請參考 docs/WmsAPI.pptx

### 程式開發步驟
#### 1. wms API
用途 ： 做API 給wms呼叫
1. 釐清用途，準備傳入資料格式、輸出資料格式
2. 傳入資料格式 ： 寫在schemas.py，宣告資料格式，繼承pydantic BaseModel。使用了深層巢狀的資料模型，做法請詳讀：
  - https://fastapi.tiangolo.com/tutorial/body-nested-models/#deeply-nested-models
3. 路由寫在main.py，路徑依照wms給的規格中的事件名稱
4. 傳入資料經過pydantic檢查，使用物件的屬性方式讀取。
5. 讀寫資料庫盡量使用sqlalchemy的orm方式，在models.py宣告資料class，繼承sqlalchemy declarative_base
6. 事件觸發商業邏輯，必定是資料庫的讀取、邏輯判斷、寫入、回傳，寫在crud.py。
7. 回傳資料用dict list人工組成，這部分沒有使用套件來做，是苦工。

##### 注意事項
程式是異步，但資料卻要同步，ERP資料同步問題。 \
不要設計成update資料，儘量都是寫入資料，也成為log資料。 因為wms沒有紀錄，以後要查資料都要從erp來查。
這有好處也有壞處：
- 好處是wmsapi 只擔任掮客，甚少商業邏輯，也不需要處理雙方資料同步問題，讓資料同步問題交給erp與wms各自處理，雙方有問題的資料留在各自系統，留有人工校正的空間。
- 壞處是會產生資料不同步，雙方呼叫了半天也不能解決問題，需要人工處理。對wmsAPI來說，這點也不是壞處。

##### todo:
- [ ] erp要做紀錄檔的purge處理
- [ ] 本範例沒有做concurrent的架構，如果WMS瘋狂的呼叫，就會異步的去執行，可能會產生資料重複問題，這等到整個系統分析完成之後再決定要不要做管控。不一定需要，可以用資料庫的transaction控制。 


#### 2. tasks
用途 ： 排程由ERP讀取代辦事項，呼叫WMS，並將結果寫入ERP的事件紀錄檔。
1. 釐清用途，準備傳入資料格式、輸出資料格式
2. 傳入資料，用用dict list人工組成這部分沒有使用套件來做，是苦工。可能會有巢狀迴圈組成，請參考e2w_pcom.py的get_message()。如果要用其他方法也行，要統一作法即可，不要每個人用不同的方法，這樣維護起來很累人。
3. 回傳的資料是dict，按照規定的格式去解析結果，這也是苦工。但是回傳資料的架構相對單純，應該不是問題。如果有實作上的困難再提出來。
4. 讀寫資料庫，先在models.py宣告資料class，儘量用ORM方式來做，用core也可以，但儘量不要用text。讀取資料儘量由ERP做好View，用簡單的查詢就可以取得，不要串好幾個table或是subquery。
5. 將task註冊於celery，由flower來做維護管理

##### todo:
- [ ] 回傳資料dict的解析，如果需要範例再提出

## 3. 資料庫操作
主要參考這一篇，目錄結構基本上跟教學是一樣的，資料模型都在models.py中宣告。\
https://fastapi.tiangolo.com/tutorial/sql-databases/

sqlalchemy也不是簡單幾句可以帶過，如果在開發過程中遇到問題請再提出，我再給實際上的解決辦法。

sqlalchemy的操作請詳讀：
  - https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/
  - https://docs.sqlalchemy.org/en/14/orm/queryguide.html#selecting-orm-entities-and-attributes

另外在docs目錄有兩個pdf檔，遇到問題時可以查一下範例。
1. SQLAlchemy完全入門.pdf
2. sqlalchemy增刪改查.pdf

或是可以問emma、實習生。

## 4. Mock ERP DB
在架構階段，我簡單的用WMS傳回的資料結構模擬開中介檔規格，用postgresql資料庫。\
實際的架構會更多欄位，但基本上都是表頭表身一對多的架構，這樣的假架構應該是足夠做範例使用。
### 準備mock db
create_mock_erp_db.sql

模擬ERP資料表：
1. 只讀取
2. 只新增，盡量不要設計成update資料。

程式是異步，但資料卻要同步，ERP資料同步問題。\
還是先請做整個整合的系統分析之後再決定解決方法。

## 5. WMS api
### token
呼叫與回傳都需要驗證token\
token的產生方法：
1. 動態取得，一段時間失效。必須要有一個取token的機制
2. 固定token

#### todo:
- [ ] token的驗證做法有兩種，需要跟廠商確認
1. 寫一個驗證function
2. 用裝飾器來驗證

### pydantic
schemas.py\
如果閱讀官方文件有困難，則看教學影片：\
https://www.imooc.com/learn/1299

此教學其實是照著官方tutorial文件所講解，最後有實做一個新冠病毒的系統。我的架構基本上也跟他一樣，但是用的技術更少。先看影片有個概念，需要用到再去詳讀。\
https://fastapi.tiangolo.com/tutorial/

## 6. Tasks
task與FastAPI沒有關係，是獨立於FastAPI，使用的技術有：
1. sqlalchemy
2. requests

requests的官方文檔：/
https://docs.python-requests.org/en/latest/

我用的很簡單，網路上有很多範例，我只用post方法。如果遇到技術問題請提出來，再依需要去研究解決方法。

### Mock WNS API
模擬WMS API傳回資料，先只判斷有回傳資料，目前沒有辦法做到測試資料。\
這是因為目前沒有WMS測試環境的關係，所以用FastAPI做模擬，沒有資料格式檢查，不管傳入什麼都直接回傳範例message。

## 7. celery
有關celery的操作請閱讀 docs/celery.pptx，還有影片，有三篇celery與MetaAPI：
https://youtube.com/playlist?list=PLMnYs2gmXPpjZzZNBYTUZNpS82PrF0pY6

##### todo:
- [ ] celery預設保存1天的資料於redis，要統計全部tasks每天執行的次數，如果有每分鐘排程的task，這樣資料就會太多，要縮短redis保存的紀錄時間，存個8小時甚至更短也可以。
- [ ] flower啟動時要設定管理員帳號密碼，目前沒有設，要跟尚師討論做法。
- [ ] flower的詳細用法尚待研究，它可以在UI新增worker，或是中斷與重啟排程，需要研究，以方便日後維護。我想了一下還是有介面可以維護tasks比較輕鬆，不用檢查log，方便多了。

0. 啟動redis
1. wmsapi app 啟動

2. celery worker 啟動，在程式目錄下執行
    ```
    celery -A app_celery.celery worker --loglevel=info --pool=solo
    ```
3. 啟動flower， 開始監控
    ```
    celery --broker=redis://localhost:6379/0 flower --port=5566
    ```
4. 啟動排程beat
    ```
    celery -A app_celery.celery beat -l info -s celery_log/celerybeat-schedule
    ```
5. 大功告成\
開啟flower，查看排程啟動狀況\
http://127.0.0.1:5566

## 8. Testing
分別對API與Tasks做測試，都是簡單的測試是否回傳成功，回傳資料類型是否正確，沒有真的做單元測試。也就是說沒有做邏輯檢查、輸入輸出的商業邏輯檢查。\
這留到系統分析完成之後再考慮要怎麼做測試。

Terminal執行：
```
coverage run -m pytest
coverage report -m
coverage html
```
到htmlcov看報表

### todo:
- [ ] test要做到什麼程度？ 做得到的程度？

## 9.測試、正式環境資料庫切換
app啟動時可以下命令、或是判斷環境，切換到正確的資料庫。
目前使用dotenv，讀環境變數。所以.env不要上傳gitlab儲存庫，尚師會在作業系統設定環境變數， 部署自動化(待討論團隊工作方法)

### todo:
- [ ] CI/CD，要跟尚師討論

## 10. 其他Todo
- [ ] requirement.txt，我是用pycharm自動產生，多有疏漏，需要人工檢查編寫，注意編碼要是utf-8。環境安裝備忘我則寫在 docs/install_memo.txt。但我不確定全部步驟都有記錄到。sorry，這是因為我已經有fastapi的python虛擬環境。
- [ ] tasks中的add.py沒有用處，我只是用來測試celery是否正常，可以刪除，同時要刪除celeryconfig.py中的task註冊。

## 11. 感想
ERP與WMS有兩個整合方式：
1. WMS直接存取ERP的中介檔
2. 新增WmsAPI作為ERP的擴充，幫ERP做API與WMS整合

這兩種方式的優缺點為何？

方案一是最省事的，只要ERP把中介檔資料結構開出來，寫好資料傳輸，接下來都是WMS廠商的事了，這我們在MES也做過。
但是事情並不是想象中那麼簡單，廠商要負責搞清楚整個作業流程，這是他們很難也不願意做的，照導致整合系統有很多例外沒有考慮，有很多測試需要時間驗證。
其實就是廠商會切割問題，還有廠商的工程師都相對年輕，做的程式漏洞百出，需要時間除錯。
當我方的工程師也是菜鳥時更慘，常做出人意料的程式與方案。

方案二則是將責任完全由我方負責，廠商只要做好他自己的事情即可。此時WMS可以視為獨立的系統，日後作業流程變更、甚至是ERP轉換，或是出貨系統從ERP獨立出來都不影響WMS。
但是我方要做的事就多了，要替ERP做API，接受呼叫還要呼叫WMS，原先ERP的流程整合也沒有少，此方案真的對嗎？

方案二是對的，問題就在做得來或是做不來。

我們團隊也不能死守ERP PL/SQL，必須熟練一種語言、框架。首選是ruby，使用ruby on rails框架，因為已經有團隊成員在使用，POS G2的開發有已經好幾年了，可以用享資源。
但是，我們做整合並不是目的，而是過程。我期望公司的資料可以用人工智慧來提取，預測分析、推薦系統，而人工智慧資源最多的是python。我想做AI已經好幾年了....資訊這行業是要一直進步的，不能停滯。

而團隊成員的是沒有能力可以熟捻多種語言的，這就變成我希望以後可以用python做人工智慧，而現階段的整合需求又是用rails最多資源的窘境。

選擇python做整合，對大家來說是一個挑戰，期望大家要多努力，學到的技術是自己的，好了，講太多是嘮叨。
