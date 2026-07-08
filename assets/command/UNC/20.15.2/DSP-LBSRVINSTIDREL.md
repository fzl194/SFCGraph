---
id: UNC@20.15.2@MMLCommand@DSP LBSRVINSTIDREL
type: MMLCommand
name: DSP LBSRVINSTIDREL（查询服务ID与服务实例的关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LBSRVINSTIDREL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB服务ID与CSLB服务实例ID的关系
status: active
---

# DSP LBSRVINSTIDREL（查询服务ID与服务实例的关系）

## 功能

该命令用于查询业务VNFC对应的CSLB服务实例，通过查询结果判断业务是否已经下发负载均衡服务的绑定策略，辅助定位隧道转发失败问题。

## 注意事项

该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODE ID（节点ID）即为业务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| APPINSTID | 业务服务实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于业务VNFC定义的服务实例ID，通过<br>**[DSP LBSRVINST](../../服务实例管理/服务实例/查询LB服务实例（DSP LBSRVINST）_29627060.md)**<br>获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LBSRVINSTIDREL]] · 服务ID与服务实例的关系（LBSRVINSTIDREL）

## 使用实例

查询指定业务VNFC的所有业务类型对应的服务实例ID。

DSP LBSRVINSTIDREL: SRVVNFCID=4;

```
%%DSP LBSRVINSTIDREL: SRVVNFCID=4;%%
RETCODE = 0  操作成功。

操作结果如下：
-------------------------
业务VNFCID 业务服务实例ID  CSLB_VNFC服务实例ID  服务ID     服务类型   
4          0               0                    0          0
4          1               1                    1          0
(结果个数 = 2)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LBSRVINSTIDREL.md`
