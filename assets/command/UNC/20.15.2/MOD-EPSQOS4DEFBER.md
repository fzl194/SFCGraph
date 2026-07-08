---
id: UNC@20.15.2@MMLCommand@MOD EPSQOS4DEFBER
type: MMLCommand
name: MOD EPSQOS4DEFBER（修改Qos Profile缺省承载QoS属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EPSQOS4DEFBER
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 缺省承载的EPS QoS
status: active
---

# MOD EPSQOS4DEFBER（修改Qos Profile缺省承载QoS属性）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来修改Qos Profile缺省承载QoS属性。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | Qos Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用来指定Qos Profile名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD QOSPROFILE命令配置生成。 |
| QCI | QCI值 | 可选必选说明：必选参数<br>参数含义：该参数用来指定QCI。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是5~255。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数用来指定ARP的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| AMBRDL | 下行APN AMBR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用来指定下行集合比特率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~2000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| AMBRUL | 上行APN AMBR(千比特/秒) | 可选必选说明：必选参数<br>参数含义：该参数用来指定上行集合比特率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~2000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSQOS4DEFBER]] · Qos Profile缺省承载QoS属性（EPSQOS4DEFBER）

## 使用实例

修改QosProfileName为“test”的缺省承载Qos属性：

```
MOD EPSQOS4DEFBER: QOSPROFILENAME="test", QCI=7, ARPPL=12, AMBRDL=2000, AMBRUL=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-EPSQOS4DEFBER.md`
