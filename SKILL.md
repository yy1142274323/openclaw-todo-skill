---
name: todo-manager
description: "管理待办事项和任务清单。支持添加、完成、删除、列表查看任务。适用于个人任务管理和项目进度跟踪。"
---

# Todo Manager

管理待办事项的Skill，支持增删改查。

## Commands

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

## 数据存储

任务保存在 `todos.json` 文件中，格式如下：
```json
[
  {"id": 1, "text": "完成任务A", "done": false, "created": "2026-03-22"}
]
```

## 使用示例

```
用户: 帮我添加一个任务"写报告"
-> 添加任务成功，ID: 1

用户: 显示我的待办
-> 1. [ ] 写报告
-> 2. [ ] 提交代码

用户: 完成第一个任务
-> 任务1已完成 ✓
```
