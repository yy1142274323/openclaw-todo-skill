#!/usr/bin/env python3
"""
Todo Manager Skill for OpenClaw
管理待办事项的简单工具
"""

import json
import os
import sys
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    """加载待办事项"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_todos(todos):
    """保存待办事项"""
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(text):
    """添加新任务"""
    todos = load_todos()
    new_id = max([t['id'] for t in todos], default=0) + 1
    todo = {
        "id": new_id,
        "text": text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    todos.append(todo)
    save_todos(todos)
    return new_id

def list_todos():
    """列出所有任务"""
    todos = load_todos()
    if not todos:
        return "暂无待办事项"
    
    result = ["📋 待办事项：", ""]
    for t in todos:
        status = "✓" if t['done'] else " "
        result.append(f"{t['id']}. [{status}] {t['text']}")
        result.append(f"   创建于: {t['created']}")
        result.append("")
    return "\n".join(result)

def done_todo(todo_id):
    """标记任务完成"""
    todos = load_todos()
    for t in todos:
        if t['id'] == todo_id:
            t['done'] = True
            save_todos(todos)
            return f"✓ 任务{todo_id}已完成"
    return f"❌ 未找到任务{todo_id}"

def delete_todo(todo_id):
    """删除任务"""
    todos = load_todos()
    todos = [t for t in todos if t['id'] != todo_id]
    save_todos(todos)
    return f"✓ 任务{todo_id}已删除"

def clear_done():
    """清除已完成任务"""
    todos = load_todos()
    todos = [t for t in todos if not t['done']]
    save_todos(todos)
    return "✓ 已清除所有已完成任务"

def main():
    if len(sys.argv) < 2:
        print(list_todos())
        return
    
    action = sys.argv[1]
    
    if action == "--list":
        print(list_todos())
    elif action == "--add" and len(sys.argv) > 2:
        text = " ".join(sys.argv[2:])
        todo_id = add_todo(text)
        print(f"✓ 添加任务成功，ID: {todo_id}")
    elif action == "--done" and len(sys.argv) > 2:
        todo_id = int(sys.argv[2])
        print(done_todo(todo_id))
    elif action == "--delete" and len(sys.argv) > 2:
        todo_id = int(sys.argv[2])
        print(delete_todo(todo_id))
    elif action == "--clear":
        print(clear_done())
    else:
        print("用法: python3 todo.py [--list|--add <内容>|--done <ID>|--delete <ID>|--clear]")

if __name__ == "__main__":
    main()
