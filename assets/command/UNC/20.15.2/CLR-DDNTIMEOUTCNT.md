---
id: UNC@20.15.2@MMLCommand@CLR DDNTIMEOUTCNT
type: MMLCommand
name: CLR DDNTIMEOUTCNT（清除DDN超时延时删除功能运行信息记录）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: DDNTIMEOUTCNT
command_category: 动作类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN消息无响应处理策略
status: active
---

# CLR DDNTIMEOUTCNT（清除DDN超时延时删除功能运行信息记录）

## 功能

**适用NF：SGW-C**

该命令用于DDN消息无响应延时删除用户功能开启后，清除相关累计值信息，包括已经处理过的延时删除用户数、从延时删除状态被恢复的用户数、从延时删除状态被删除的用户数，不清除当前处于延时删除状态的用户数信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DDNTIMEOUTCNT]] · DDN超时延时删除功能运行信息记录（DDNTIMEOUTCNT）

## 使用实例

清除DDN消息无响应延时删除用户功能生效后的相关维护信息：

```
CLR DDNTIMEOUTCNT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-DDNTIMEOUTCNT.md`
