---
id: UDG@20.15.2@MMLCommand@LST HTTPSTATUS
type: MMLCommand
name: LST HTTPSTATUS（查询HTTP状态码判定配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP状态码管理
status: active
---

# LST HTTPSTATUS（查询HTTP状态码判定配置）

## 功能

该命令用于查询已有的HTTP状态码判定配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：无 |
| STATUS | 状态码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行判定的状态码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~699。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPSTATUS]] · HTTP状态码判定配置（HTTPSTATUS）

## 使用实例

查询已有的HTTP状态码判定配置，可以用如下命令：

```
%%LST HTTPSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
               索引  =  1
               场景  =  ERRNEXTHOP
           配置类型  =  WHITELIST
             状态码  =  604
               描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP状态码判定配置（LST-HTTPSTATUS）_67609928.md`
