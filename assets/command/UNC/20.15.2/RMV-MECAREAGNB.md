---
id: UNC@20.15.2@MMLCommand@RMV MECAREAGNB
type: MMLCommand
name: RMV MECAREAGNB（删除5G MEC gNodeB信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MECAREAGNB
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 本地特色业务区域管理
- 本地特色业务区域gNodeB成员管理
status: active
---

# RMV MECAREAGNB（删除5G MEC gNodeB信息）

## 功能

**适用NF：AMF**

该命令用于删除5G MEC gNodeB成员。

## 注意事项

下一次移动性流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于表示移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于表示移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GNBIDBEGIN | gNodeB起始标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示gNodeB标识起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>不同记录间的gNodeB ID区间不允许存在重叠。 |
| GNBIDEND | gNodeB结束标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示gNodeB标识结束值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。本参数表示的gNodeB标识不能小于“gNodeB起始标识”。<br>默认值：无<br>配置原则：<br>可以通过DSP NGAPLINK获取gNodeB标识。 |
| GNBIDLEN | gNodeB标识长度 | 可选必选说明：必选参数<br>参数含义：该参数用于指定gNodeB标识的长度（比特位数）。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G MEC gNodeB信息（MECAREAGNB）](configobject/UNC/20.15.2/MECAREAGNB.md)

## 使用实例

删除标识为“1”区域的gNodeB（MCC="123", MNC="45", GNBIDBEGIN="123456", GNBIDEND="123456", GNBIDLEN="24"）成员，执行如下命令：

```
RMV MECAREAGNB:MCC="123",MNC="45",GNBIDBEGIN=123456,GNBIDEND=123456,GNBIDLEN=24;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-MEC-gNodeB信息（RMV-MECAREAGNB）_85251941.md`
