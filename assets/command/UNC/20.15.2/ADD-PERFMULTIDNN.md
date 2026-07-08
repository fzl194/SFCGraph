---
id: UNC@20.15.2@MMLCommand@ADD PERFMULTIDNN
type: MMLCommand
name: ADD PERFMULTIDNN（增加MultiDNN性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFMULTIDNN
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# ADD PERFMULTIDNN（增加MultiDNN性能统计对象）

## 功能

**适用NF：SMF、PGW-C**

该命令用于增加MultiDNN性能统计对象。当需要对指定MultiDNN园区的会话进行性能统计时使用该命令，MultiDNN园区由该命令中的数据网络名称，切片业务类型和切片细分标识唯一确定。

## 注意事项

- 该命令执行后立即生效。

- 网络切片已支持的DNN（ADD NSDNN配置，且DNN参数含有“multi”字段）会自动添加到PERFMULTIDNN中，不需要人工配置。执行ADD PERFMULTIDNN命令时只能配置ADD NSDNN命令没有配置过的含有“multi”字段的DNN。若PERFMULTIDNN记录数已达到最大规格，则随后执行ADD NSDNN命令添加的新切片信息不会再自动同步到PERFMULTIDNN中。

- 最多可输入3000条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DNN | SST | SD |
| --- | --- | --- |
| basicdnn | 1 | FFFFFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：必选参数<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：必选参数<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [MultiDNN性能统计对象（PERFMULTIDNN）](configobject/UNC/20.15.2/PERFMULTIDNN.md)

## 使用实例

当运营商希望增加一个MultiDNN配置记录，其中DNN为“huawei.com”，SST为1，SD为“010101”作为性能指标对象时，执行如下命令：

```
ADD PERFMULTIDNN: DNN="huawei.com", SST=1, SD="010101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MultiDNN性能统计对象（ADD-PERFMULTIDNN）_81671277.md`
