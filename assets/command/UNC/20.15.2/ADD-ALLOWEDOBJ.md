---
id: UNC@20.15.2@MMLCommand@ADD ALLOWEDOBJ
type: MMLCommand
name: ADD ALLOWEDOBJ（增加授权控制对象信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ALLOWEDOBJ
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 访问授权对象管理
status: active
---

# ADD ALLOWEDOBJ（增加授权控制对象信息）

## 功能

**适用NF：NRF**

该命令用于新增授权控制对象信息中的FQDN信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。该字段值需要全系统唯一，只能由字母（A-Z或者a-z）、数字（0-9）组成，不能以数字开始。<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制策略的NF对象的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ALLOWEDOBJ]] · 授权控制对象信息（ALLOWEDOBJ）

## 使用实例

运营商在NRF上配置对象名称为objname001，FQDN为huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org的NF的访问授权控制策略，通过下面命令添加此NF对象。

```
ADD ALLOWEDOBJNAME: OBJNAME="objname001";
ADD ALLOWEDOBJ:OBJNAME="objname001",FQDN="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ALLOWEDOBJ.md`
