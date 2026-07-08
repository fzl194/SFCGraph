---
id: UDG@20.15.2@MMLCommand@LST INNERTLSMODE
type: MMLCommand
name: LST INNERTLSMODE（查询TLS模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INNERTLSMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- TLS模式管理
status: active
---

# LST INNERTLSMODE（查询TLS模式）

## 功能

此命令用于查询服务的TLS模式。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务类型。<br>数据来源：本端规划<br>取值范围：<br>- HAFETCD（HAFETCD）<br>- CMF（CMF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TLS模式（INNERTLSMODE）](configobject/UDG/20.15.2/INNERTLSMODE.md)

## 使用实例

查询服务的TLS模式：

```
%%LST INNERTLSMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
服务类型  =  HAFETCD
 TLS模式  =  HTTP协议
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TLS模式（LST-INNERTLSMODE）_63673348.md`
