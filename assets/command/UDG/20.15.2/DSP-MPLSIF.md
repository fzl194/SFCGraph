---
id: UDG@20.15.2@MMLCommand@DSP MPLSIF
type: MMLCommand
name: DSP MPLSIF（显示MPLS接口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MPLSIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS接口
status: active
---

# DSP MPLSIF（显示MPLS接口信息）

## 功能

该命令用于显示MPLS接口信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [MPLS接口（MPLSIF）](configobject/UDG/20.15.2/MPLSIF.md)

## 使用实例

显示MPLS接口信息：

```
DSP MPLSIF:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
            接口名  =  Ethernet67/0/6
接口配置的MPLS MTU  =  1500
         接口MTU值  =  1500
       生效的MTU值  =  1500
      接口协议状态  =  接口Up
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示MPLS接口信息（DSP-MPLSIF）_00440669.md`
