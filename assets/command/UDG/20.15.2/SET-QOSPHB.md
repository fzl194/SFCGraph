---
id: UDG@20.15.2@MMLCommand@SET QOSPHB
type: MMLCommand
name: SET QOSPHB（设置QoS PHB）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: QOSPHB
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- PHB映射关系
status: active
---

# SET QOSPHB（设置QoS PHB）

## 功能

当接口上使能简单流分类，并且报文在接口下行转发检查PHB时，可以使用该命令配置当前域的下行IP报文的服务等级和颜色映射成对应的DSCP值，或者下行VLAN报文在路由器内部的服务等级和报文颜色对应路由器外部的802.1p的值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSNAME | DS域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定差分服务域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD QOSDIFFERSERV命令配置DS域。 |
| PHBTYPE | PHB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定修改的差分服务域下行映射类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- 8021p：对出方向的VLAN报文8021p值进行修改。<br>- ip_dscp：对出方向的IP报文DSCP(差分服务码点)值进行修改。<br>- mpls_exp：对出方向的MPLS报文EXP(实验比特位)值进行修改。<br>默认值：无 |
| PHBVALUE | PHB值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要映射的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。802.1p的取值范围是0到7;DSCP值的范围是0到63。取值越大优先级越高。<br>默认值：无 |
| SERVICECLASS | 服务分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定映射前的内部服务等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- be：尽力而为。<br>- af1：确保转发等级1。<br>- af2：确保转发等级2。<br>- af3：确保转发等级3。<br>- af4：确保转发等级4。<br>- ef：加速转发。<br>- cs6：类选择码6。<br>- cs7：类选择码7。<br>默认值：无 |
| COLOR | 颜色分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定映射前报文的着色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- green：报文颜色，绿色报文的丢弃优先级最低。<br>- yellow：报文颜色，黄色报文的丢弃优先级介于绿色红色之间。<br>- red：报文颜色，红色报文的丢弃优先级最高。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSPHB]] · QoS PHB（QOSPHB）

## 关联任务

- [[UDG@20.15.2@Task@0-00069]]

## 使用实例

修改DS域default的路由器内部服务等级be，报文着色为green的下行VLAN报文，映射为外部优先级3：

```
SET QOSPHB:DSNAME="default",PHBTYPE=8021p,PHBVALUE=3,SERVICECLASS=be,COLOR=green;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置QoS-PHB（SET-QOSPHB）_00840685.md`
