---
id: UDG@20.15.2@MMLCommand@DSP EXTERNALDB
type: MMLCommand
name: DSP EXTERNALDB（查询外置规则数据库）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: EXTERNALDB
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- 外部规则数据库
status: active
---

# DSP EXTERNALDB（查询外置规则数据库）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询系统中当前使用的外置规则数据库信息。

## 注意事项

可能存在实际加载的库与回显的库不一致，不能以DSP命令的结果判断库是否加载成功，需要查看是否存在ALM-81184 外部规则数据库加载失败的告警。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置外置规则库类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OTT：OTT规则数据库。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTERNALDB]] · 外置规则数据库（EXTERNALDB）

## 使用实例

查询外置规则数据库信息：

```
DSP EXTERNALDB:DBTYPE=OTT;
```

```

RETCODE = 0  操作成功.

外置规则数据库版本信息
------------------------------
外置规则数据库版本号 = 0020.01.0000.0000.005      
          引擎版本号 = 2
      上一次加载版本 = 0020.01.0000.0000.001
            加载状态 = Success

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-EXTERNALDB.md`
