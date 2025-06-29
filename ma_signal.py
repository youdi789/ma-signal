# 导入相关库
import yfinance as yf              # 导入yf库（用于从Yahoo Finance获取股票数据）
import pandas as pd               # 导入pd库（用于数据处理）
import matplotlib.pyplot as plt   # 导入 matplotlib 库用于数据可视化
import os                         # 用于文件夹操作

# 封装函数，def是python定义函数的关键字，函数名为获取信号，接收一个df作为参数
# 将 计算日均线 和 买入信号 封装成函数，方便复用
def get_signal(df):
    df['MA5'] = df['Close'].rolling(window=5).mean()    # 计算5日均线
    df['MA10'] = df['Close'].rolling(window=10).mean()  # 计算10日均线
    # 计算是否出现“金叉”：MA5 上穿 MA10
    # 命名买入信号布尔列：Buy，其同时满足 MA5>MA10 且 前一天MA5<=MA10 时，存在买入信号
    df['Buy'] = (df['MA5'] > df['MA10']) & (df['MA5'].shift(1) <= df['MA10'].shift(1))
    return df

# 可视化函数：绘制三线图 + 散点图（买点）
def plot_signals(df, symbol):
    buy_signal = df[df['Buy'] == True]  # 提取买入信号行

    # 绘制收盘价 + 均线图
    df[['Close', 'MA5', 'MA10']].plot(title=f'{symbol} 收盘价 + MA5/MA10', figsize=(10, 5))
    plt.grid()
    plt.show()

    # 信息点可视化，叠加散点图
    plt.figure(figsize=(10, 5))               # 建立图窗
    plt.plot(df['Close'], label='Close')      # 画出Close的折线图，并设置标签
    plt.plot(df['MA5'], label='MA5')          # 画出MA5的折线图
    plt.plot(df['MA10'], label='MA10')        # 画出MA10的折线图
    plt.scatter(buy_signal.index, buy_signal['Close'], color='red', label='Buy Signal', marker='^')  # scatter绘制散点图，并设置属性
    plt.legend()                              # 产生图例
    plt.title(f'{symbol} Buy Signal Based on MA Crossover')
    plt.grid()
    plt.show()

# 主函数：输入股票代码和时间周期，输出买点分析图 + 保存 CSV
def main(symbol, period="1y"):
    df = yf.download(symbol, period=period)         # 下载股票数据
    df = get_signal(df)                             # 计算信号
    buy_signal = df[df['Buy'] == True]              # 提取买入信号
    print(f"{symbol} 买入信号：")
    print(buy_signal[['Close', 'MA5', 'MA10']])     # 打印买入信号
    plot_signals(df, symbol)                        # 可视化图表
    df.to_csv(f"data/{symbol}.csv")                 # 保存数据

if __name__ == "__main__":
    # 获取脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)  # 切换到脚本所在目录，避免路径错误

    # 自动创建 data 文件夹，避免路径报错
    if not os.path.exists("data"):
        os.makedirs("data")

    # 运行两个股票示例
    main("AAPL", "1y")
    main("TSLA", "6mo")

    
