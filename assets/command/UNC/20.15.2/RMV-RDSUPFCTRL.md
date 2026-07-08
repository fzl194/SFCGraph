---
id: UNC@20.15.2@MMLCommand@RMV RDSUPFCTRL
type: MMLCommand
name: RMV RDSUPFCTRL（删除RADIUS服务器的UP列表中指定UP的功能属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RDSUPFCTRL
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- RADIUS UPF控制
status: active
---

# RMV RDSUPFCTRL（删除RADIUS服务器的UP列表中指定UP的功能属性）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用来删除RADIUS服务器使用的UP列表中指定UPF的功能属性。

## 注意事项

- 该命令执行后立即生效。

- 会在下一次二次鉴权RADIUS中转UPF会话创建时生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。该参数需要是UPLIST4RDS配置中已添加的UPLISTNAME的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数取值需要是UPLIST4RDS配置中已添加的UPINSTANCEID的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |

## 操作的配置对象

- [RADIUS服务器的UP列表中指定UP的功能属性（RDSUPFCTRL）](configobject/UNC/20.15.2/RDSUPFCTRL.md)

## 使用实例

删除UP列表名为“uplist1”，UP名为“up1”的配置记录：

```
RMV UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除RADIUS服务器的UP列表中指定UP的功能属性（RMV-RDSUPFCTRL）_82242449.md`
