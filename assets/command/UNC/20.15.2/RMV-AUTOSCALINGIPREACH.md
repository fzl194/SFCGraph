---
id: UNC@20.15.2@MMLCommand@RMV AUTOSCALINGIPREACH
type: MMLCommand
name: RMV AUTOSCALINGIPREACH（删除IP可达性检测自动化配置模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGIPREACH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- RU可达性检测自动化配置
status: active
---

# RMV AUTOSCALINGIPREACH（删除IP可达性检测自动化配置模板）

## 功能

该命令用于删除IP可达性检测自动化配置模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。该参数由ADD AUTOSCALINGSERVICE命令配置获得。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用来表示IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：无 |
| DESTADDR4 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示对端网关的IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTADDR6 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示对端网关的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AUTOSCALINGIPREACH]] · IP可达性检测自动化配置模板（AUTOSCALINGIPREACH）

## 使用实例

删除一个IP可达性检测自动化配置模板：

```
RMV AUTOSCALINGIPREACH: SERVICENAME="service1",IPVERSION=IPv4,DESTADDR4="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AUTOSCALINGIPREACH.md`
