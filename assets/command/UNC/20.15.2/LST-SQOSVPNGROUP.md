---
id: UNC@20.15.2@MMLCommand@LST SQOSVPNGROUP
type: MMLCommand
name: LST SQOSVPNGROUP（查询VPN组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SQOSVPNGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- VPN组
status: active
---

# LST SQOSVPNGROUP（查询VPN组）

## 功能

该命令用来查询VPN组的信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNGROUPNAME | VPN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SQOSVPNGROUP]] · VPN组（SQOSVPNGROUP）

## 使用实例

查询VPN组的配置信息：

```
LST SQOSVPNGROUP:VPNGROUPNAME="vg1";
```

```
RETCODE = 0  操作成功。                                              
                                                                                
结果如下                                                        
------------------------                                                        
VPN组名称 = vg1
  VPN名称 = vpn1 
VPN优先级 = 1                                                              
(结果个数 = 1)                                                         
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SQOSVPNGROUP.md`
