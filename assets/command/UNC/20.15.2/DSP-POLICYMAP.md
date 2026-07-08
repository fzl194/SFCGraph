---
id: UNC@20.15.2@MMLCommand@DSP POLICYMAP
type: MMLCommand
name: DSP POLICYMAP（查询策略映射表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: POLICYMAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 策略映射
status: active
---

# DSP POLICYMAP（查询策略映射表）

## 功能

查询策略映射表，获取业务VNFC侧的策略ID。策略映射表中记录业务VNFC侧策略ID与CSLB侧策略ID的对应关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| PLYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “PLY_TYPE_LB：负载均衡策略”<br>- “PLY_TYPE_DP：流识别策略”<br>- “PLY_TYPE_NEXTHOP：下一跳策略”<br>- “PLY_TYPE_EXCHANGE：交换表策略”<br>- “PLY_TYPE_LB_EX：扩展负载均衡策略”<br>- “PLY_TYPE_NEXTHOP_EX：扩展下一跳策略”<br>默认值：无 |
| LBPOLICYID | LB策略ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定CSLB分配的策略标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [策略映射表（POLICYMAP）](configobject/UNC/20.15.2/POLICYMAP.md)

## 使用实例

查询策略映射表。

DSP POLICYMAP:;

```
%%DSP POLICYMAP: PLYTYPE=PLY_TYPE_NEXTHOP;%%
RETCODE = 0  操作成功 

结果如下:
-------------------------
业务VNFC ID    策略类型         APP策略ID     LB策略ID     

4             下一跳策略        1            1            
4             下一跳策略        0            0            
4             下一跳策略        2            2            
4             下一跳策略        4            4            
4             下一跳策略        3            3            
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询策略映射表（DSP-POLICYMAP）_29627055.md`
