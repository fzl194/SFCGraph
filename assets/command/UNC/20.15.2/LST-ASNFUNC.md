---
id: UNC@20.15.2@MMLCommand@LST ASNFUNC
type: MMLCommand
name: LST ASNFUNC（查询ASN功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ASNFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- ASN功能管理
status: active
---

# LST ASNFUNC（查询ASN功能）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于查询ASN功能开关状态及ASN的同步周期。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ASNFUNC]] · ASN功能（ASNFUNC）

## 使用实例

显示ASN功能开关的配置及同步周期：

```
LST ASNFUNC:;
RETCODE = 0  操作成功。

ASN漫游功能信息
---------------
        ASN 功能开关  =  使能
ASN 同步时长(小时)  =  5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ASNFUNC.md`
