# 🦞 OpenClaw Todo Skill

一个简单实用的待办事项管理技能，适合 OpenClaw AI 助手使用。

## 功能特性

- ✅ 添加待办事项
- ✅ 列出所有任务
- ✅ 标记任务完成
- ✅ 删除任务
- ✅ 清除已完成任务

## 安装方法

```bash
# 克隆仓库
git clone https://github.com/yy1142274323/openclaw-todo-skill.git

# 或使用 OpenClaw skill 安装
clawdhub install openclaw-todo-skill
```

## 使用方法

### 命令行使用

```bash
# 查看所有待办事项
python3 todo.py --list

# 添加新任务
python3 todo.py --add "完成任务A"

# 标记任务完成
python3 todo.py --done 1

# 删除任务
python3 todo.py --delete 1

# 清除所有已完成任务
python3 todo.py --clear
```

### OpenClaw 中使用

在 OpenClaw 中配置为 Skill 后，可以直接用自然语言管理待办：

```
用户: 帮我添加一个任务"写报告"
-> 添加任务成功，ID: 1

用户: 显示我的待办
-> 1. [ ] 写报告
-> 2. [ ] 提交代码

用户: 完成第一个任务
-> 任务1已完成 ✓
```

## 数据存储

任务保存在 `todos.json` 文件中，格式如下：

```json
[
  {
    "id": 1,
    "text": "完成任务A",
    "done": false,
    "created": "2026-03-22 22:59"
  }
]
```

## 示例

```
$ python3 todo.py --add "完成项目报告"
✓ 添加任务成功，ID: 1

$ python3 todo.py --list
📋 待办事项：

1. [ ] 完成项目报告
   创建于: 2026-03-22 22:59

$ python3 todo.py --done 1
✓ 任务1已完成
```

## 技术栈

- Python 3
- JSON 数据存储
- 无需数据库，纯文件存储

## 赞助支持

如果这个技能对你有帮助，欢迎赞助支持！

<img src="https://raw.githubusercontent.com/yy1142274323/jarvis-api-optimizer/main/alipay_qr_v2.png" width="200" alt="支付宝赞助二维码">

## 作者

- Author: Claw 🦞
- GitHub: @yy1142274323

## License

MIT License
