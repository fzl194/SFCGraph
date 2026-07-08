---
id: UNC@20.15.2@MMLCommand@RMV ALLOWEDDOMAINS
type: MMLCommand
name: RMV ALLOWEDDOMAINS（删除允许访问的域名）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALLOWEDDOMAINS
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
- NF域名访问授权控制
status: active
---

# RMV ALLOWEDDOMAINS（删除允许访问的域名）

## 功能

**适用NF：NRF**

该命令用于删除指定NF对象允许访问的FQDN。

当某个NF不再通过NRF限制特定域名的NF访问，可以通过此命令删除允许访问的NF域名。

## 注意事项

- 该命令执行后并不会立即生效，需要执行CMT ALLOWPLCY命令后生效。

- 当所有允许访问属性被删除后，表示针对此对象在NRF上的设置是可以被任何NF域名的NF实例访问。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称，该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| ALLOWEDFQDN | 允许访问该对象的FQDN | 可选必选说明：必选参数<br>参数含义：该参数表示指定的NF对象所允许访问的FQDN，该参数可以通过DSP REGNFINSTANCE命令获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [允许访问的域名（ALLOWEDDOMAINS）](configobject/UNC/20.15.2/ALLOWEDDOMAINS.md)

## 使用实例

授权对象objname001可以被多个FQDN访问，其中包含：huawei1.com.apn.epc.mnc45.mcc123.3gppnetwork.org。运营商根据需要，不允许FQDN为huawei1.com.apn.epc.mnc45.mcc123.3gppnetwork.org的NF继续访问objname1时，执行下面命令：

```
RMV ALLOWEDDOMAINS:OBJNAME="objname001",ALLOWEDFQDN="huawei1.com.apn.epc.mnc45.mcc123.3gppnetwork.org";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的域名（RMV-ALLOWEDDOMAINS）_09654367.md`
