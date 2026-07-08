---
id: UNC@20.15.2@MMLCommand@ADD ALLOWSERNAME
type: MMLCommand
name: ADD ALLOWSERNAME（增加基于地址的白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ALLOWSERNAME
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于地址的白名单管理
status: active
---

# ADD ALLOWSERNAME（增加基于地址的白名单）

## 功能

该命令用于增加基于IP地址过滤的允许访问的服务白名单，当系统作为服务端时，添加到白名单中的指定IP地址的服务，只允许白名单中指定的对端地址的服务访问。未添加到白名单的服务则允许所有对端访问。

## 注意事项

- 该命令执行后立即生效。

- 如果配置了该白名单，白名单中的服务不允许白名单以外的NF的业务访问。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加到白名单的服务的NF实例标识。目前本参数不生效。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加到白名单中的服务的服务名称，由3GPP标准协议29510定义。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| LOCALADDR | 本端地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定添加到白名单的服务的服务地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PEERADDR | 对端地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定允许访问白名单中的服务的对端地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于地址的白名单（ALLOWSERNAME）](configobject/UNC/20.15.2/ALLOWSERNAME.md)

## 使用实例

添加标识为SMF_Instance_0的NF实例的服务类型为nsmf-event-exposure且本端地址为192.168.0.1的服务，仅允许对端地址为192.168.0.2的服务访问，则执行如下命令：

```
ADD ALLOWSERNAME: INDEX=0, NFINSTANCEID="SMF_Instance_0", SERVICENAME="nsmf-event-exposure", LOCALADDR="192.168.0.1", PEERADDR="192.168.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于地址的白名单（ADD-ALLOWSERNAME）_83813626.md`
