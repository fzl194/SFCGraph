---
id: UDG@20.15.2@MMLCommand@LST HOSTSTCIF
type: MMLCommand
name: LST HOSTSTCIF（查询接口协议报文统计配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HOSTSTCIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 统计功能配置
status: active
---

# LST HOSTSTCIF（查询接口协议报文统计配置）

## 功能

该命令用于查询接口协议报文统计配置。

只有在任意一个接口下使能了协议报文统计功能之后执行该命令才能查询到结果。

不指定IFNAME参数时，查询所有接口的配置信息；当指定IFNAME参数时，可以查询指定接口的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HOSTSTCIF]] · 接口协议报文统计配置（HOSTSTCIF）

## 使用实例

查询接口协议报文统计配置：

```
LST HOSTSTCIF:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
接口名称  =  GigabitEthernet0/0/1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HOSTSTCIF.md`
