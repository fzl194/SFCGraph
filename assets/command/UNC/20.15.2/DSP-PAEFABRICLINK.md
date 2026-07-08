---
id: UNC@20.15.2@MMLCommand@DSP PAEFABRICLINK
type: MMLCommand
name: DSP PAEFABRICLINK（显示PAE链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEFABRICLINK
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- Fabric
status: active
---

# DSP PAEFABRICLINK（显示PAE链路信息）

## 功能

该命令用于显示指定资源上转发链路信息。

## 注意事项

- 该命令执行后立即生效。
- 在sriov bonding模式下链路级探测不再可信，链路探测状态显示为init，此状态无效不代表探测结果。可执行MML命令**[DSP PAEPORTINFO](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)**查询绑定模式是否为是。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [PAE链路信息（PAEFABRICLINK）](configobject/UNC/20.15.2/PAEFABRICLINK.md)

## 使用实例

显示微服务类型“aa”微服务类型实例 "aa"上转发链路信息：

```
DSP PAEFABRICLINK:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
--------             
微服务类型  微服务实例号 平面ID  本端节点TB   远端节点TB    本端端口名称  远端端口名称 链路优先级  链路是否连通过    链路状态    最近链路连通时间       最近链路中断时间
		
aa          aa           0       aa           bb            eth1          eth1         11          是                up          2017-09-14 01:20:26    2017-09-14 03:21:00
aa          aa           1       aa           bb            eth2          eth2         16          是                up          2017-09-14 01:20:26    2017-09-14 03:21:00 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE链路信息（DSP-PAEFABRICLINK）_92520014.md`
