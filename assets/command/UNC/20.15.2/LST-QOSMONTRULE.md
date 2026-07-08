---
id: UNC@20.15.2@MMLCommand@LST QOSMONTRULE
type: MMLCommand
name: LST QOSMONTRULE（查询QoS监测规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSMONTRULE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- QoS监测管理
- QoS监测规则管理
status: active
---

# LST QOSMONTRULE（查询QoS监测规则）

## 功能

**适用NF：SMF**

该命令用于查询QoS监测规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHMODE | 匹配类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指示匹配类型。<br>数据来源：本端规划<br>取值范围：<br>- MSISDN（MSISDN）<br>- IMSI（IMSI）<br>- MULTIPARA（多参数）<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"MATCHMODE"配置为"IMSI"时为条件可选参数。<br>参数含义：该参数用于指定IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"MATCHMODE"配置为"MSISDN"时为条件可选参数。<br>参数含义：该参数用于指定MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定切片业务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定切片细分标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| ARP | ARP数值 | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定ARP。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：无 |
| FIVEQI | 5QI | 可选必选说明：该参数在"MATCHMODE"配置为"MULTIPARA"时为条件可选参数。<br>参数含义：该参数用于指定5QI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSMONTRULE]] · QoS监测规则（QOSMONTRULE）

## 使用实例

查询“IMSI”为“123030123456789”的QoS监测功能配置：

```
%%LST QOSMONTRULE:MATCHMODE=IMSI,IMSI="123030123456789";%%
RETCODE = 0  操作成功

结果如下
--------
              IMSI  =  123030123456789
       QoS监测开关  =  不使能
      时延监测方向  =  往返监测
          上报频率  =  会话释放触发
下行时延阈值(毫秒)  =  NULL
上行时延阈值(毫秒)  =  NULL
往返时延阈值(毫秒)  =  NULL
等待最小值时间(秒)  =  NULL
      测量周期(秒)  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSMONTRULE.md`
