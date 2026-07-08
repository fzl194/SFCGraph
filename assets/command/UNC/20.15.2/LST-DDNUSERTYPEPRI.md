---
id: UNC@20.15.2@MMLCommand@LST DDNUSERTYPEPRI
type: MMLCommand
name: LST DDNUSERTYPEPRI（查询基于用户属性的DDN消息优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNUSERTYPEPRI
command_category: 查询类
applicable_nf:
- SGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 基于用户属性的DDN优先级管理
status: active
---

# LST DDNUSERTYPEPRI（查询基于用户属性的DDN消息优先级）

## 功能

**适用NF：SGW-C、SMF**

该命令用于查询本地用户、漫游用户、拜访用户的DDN消息的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DDNUSERTYPEPRI]] · 基于用户属性的DDN消息优先级（DDNUSERTYPEPRI）

## 使用实例

查询本地用户、漫游用户、拜访用户的DDN消息的优先级：

```
%%LST DDNUSERTYPEPRI:;%%
RETCODE = 0  操作成功

基于用户属性的DDN消息优先级
---------------------------
       本地用户优先级  =  高
       漫游用户优先级  =  低
       拜访用户优先级  =  最低
DDN用户类型优先级开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DDNUSERTYPEPRI.md`
