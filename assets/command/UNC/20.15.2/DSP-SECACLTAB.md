---
id: UNC@20.15.2@MMLCommand@DSP SECACLTAB
type: MMLCommand
name: DSP SECACLTAB（显示安全ACL表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SECACLTAB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ACL
status: active
---

# DSP SECACLTAB（显示安全ACL表项）

## 功能

该命令用来显示安全ACL表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECACLTAB]] · 安全ACL表项（SECACLTAB）

## 使用实例

显示指定资源单元的安全ACL表项：

```
DSP SECACLTAB:RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```
RETCODE = 0  操作成功.                                                                                                     
结果如下 
------------------------ 
RU名称                      源IP地址是否有效    目的IP地址是否有效    源IP地址      目的IP地址    源IP地址掩码       目的IP地址掩码     源端口号    目的端口号    源端口类型    目的端口类型    协议类型    优先级    源端口起始值    源端口终止值    目的端口起始值    目的端口终止值    安全类型    策略类型        策略ID    规则ID    下发标记

VNODE_VNRS_VNFC_IPU_0066    IP配置无效          IP配置有效            0.0.0.0        192.168.0.2    0.0.0.0            255.255.255.255    0           22            不可用        等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         FALSE   
VNODE_VNRS_VNFC_IPU_0066    IP配置无效          IP配置有效            0.0.0.0        192.168.0.2    0.0.0.0            255.255.255.255    0           830           不可用        等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         FALSE   
VNODE_VNRS_VNFC_IPU_0066    IP配置无效          IP配置有效            0.0.0.0        192.168.0.2    0.0.0.0            255.255.255.255    0           6000          不可用        等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         FALSE   
VNODE_VNRS_VNFC_IPU_0066    IP配置有效          IP配置有效            192.168.0.1    192.168.0.2    255.255.255.255    255.255.255.255    51652       6000          等于          等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         TRUE    
VNODE_VNRS_VNFC_IPU_0066    IP配置有效          IP配置有效            192.168.0.1    192.168.0.2    255.255.255.255    255.255.255.255    60242       22            等于          等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         TRUE    
VNODE_VNRS_VNFC_IPU_0066    IP配置有效          IP配置有效            192.168.0.1    192.168.0.2    255.255.255.255    255.255.255.255    62610       830           等于          等于            6           0         0               0               0                 0                 允许        动态链路策略    0         0         TRUE    
(结果个数 = 6)                                                                                                                                          
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SECACLTAB.md`
