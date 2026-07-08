---
id: UNC@20.15.2@MMLCommand@DSP PAERULEEXTERN
type: MMLCommand
name: DSP PAERULEEXTERN（显示PAE上外联口规则信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAERULEEXTERN
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

# DSP PAERULEEXTERN（显示PAE上外联口规则信息）

## 功能

该命令用于显示PAE外联口的分发规则。

PAE接收到报文，根据配置的规则，找到对应的虚拟通信端口后将报文从对应的端口发送出去。

通过该命令可查看PAE模块端口的分发规则，通过获取的信息，可了解配置是否正常，并进行故障诊断。

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

- [[UNC@20.15.2@ConfigObject@PAERULEEXTERN]] · PAE上外联口规则信息（PAERULEEXTERN）

## 使用实例

显示微服务类型为“aa”微服务实例为“aa”的外联口的分发规则：

```
DSP PAERULEEXTERN:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
端口ID    默认队列ID    负载均衡哈希值类型     下一个表项    QoS负载均衡类型          默认队列组ID    TB低32位地址    TP        TB高16位地址    VPN实例索引    特殊类型报文TP
 
2         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff  
3         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
4         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
5         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
6         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
7         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
8         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
9         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
(结果个数 = 8)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAERULEEXTERN.md`
