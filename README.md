# MA Crossover Signal

本项目基于 Python 的 `yfinance` 和 `pandas` 库，生成 AAPL、TSLA 等股票的 5/10 日均线交叉买入信号，并进行可视化。

## 功能特色

- 支持 5/10 日均线的计算
- 自动识别“金叉”买入信号
- 输出买点数据，支持保存为 CSV 文件
- 图像展示股票价格及均线交叉点
- 支持更换任意股票代码与周期（如 main("MSFT", "2y")）

## 使用方法

运行如下命令生成图表与 CSV 文件：


**常见的库**
1.金融库：yfinance --用于从 Yahoo Finance 获取股票、指数等数据。
2.pandas --用于数据分析和处理的
3.Matplotlib：用于数据可视化

**df**
df = yf.download("AAPL", period="1y") **用于从yf中下载AAPL的股票数据，其中df是pandas库的数据框对象**

**df['a']:**
创建a这一列/选取出a这一列

**什么是 语句：rolling（window 参数）？**
对数据进行滚动窗口计算，窗口大小为 5，每次计算时考虑连续的 5 个数据点

**plot**是 Pandas DataFrame 的绘图方法，用于绘制折线图
使用eg：**df['Close'].plot(title='AAPL 收盘价走势')**即标题为“AAPL收盘价走势”的收盘价折线图

**plt.show()**
用于在屏幕上显示图表，否则只会显示在后台，不会绘制

**n日移动平均线的计算**
df['MA5'] = df['Close'].rolling(window=5).mean()   
df['MA10'] = df['Close'].rolling(window=10).mean() 
创建MA5列，选取close这一列的数据进行滚动计算，计算窗口 为连续的5个数据点，最后计算其平均值

**plt.scatter(buy_signal.index, buy_signal['Close'], color='red', label='Buy Signal', marker='^')**#绘制散点图并设置属性
1.scatter(x,y):
 x是日期,y是值（横纵坐标）

2.marker='^'
定义了散点的形状，'^' 表示使用向上的三角形标记。

3.color='green'
定义了散点的颜色，这里设置为绿色。

4.label='Buy Signal'
定义了散点图的图例标签，用于在图例中显示这些散点代表的含义，这里是“买入信号”。

**Q1：为什么散点标记有时不在MA的交叉点上？**
Buy_signal['Close']
使用的是 收盘价的值，而不是 MA5 或 MA10 的值
**在一个代码窗格中，三线合一**
df[['Close', 'MA5', 'MA10']].plot(title='AAPL 收盘价 + MA5/MA10', figsize=(10, 5))
=
plt.plot(df['Close'], label='Close') #画出Close的折线图，并设置标签
plt.plot(df['MA5'], label='MA5') #画出MA5的折线图，并设置标签
plt.plot(df['MA10'], label='MA10') #画出MA10的折线图，并设置标签