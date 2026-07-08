---
id: UNC@20.15.2@MMLCommand@DSP ARPDYNBLACKLIST
type: MMLCommand
name: DSP ARPDYNBLACKLIST（查询ARP动态黑名单）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPDYNBLACKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP防欺骗配置
status: active
---

# DSP ARPDYNBLACKLIST（查询ARP动态黑名单）

## 功能

该命令用于查询ARP动态黑名单。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPDYNBLACKLIST]] · ARP动态黑名单（ARPDYNBLACKLIST）

## 使用实例

不指定参数时，查询VNFC上所有ARP动态黑名单：

```
DSP ARPDYNBLACKLIST:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
         IP地址  =  10.1.1.2
        MAC地址  =  00E0-FC12-3456
       接口名称  =  Eth64/0/6
老化时间（min）  =  19
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ARP动态黑名单（DSP-ARPDYNBLACKLIST）_50280942.md`
