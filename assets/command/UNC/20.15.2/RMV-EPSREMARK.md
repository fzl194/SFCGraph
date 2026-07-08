---
id: UNC@20.15.2@MMLCommand@RMV EPSREMARK
type: MMLCommand
name: RMV EPSREMARK（删除EPS QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPSREMARK
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- EPS Qos映射ToS_DSCP
status: active
---

# RMV EPSREMARK（删除EPS QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来恢复在SAE架构下，QoS参数到IP DSCP（区别服务编码点）/TOS（服务类型）的映射配置。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数指定QoS Profile的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功，可以通过LST QOSPROFILE或LST QOSGLOBAL命令查询。 |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：该参数表示QoS流量级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数表示ARP的优先级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：<br>- 0：General，通用用户。如果某业务级别各个优先级的用户都没有配置DSCP，则用General配置的值。<br>- 1~15：用户的优先级，其中1的优先级最高。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSREMARK]] · EPS QoS到TOS/DSCP的映射规则（EPSREMARK）

## 使用实例

删除Qos Profile名称为“qosprofile1”，QCI为“1”，ARP Priority Level为“15”的配置实例：

```
RMV EPSREMARK: QOSPROFILENAME="qosprofile1", QCI=1, ARPPL=15;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EPSREMARK.md`
