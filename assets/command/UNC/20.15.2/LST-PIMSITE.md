---
id: UNC@20.15.2@MMLCommand@LST PIMSITE
type: MMLCommand
name: LST PIMSITE（查询PIM全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PIMSITE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM全局参数
status: active
---

# LST PIMSITE（查询PIM全局配置）

## 功能

该命令用于查询全局PIM相关参数。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMSITE]] · PIM全局配置（PIMSITE）

## 使用实例

查看PIM全局配置：

```
LST PIMSITE:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
                                       VPN实例名称  =  _public_
                                            地址族  =  IPv4单播
                                          DR优先级  =  1
                                         SSM策略号  =  2000
                               Assert保持时间（s）  =  180
                           JP加入剪枝维持时间（s）  =  210
                              PIM邻居维持时间（s）  =  105
                         （S，G）表项生存时间（s）  =  210
                            Hello报文发送间隔（s）  =  70
                               JP报文发送间隔（s）  =  60
                             接口的lan-delay（ms）  =  500
配置Hello消息中携带的否决Prune剪枝的时间间隔（ms）  =  2500
                                       使能双向PIM  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PIM全局配置（LST-PIMSITE）_00840765.md`
