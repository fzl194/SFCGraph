---
id: UNC@20.15.2@MMLCommand@LST QOSBA
type: MMLCommand
name: LST QOSBA（查询QoS BA）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSBA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- BA映射关系
status: active
---

# LST QOSBA（查询QoS BA）

## 功能

该命令用来查询当前域的上行IP报文的DSCP值或者上行VLAN报文的802.1p的值对应路由器内部的服务等级，还有相应的报文着色策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSNAME | DS域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定差分服务域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| BATYPE | ba类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定修改的差分服务域上行映射类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- 8021p：对入方向的VLAN报文8021p值进行修改。<br>- ip_dscp：对入方向的IP报文DSCP(差分服务码点)值进行修改。<br>- mpls_exp：对入方向的MPLS报文EXP(实验比特位)值进行修改。<br>默认值：无 |
| BAVALUE | ba值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要映射的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。802.1p的取值范围是0到7;DSCP值的范围是0到63。取值越大优先级越高。<br>默认值：无 |
| SERVICECLASS | 服务分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后的内部服务等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- be：尽力而为。<br>- af1：确保转发等级1。<br>- af2：确保转发等级2。<br>- af3：确保转发等级3。<br>- af4：确保转发等级4。<br>- ef：加速转发。<br>- cs6：类选择码6。<br>- cs7：类选择码7。<br>默认值：无 |
| COLOR | 颜色分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射后报文的着色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- green：报文颜色，绿色报文的丢弃优先级最低。<br>- yellow：报文颜色，黄色报文的丢弃优先级介于绿色红色之间。<br>- red：报文颜色，红色报文的丢弃优先级最高。<br>默认值：无 |

## 操作的配置对象

- [QoS BA（QOSBA）](configobject/UNC/20.15.2/QOSBA.md)

## 使用实例

查询DS域default的上行IP报文的DSCP值或上行VLAN报文的802.1p值对应路由器内部的服务等级与报文着色：

```
LST QOSBA:;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
DS域名    ba类型    ba值       服务分类    颜色分类
default   8021p     0          be          绿
default   8021p     1          be          红
default   8021p     2          af2         绿
default   8021p     3          af3         绿
default   8021p     4          af4         绿 
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS-BA（LST-QOSBA）_00441337.md`
