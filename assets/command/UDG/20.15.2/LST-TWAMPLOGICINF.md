---
id: UDG@20.15.2@MMLCommand@LST TWAMPLOGICINF
type: MMLCommand
name: LST TWAMPLOGICINF（查询本地逻辑接口）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPLOGICINF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- 本端逻辑接口配置
status: active
---

# LST TWAMPLOGICINF（查询本地逻辑接口）

## 功能

该命令用于查询本地逻辑接口。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置逻辑接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPLOGICINF]] · 本地逻辑接口（TWAMPLOGICINF）

## 使用实例

查询逻辑接口名称为：n3if1/1/0的实例：

```
%%LST TWAMPLOGICINF: NAME="n3if1/1/0";%%
RETCODE = 0  操作成功

结果如下
--------
    逻辑接口名称  =  n3if1/1/0
      地址族类型  =  IPV4
逻辑接口IPv4地址  =  10.0.0.0
    逻辑接口掩码  =  255.255.255.255
     VPN实例名称  =  ck
      SHAREDTYPE  =  TRUE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询本地逻辑接口（LST-TWAMPLOGICINF）_73142135.md`
