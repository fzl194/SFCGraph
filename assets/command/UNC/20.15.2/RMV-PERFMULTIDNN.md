---
id: UNC@20.15.2@MMLCommand@RMV PERFMULTIDNN
type: MMLCommand
name: RMV PERFMULTIDNN（删除MultiDNN性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFMULTIDNN
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFMULTIDNN（删除MultiDNN性能统计对象）

## 功能

![](删除MultiDNN性能统计对象（RMV PERFMULTIDNN）_31551070.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除MultiDNN性能统计对象会导致相应MultiDNN园区性能统计信息无法上报。

**适用NF：SMF、PGW-C**

该命令用于删除MultiDNN性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- 若执行RMV PERFMULTIDNN失败，提示信息为“默认配置不可删除”，则该条PERFMULTIDNN为ADD NSDNN同步的配置。执行RMV NSDNN则会自动同步删除该条PERFMULTIDNN。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：必选参数<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：必选参数<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFMULTIDNN]] · MultiDNN性能统计对象（PERFMULTIDNN）

## 使用实例

当运营商希望删除一个MultiDNN配置记录，其中DNN为“huawei.com”，SST为1，SD为“010101”作为性能指标对象时，执行如下命令：

```
RMV PERFMULTIDNN: DNN="huawei.com", SST=1, SD="010101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFMULTIDNN.md`
