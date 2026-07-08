---
id: UNC@20.15.2@MMLCommand@DSP PAEPORTINFO
type: MMLCommand
name: DSP PAEPORTINFO（显示PAE端口基本信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPORTINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEPORTINFO（显示PAE端口基本信息）

## 功能

该命令用于显示指定微服务的PAE端口信息。流量不通或者端口状态异常场景下，需要确认当前微服务的PAE端口信息以及相关配置是否正常时，可以使用该命令。

## 注意事项

该命令执行后立即生效。内联口不支持ARP和PING等主机报文应答。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEPORTINFO]] · PAE端口基本信息（PAEPORTINFO）

## 使用实例

如果用户希望显示所有微服务的PAE端口信息，可以执行如下操作：

```
DSP PAEPORTINFO:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
微服务类型  微服务实例号   端口类型    端口名称      端口ID    IP地址                                  掩码或前缀长度    MAC地址           MTU（byte）  MTU配置类型    端口状态    命名空间   绑定模式   队列数
					
aa          aa             内联口      eth1          1         0.0.0.0                                 0                 00E0-FC66-0967    1800         用户配置       up          NULL        是        1
aa          aa             内联口      eth2          2         0.0.0.0                                 0                 00E0-FC66-0968    1800         用户配置       up          NULL        是        1
aa          aa             Loop口      pae_tun0      2         192.168.0.1                             24                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun0      2         fc00:db8::100                           32                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun0:1    2         192.168.0.2                             24                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun0:2    2         192.168.0.3                             24                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun0:3    2         192.168.0.4                             24                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun0:4    2         192.168.0.5                             24                NULL              1500         无效配置       up          NULL        否        1
aa          aa             Loop口      pae_tun1      3         192.168.0.6                             24                NULL              1500         无效配置       up          NULL        否        1
bb          bb             内联口      eth1          1         0.0.0.0                                 0                 00E0-FC66-1067    1800         用户配置       up          NULL        是        1
bb          bb             内联口      eth2          2         0.0.0.0                                 0                 00E0-FC66-1068    1800         用户配置       up          NULL        是        1
bb          bb             Loop口      pae_tun1      3         192.168.0.7                             24                NULL              1500         无效配置       up          NULL        否        1
(结果个数 = 12)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEPORTINFO.md`
