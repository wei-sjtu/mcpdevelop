// 导入必要的模块，这里使用Node.js的net模块来创建TCP服务器
const net = require('net');

// 定义服务器的端口号
const PORT = 3000;

// 创建一个TCP服务器实例
const server = net.createServer((socket) => {
    // 当有新的客户端连接时触发此事件
    console.log('有新的客户端连接');

    // 监听客户端发送的数据
    socket.on('data', (data) => {
        // 将接收到的数据转换为字符串
        const message = data.toString();
        console.log(`收到客户端消息: ${message}`);

        // 向客户端发送响应
        socket.write('服务器已收到消息');
    });

    // 监听客户端断开连接事件
    socket.on('end', () => {
        console.log('客户端已断开连接');
    });
});

// 启动服务器并监听指定端口
server.listen(PORT, () => {
    console.log(`服务器已启动，监听端口 ${PORT}`);
});