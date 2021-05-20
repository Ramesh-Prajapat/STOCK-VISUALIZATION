import yfinance as yf
import MySQLdb
db = MySQLdb.connect("localhost", "root", "Qp$_a400", "data_visualization")
cur = db.cursor()
comp_name_file = open("nifty_fifty.txt")
for ticker in comp_name_file.readlines():
    tic = ticker.rstrip()
    full_name = "{}.NS".format(tic)
    print(full_name)
    df = yf.download(full_name, start="2019-01-01",end="2021-01-01")
    df_columns = df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    index = df.index
    all_date = list(index)
    total_row = len(all_date)
    all_data = []
    for i in range(total_row):
        ddate = str(all_date[i]).split(" ")[0]
        open = '%.5f' % df_columns["Open"][i]
        high = '%.5f' % df_columns["High"][i]
        low = '%.5f' % df_columns["Low"][i]
        close = '%.5f' % df_columns["Close"][i]
        adj_close = '%.5f' % df_columns["Adj Close"][i]
        volume = df_columns["Volume"][i]
        all_data.append((tic, ddate, open,high,low,close,adj_close,volume))
    #print(all_data)
    ad = all_data
    for i in range(len(ad)):
        try:
            cur.execute(('INSERT INTO page1_russelldata(TICKER, D_DATE, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE, VOLUME) VALUES("{}","{}",{}, {}, {}, {}, {}, {})').format(ad[i][0], ad[i][1], ad[i][2], ad[i][3], ad[i][4], ad[i][5], ad[i][6], ad[i][7]))
            db.commit()
        except:
            pass
db.close()
