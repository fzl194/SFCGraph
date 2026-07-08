---
id: UDG@20.15.2@MMLCommand@DSP NEXTHOP
type: MMLCommand
name: DSP NEXTHOP（查询负载均衡下一跳）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NEXTHOP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 策略调测
- 下一跳策略
status: active
---

# DSP NEXTHOP（查询负载均衡下一跳）

## 功能

查询负载均衡的下一跳信息。

## 注意事项

该命令仅限于开发和测试使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NXTHPTYPE | 下一跳类型 | 可选必选说明：必选参数<br>参数含义：下一跳的类型。<br>默认值：无<br>取值范围：<br>- “SRV_PLY_TYPE_NORMAL(标准类型) ”<br>- “SRV_PLY_TYPE_EXTEND(扩展类型) ” |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>默认值：无<br>取值范围：0~4294967294 |
| GROUPID | 下一跳组ID | 可选必选说明：必选参数<br>参数含义：下一跳的组ID，该参数可以使用CLI命令查询vPlyIDMap表获取。<br>默认值：无<br>取值范围：0~4294967294 |
| NEXTHOPINDEX | 下一跳索引 | 可选必选说明：可选参数<br>参数含义：下一跳的索引。<br>默认值：无<br>取值范围：0~4294967294 |

## 操作的配置对象

- [负载均衡下一跳（NEXTHOP）](configobject/UDG/20.15.2/NEXTHOP.md)

## 使用实例

1. 查询负载均衡下一跳信息的命令如下：DSP NEXTHOP: NXTHPTYPE=SRV_PLY_TYPE_EXTEND, CONSUMERVNFCID=4, GROUPID=9, NEXTHOPINDEX=16606;
  ```
  %%DSP NEXTHOP: NXTHPTYPE=SRV_PLY_TYPE_EXTEND, CONSUMERVNFCID=4, GROUPID=9, NEXTHOPINDEX=16606;%%
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
   下一跳类型  =  扩展类型
  服务VNFC ID  =  4
   下一跳组ID  =  9
   下一跳索引  =  16606
          QoS  =  1
       Low TB  =  2
      High TB  =  0
           TP  =  2419994929
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询负载均衡下一跳（DSP-NEXTHOP）_29627117.md`
