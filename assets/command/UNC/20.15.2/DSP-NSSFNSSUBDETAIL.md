---
id: UNC@20.15.2@MMLCommand@DSP NSSFNSSUBDETAIL
type: MMLCommand
name: DSP NSSFNSSUBDETAIL（显示切片可用性订阅详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFNSSUBDETAIL
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能参数配置
status: active
---

# DSP NSSFNSSUBDETAIL（显示切片可用性订阅详细信息）

## 功能

**适用NF：NSSF**

该命令用于显示切片可用性订阅详细信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 订阅标识 | 可选必选说明：必选参数<br>参数含义：该参数表示订阅标识，通过该参数指定需要查询的订阅，该参数可通过DSP NSSFNSSUBINFO命令获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由小写字母（a-z）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [切片可用性订阅详细信息（NSSFNSSUBDETAIL）](configobject/UNC/20.15.2/NSSFNSSUBDETAIL.md)

## 使用实例

运营商想要查询切片可用性订阅详细信息时，执行此命令。

```
DSP NSSFNSSUBDETAIL: SUBID="0004c7d76079f5a24517a4e03d90e484975c";
%%DSP NSSFNSSUBDETAIL: SUBID="0004c7d76079f5a24517a4e03d90e484975c";%%
RETCODE = 0  操作成功

结果如下
--------
订阅标识                              订阅通知URI                                                                           移动国家码  移动网号  跟踪区域码  AMF集合标识    过期时间              从本NSSF生成标识

0004c7d76079f5a24517a4e03d90e484975c  http://10.70.183.1:5160/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  460         03        290102      460-03-01-001  2021-05-11T07:10:25Z  TRUE
0004c7d76079f5a24517a4e03d90e484975c  http://10.70.183.2:5260/nnssf-nssaiavailability/v1/nssai-availability/subscriptions/  125         236       290102      460-03-01-001  2021-05-11T07:10:25Z  TRUE
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示切片可用性订阅详细信息（DSP-NSSFNSSUBDETAIL）_56547717.md`
