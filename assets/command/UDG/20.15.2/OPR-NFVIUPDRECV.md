---
id: UDG@20.15.2@MMLCommand@OPR NFVIUPDRECV
type: MMLCommand
name: OPR NFVIUPDRECV（NFVI分批升级恢复）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: NFVIUPDRECV
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- NFVI分批升级管理
status: active
---

# OPR NFVIUPDRECV（NFVI分批升级恢复）

## 功能

该命令用于NFVI分批升级过程失败恢复。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPER_MODE | 操作模式 | 可选必选说明：可选参数<br>参数含义：操作模式类型。<br>数据来源：本端规划<br>取值范围：<br>- Recovery（升级正常结束恢复）<br>- ForceRecovery（系统异常强制恢复）<br>默认值：Recovery<br>配置原则：无 |
| POD_NAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NFVIUPDRECV]] · NFVI分批升级恢复（NFVIUPDRECV）

## 使用实例

- NFVI分批升级恢复。
  ```
  %%OPR NFVIUPDRECV: OPER_MODE=Recovery;%%
  ```
- NFVI分批升级强制恢复。
  ```
  %%OPR NFVIUPDRECV: OPER_MODE=ForceRecovery;%%
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/OPR-NFVIUPDRECV.md`
