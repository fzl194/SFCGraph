---
id: UNC@20.15.2@MMLCommand@LST PSEUDONYPOLICY
type: MMLCommand
name: LST PSEUDONYPOLICY（查询CHR假名化本地策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PSEUDONYPOLICY
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SGSN
- MME
- SGW-C
- PGW-C
- NCG
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 软件参数管理
- 假名化策略
status: active
---

# LST PSEUDONYPOLICY（查询CHR假名化本地策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SGSN、MME、SGW-C、PGW-C、NCG、SMSF**

该命令用于查询CHR假名化本地策略的属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSEUDONYPOLICY]] · CHR假名化本地策略（PSEUDONYPOLICY）

## 使用实例

如果想查询CHR假名化本地策略的属性配置，可以用如下命令：

```
%%LST PSEUDONYPOLICY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
CHR pseudony local policy switch  =  ON
   CHR pseudony local policy key  =  *****
(Number of results = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PSEUDONYPOLICY.md`
