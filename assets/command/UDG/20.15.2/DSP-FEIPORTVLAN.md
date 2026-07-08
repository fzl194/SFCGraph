---
id: UDG@20.15.2@MMLCommand@DSP FEIPORTVLAN
type: MMLCommand
name: DSP FEIPORTVLAN（显示FEI端口VLAN）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FEIPORTVLAN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FEI端口VLAN
status: active
---

# DSP FEIPORTVLAN（显示FEI端口VLAN）

## 功能

该命令用来查询FEI指定端口的VLAN表项信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAINIFNAME | 主接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定主接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |

## 操作的配置对象

- [FEI端口VLAN（FEIPORTVLAN）](configobject/UDG/20.15.2/FEIPORTVLAN.md)

## 使用实例

查询FEI指定端口VLAN表项信息：

```
DSP FEIPORTVLAN:MAINIFNAME="Ethernet66/0/3";
```

```

RETCODE = 0  操作成功。

结果如下
--------
子接口名称          VLAN ID值    转发状态

Ethernet66/0/3.1    1            有效    
Ethernet66/0/3.2    2            有效    
Ethernet66/0/3.3    3            有效    
Ethernet66/0/3.4    4            有效    
Ethernet66/0/3.5    5            有效    
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示FEI端口VLAN（DSP-FEIPORTVLAN）_49802286.md`
