---
id: UDG@20.15.2@MMLCommand@DSP SECACL6TAB
type: MMLCommand
name: DSP SECACL6TAB（显示安全ACL6表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SECACL6TAB
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

# DSP SECACL6TAB（显示安全ACL6表项）

## 功能

该命令用来显示安全ACL6表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SECACL6TAB]] · 安全ACL6表项（SECACL6TAB）

## 使用实例

显示指定资源单元的安全ACL6表项：

```
DSP SECACL6TAB:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```
RETCODE = 0  操作成功.                                                                                                     
结果如下 
------------------------
      资源单元名称  =  VNODE_VNRS_VNFC_IPU_0064
  源IP地址是否有效  =  IP配置有效 
目的IP地址是否有效  =  IP配置有效
          源IP地址  =  2001:db8::1
        目的IP地址  =  2001:db8::5
      源IP地址掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
    目的IP地址掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
        源端口类型  =  范围
      目的端口类型  =  范围
          源端口号  =  0
        目的端口号  =  0
          协议类型  =  6
            优先级  =  17592186044576
      源端口起始值  =  20
      源端口终止值  =  50
    目的端口起始值  =  22
    目的端口终止值  =  52
          安全类型  =  允许
          策略类型  =  白名单策略
            策略ID  =  1
            规则ID  =  10
          下发标记  =  TRUE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SECACL6TAB.md`
