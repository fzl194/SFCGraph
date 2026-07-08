---
id: UNC@20.15.2@MMLCommand@DSP DDNTIMEOUTCNT
type: MMLCommand
name: DSP DDNTIMEOUTCNT（显示DDN超时延时删除功能运行信息记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DDNTIMEOUTCNT
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
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

# DSP DDNTIMEOUTCNT（显示DDN超时延时删除功能运行信息记录）

## 功能

**适用NF：SGW-C**

该命令用于查询DDN消息无响应延时删除用户功能生效后的相关维护信息，显示当前处于延时删除状态的用户数量、已经处理过的延时删除用户数量、从延时删除状态被恢复的用户数量、从延时删除状态被删除的用户数量信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DDN超时延时删除功能运行信息记录（DDNTIMEOUTCNT）](configobject/UNC/20.15.2/DDNTIMEOUTCNT.md)

## 使用实例

查询DDN消息无响应延时删除用户功能生效后的相关维护信息：

```
DSP DDNTIMEOUTCNT:;
RETCODE = 0 操作成功.

结果如下
------------------
结果 = 
当前处于延时删除状态的用户数量 = 0
从延时删除状态被恢复的用户数量 = 0
从延时删除状态被删除的用户数量 = 0
已经处理过的延时删除用户数量 = 0
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示DDN超时延时删除功能运行信息记录（DSP-DDNTIMEOUTCNT）_46314491.md`
