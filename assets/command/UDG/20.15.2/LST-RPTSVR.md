---
id: UDG@20.15.2@MMLCommand@LST RPTSVR
type: MMLCommand
name: LST RPTSVR（显示报表服务器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTSVR
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器
status: active
---

# LST RPTSVR（显示报表服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询配置的所有报表服务器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [报表服务器（RPTSVR）](configobject/UDG/20.15.2/RPTSVR.md)

## 使用实例

显示所有配置的报表服务器：

```
LST RPTSVR:;
```

```

RETCODE = 0 操作成功

报表服务器信息
--------------
报表服务器名称   报表消息类型   心跳检测成功次数阈值   心跳检测的失败次数门限   心跳消息发送时间间隔   服务器功能
dbcs1            UFDR           6                     6                       10                        RPT&SSU                
dbcs2            UFDR           6                     6                       10                        RPT&SSU                

(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示报表服务器（LST-RPTSVR）_27634000.md`
