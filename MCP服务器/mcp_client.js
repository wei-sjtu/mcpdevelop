// 导入必要的模块，这里使用Node.js的net模块来创建TCP客户端
const net = require('net');

// 定义服务器的地址和端口号
const SERVER_HOST = '127.0.0.1';
const SERVER_PORT = 3000;

// 创建一个TCP客户端实例
const client = net.createConnection({ host: SERVER_HOST, port: SERVER_PORT }, () => {
    // 连接成功后向服务器发送消息
    console.log('已连接到服务器');
    client.write('这是客户端发送的消息');
});

// 监听服务器返回的数据
client.on('data', (data) => {
    // 将接收到的数据转换为字符串
    const message = data.toString();
    console.log(`收到服务器响应: ${message}`);

    // 关闭客户端连接
    client.end();
});

// 监听客户端断开连接事件
client.on('end', () => {
    console.log('与服务器的连接已断开');
});

// 监听连接错误事件
client.on('error', (err) => {
    console.error(`连接出错: ${err.message}`);
});