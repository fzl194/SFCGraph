---
id: UDG@20.15.2@MMLCommand@LST MGMDIF
type: MMLCommand
name: LST MGMDIF（查询IGMP接口配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MGMDIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- IGMP接口配置
status: active
---

# LST MGMDIF（查询IGMP接口配置）

## 功能

该命令用来查询IGMP接口配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MGMDIF]] · IGMP接口配置（MGMDIF）

## 使用实例

查询IGMP接口配置：

```
LST MGMDIF:IFNAME="Ethernet64/0/3",VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
                     VPN实例名称  =  _public_
                          地址族  =  IPv4单播
                        接口名称  =  Ethernet64/0/3
                    接口IGMP使能  =  FALSE
   配置的周期性普遍查询时间（s）  =  60
     普遍查询的最大响应时间（s）  =  10
              配置的鲁棒稳定系数  =  4
                配置的IGMP版本号  =  2
     特定组查询的周期性时间（s）  =  1
            是否需要Router-Alert  =  FALSE
            是否发送Router-Alert  =  TRUE
       其他查询器存在的时间（s）  =  0
              是否配置立刻离开组  =  FALSE
动态加入的IGMP组记录是否永不超时  =  FALSE
             接口使能SSM映射功能  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MGMDIF.md`
