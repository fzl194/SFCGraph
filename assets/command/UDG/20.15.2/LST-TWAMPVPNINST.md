---
id: UDG@20.15.2@MMLCommand@LST TWAMPVPNINST
type: MMLCommand
name: LST TWAMPVPNINST（查询VPN实例名称）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPVPNINST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- VPN实例
status: active
---

# LST TWAMPVPNINST（查询VPN实例名称）

## 功能

该命令用于查询VPN实例名称。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>区分大小写，不支持空格。<br>“_public_”是公网缺省VPN的实例名，不允许用户配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPVPNINST]] · VPN实例名称（TWAMPVPNINST）

## 使用实例

查询VPN实例，命令如下：

```
%%LST TWAMPVPNINST: ;%%
RETCODE = 0  操作成功

结果如下
--------
VPN实例名称  =  ck
    VPN实例ID  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VPN实例名称（LST-TWAMPVPNINST）_27262288.md`
