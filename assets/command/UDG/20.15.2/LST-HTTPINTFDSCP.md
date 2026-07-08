---
id: UDG@20.15.2@MMLCommand@LST HTTPINTFDSCP
type: MMLCommand
name: LST HTTPINTFDSCP（查询HTTP服务存储的接口DSCP信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPINTFDSCP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST HTTPINTFDSCP（查询HTTP服务存储的接口DSCP信息）

## 功能

该命令用来查看逻辑接口对外发送IP包时携带的DSCP值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPINTFDSCP]] · HTTP服务存储的接口DSCP信息（HTTPINTFDSCP）

## 使用实例

若查看逻辑接口对外发送IP包时携带的DSCP值，则可以使用如下命令：

```
%%LST HTTPINTFDSCP:;%%
RETCODE = 0  操作成功

结果如下
--------
NF类型      DSCP值  

NFTypeNRF   46      
NFTypeAMF   46      
NFTypeSMF   46      
NFTypeSMSF  46      
NFTypeNSSF  46      
NFTypeCHF   46      
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HTTPINTFDSCP.md`
