---
id: UDG@20.15.2@MMLCommand@DSP PAERULELOOP3T
type: MMLCommand
name: DSP PAERULELOOP3T（显示PAE上Loop口三元组规则信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAERULELOOP3T
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

# DSP PAERULELOOP3T（显示PAE上Loop口三元组规则信息）

## 功能

该命令用于显示PAE Loop口三元组分发规则。

PAE接收到报文，根据配置的规则，找到对应的虚拟通信端口后将报文从对应的端口发送出去。通过该命令可查看PAE模块端口的分发规则，通过获取的信息，可了解配置是否正常，并进行故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAERULELOOP3T]] · PAE上Loop口三元组规则信息（PAERULELOOP3T）

## 使用实例

显示微服务类型为“aa”微服务实例为“aa” Loop口三元组规则信息：

```
DSP PAERULELOOP3T:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
--------
源IP地址              源端口    协议号    负载均衡默认哈希值    负载均衡哈希值类型    QoS负载均衡类型       TB高16位地址    TB低32位地址    TP        应用头类型    变长报文长度

192.168.0.1           13330     6         0x0                   PAE_HASH_VPN_IP3T     PAE_QOSBATYPE_DSCP    0x0             0x40            0x1111    63488         2           
192.168.0.2           8738      17        0x0                   PAE_HASH_VPN_IP3T     PAE_QOSBATYPE_DSCP    0x0             0x40            0x1111    63488         2           
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PAERULELOOP3T.md`
