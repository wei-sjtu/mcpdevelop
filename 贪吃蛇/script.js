// 获取画布元素和绘图上下文
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 画布尺寸
const canvasSize = 400;
canvas.width = canvasSize;
canvas.height = canvasSize;

// 方块大小
const blockSize = 20;

// 蛇的初始位置和方向
let snake = [
    { x: 10 * blockSize, y: 10 * blockSize }
];
let direction = 'right';

// 食物的位置
let food = {
    x: Math.floor(Math.random() * (canvasSize / blockSize)) * blockSize,
    y: Math.floor(Math.random() * (canvasSize / blockSize)) * blockSize
};

// 游戏循环间隔
let gameInterval;

// 开始游戏
function startGame() {
    gameInterval = setInterval(update, 100);
}

// 更新游戏状态
function update() {
    // 清空画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 绘制蛇
    drawSnake();

    // 绘制食物
    drawFood();

    // 移动蛇
    moveSnake();

    // 检查碰撞
    checkCollision();
}

// 绘制蛇
function drawSnake() {
    snake.forEach(segment => {
        ctx.fillStyle = 'green';
        ctx.fillRect(segment.x, segment.y, blockSize, blockSize);
    });
}

// 绘制食物
function drawFood() {
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, blockSize, blockSize);
}

// 移动蛇
function moveSnake() {
    let head = {
        x: snake[0].x,
        y: snake[0].y
    };

    switch (direction) {
        case 'up':
            head.y -= blockSize;
            break;
        case 'down':
            head.y += blockSize;
            break;
        case 'left':
            head.x -= blockSize;
            break;
        case 'right':
            head.x += blockSize;
            break;
    }

    snake.unshift(head);

    // 检查是否吃到食物
    if (head.x === food.x && head.y === food.y) {
        // 生成新的食物
        food = {
            x: Math.floor(Math.random() * (canvasSize / blockSize)) * blockSize,
            y: Math.floor(Math.random() * (canvasSize / blockSize)) * blockSize
        };
    } else {
        // 移除蛇的尾部
        snake.pop();
    }
}

// 检查碰撞
function checkCollision() {
    let head = snake[0];

    // 检查是否撞到边界
    if (head.x < 0 || head.x >= canvasSize || head.y < 0 || head.y >= canvasSize) {
        gameOver();
    }

    // 检查是否撞到自己
    for (let i = 1; i < snake.length; i++) {
        if (head.x === snake[i].x && head.y === snake[i].y) {
            gameOver();
        }
    }
}

// 游戏结束
function gameOver() {
    clearInterval(gameInterval);
    alert('游戏结束！');
}

// 监听键盘事件
document.addEventListener('keydown', function(event) {
    switch (event.key) {
        case 'ArrowUp':
            if (direction !== 'down') direction = 'up';
            break;
        case 'ArrowDown':
            if (direction !== 'up') direction = 'down';
            break;
        case 'ArrowLeft':
            if (direction !== 'right') direction = 'left';
            break;
        case 'ArrowRight':
            if (direction !== 'left') direction = 'right';
            break;
    }
});

// 开始游戏
startGame();