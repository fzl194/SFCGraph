---
id: UNC@20.15.2@MMLCommand@LST NFDISCSRVLBSW
type: MMLCommand
name: LST NFDISCSRVLBSW（查询服务发现Service负载均衡功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFDISCSRVLBSW
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF发现NFS负载均衡管理
status: active
---

# LST NFDISCSRVLBSW（查询服务发现Service负载均衡功能）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询服务发现时的NF Service负载均衡功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFDISCSRVLBSW]] · 服务发现Service负载均衡功能（NFDISCSRVLBSW）

## 使用实例

查询服务发现时的NF Service负载均衡功能。

```
%%LST NFDISCSRVLBSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
对端NF类型    =  NfUDM
负载均衡开关  =  ON
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFDISCSRVLBSW.md`
