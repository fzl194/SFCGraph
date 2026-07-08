---
id: UDG@20.15.2@ConfigObject@DBGCMDPRXY
type: ConfigObject
name: DBGCMDPRXY（通过命令代理执行调试命令）
nf: UDG
version: 20.15.2
object_name: DBGCMDPRXY
object_kind: action
status: active
---

# DBGCMDPRXY（通过命令代理执行调试命令）

## 说明

该命令用于在APP VNFC上执行调试命令。完整的调试命令在“CMDMSG（调试命令字符串）”参数中下发，调试命令的详细帮助可通过如下步骤获取：

1、执行本命令，在“CMDMSG（调试命令字符串）”中输入“$”获取可执行的所有调试命令。

2、执行本命令，在“CMDMSG（调试命令字符串）”中输入要执行的调试命令、空格和“$”，显示调试命令的第一关键字。

3、执行本命令，在“CMDMSG（调试命令字符串）”中输入要执行的调试命令、第一关键字、空格和“$”，显示调试命令的第二关键字。

4、依次类推，直到显示调试命令的所有关键字。

## 操作本对象的命令

- [OPR DBGCMDPRXY](command/UDG/20.15.2/OPR-DBGCMDPRXY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/通过命令代理执行调试命令（OPR-DBGCMDPRXY）_29626981.md`
