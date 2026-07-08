---
id: UDG@20.15.2@MMLCommand@DSP LBSRVINST
type: MMLCommand
name: DSP LBSRVINST（查询LB服务实例）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBSRVINST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务实例管理
- 服务实例
status: active
---

# DSP LBSRVINST（查询LB服务实例）

## 功能

该命令用于查询业务VNFC申请的LB服务实例信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINDEX | 服务实例索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC实例索引。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294<br>说明：首次执行本命令时，无需输入本参数，显示所有<br>“服务VNFC ID（CONSUMERVNFCID）”<br>对应的记录 。后续查询过程中，根据首次查询结果输入本参数，可以查询单条记录。 |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBSRVINST]] · LB服务实例（LBSRVINST）

## 使用实例

查询服务VNFC ID为4的LB服务实例信息:

DSP LBSRVINST: CONSUMERVNFCID=4;

```
%%DSP LBSRVINST: CONSUMERVNFCID=4;%%
RETCODE = 0  操作成功

结果如下:
-------------------------
         服务VNFC ID  =  4
        服务实例索引  =  0
        服务实例名称  =  Sig
          服务实例ID  =  0
        网络接入类型  =  带VNRS接入
负载均衡业务感知类型  =  L4业务感知
    负载均衡应用模式  =  通用模式
    负载均衡转发模式  =  通用模式
        首识别策略ID  =  4096
    首负载均衡策略ID  =  8192
              静默期  =  4294967295
            老化时间  =  4294967295
          服务组索引  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LB服务实例（DSP-LBSRVINST）_29627060.md`
