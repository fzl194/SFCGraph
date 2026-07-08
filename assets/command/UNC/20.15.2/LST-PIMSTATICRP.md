---
id: UNC@20.15.2@MMLCommand@LST PIMSTATICRP
type: MMLCommand
name: LST PIMSTATICRP（查询PIM静态RP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PIMSTATICRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM静态RP
status: active
---

# LST PIMSTATICRP（查询PIM静态RP配置）

## 功能

该命令用于查询静态RP配置。

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

- [[UNC@20.15.2@ConfigObject@PIMSTATICRP]] · PIM静态RP配置（PIMSTATICRP）

## 使用实例

查询PIM静态RP配置：

```
LST PIMSTATICRP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
        VPN实例名称  =  _public_
             地址族  =  IPv4单播
       静态RP的地址  =  192.168.0.3
         静态RP策略  =  2000
     静态RP的优先级  =  1
  静态RP使能双向PIM  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PIMSTATICRP.md`
