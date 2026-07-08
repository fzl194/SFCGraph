---
id: UNC@20.15.2@MMLCommand@DSP SDRVPN
type: MMLCommand
name: DSP SDRVPN（查询SDRC中的VPN信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRVPN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRVPN（查询SDRC中的VPN信息）

## 功能

该命令用于查询SDRC中的VPN信息，若命令不接任何参数，则该命令列出SDRC中所有VPN的信息，否则显示特定的VPN信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示vpn的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDRVPN]] · SDRC中的VPN信息（SDRVPN）

## 使用实例

显示SDRC中VPNNAME等于_public_的VPN信息

```
%%DSP SDRVPN:;%%
RETCODE = 0  操作成功

结果如下
--------
VPN 名称  =  _public_
 SDR ID  =  1
 下行经过LB  =  是
VPN拓扑  =  instance_id:281492156580961 low_tb:1121 tp:2416123937  instance_id:281492156580949 low_tb:1109 tp:2416123937
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SDRC中的VPN信息（DSP-SDRVPN）_94730437.md`
