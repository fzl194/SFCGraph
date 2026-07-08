---
id: UNC@20.15.2@MMLCommand@DSP PIMRP
type: MMLCommand
name: DSP PIMRP（查询RP信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PIMRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- RP信息
status: active
---

# DSP PIMRP（查询RP信息）

## 功能

该命令用于显示RP信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMRP]] · RP信息（PIMRP）

## 使用实例

显示RP信息：

```
DSP PIMRP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
   VPN实例名称  =  _public_
        地址族  =  IPv4单播
    C-RP的地址  =  10.0.0.1
    RP是否本地  =  TRUE
        组地址  =  239.0.0.1
组地址掩码长度  =  4
    RP的优先级  =  0
  RP的生存时间  =  00:17:12
  RP的超时时间  =  00:02:15
       OMU类型  =  MASTER
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PIMRP.md`
