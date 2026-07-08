---
id: UDG@20.15.2@MMLCommand@LST RPTRATELT
type: MMLCommand
name: LST RPTRATELT（查询业务报表消息流控配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTRATELT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表速率控制
status: active
---

# LST RPTRATELT（查询业务报表消息流控配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询报表消息流控配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTRATELT]] · 业务报表消息流控配置（RPTRATELT）

## 使用实例

假如运营商需要查询报表消息流控配置：

```
%%LST RPTRATELT:;
```

```
%%
RETCODE = 0  操作成功

报表消息流控配置信息
--------------------
        用户信息重发请求消息流控门限  =  100
                用户信息定时重发间隔  =  0
触发UFDR Stats的用户更新消息流控门限  =  300
     SSG主动定时重发用户信息功能开关  =  不使能
     SSG主动定时重发用户信息时间间隔  =  36000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务报表消息流控配置（LST-RPTRATELT）_93531887.md`
