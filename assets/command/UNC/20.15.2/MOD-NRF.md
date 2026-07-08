---
id: UNC@20.15.2@MMLCommand@MOD NRF
type: MMLCommand
name: MOD NRF（修改NRF信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRF
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF配置管理
- NRF实例配置管理
status: active
---

# MOD NRF（修改NRF信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于在NF（可以是NRF）上修改需要对接的对端NRF实例信息。

## 注意事项

- 该命令执行后立即生效。

- TLS参数仅代表NRF是否支持TLS，如需开启SBI接口加密特性，还需要执行其它相关配置操作，详细信息请参考WSFD-010308 SBI接口加密 > 激活SBI接口加密特性。
- 本端NF为NRF时参数CAPACITY暂不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>- 本参数的构成字符只能是字母A～Z或a～z、数字0～9和下划线"_"和中划线"-"，例如，NRF_Instance_0。<br>- 不允许配置前18位字符与数据库中所有存储的非UUID格式的NRFINSTANCENAME的相同记录。 |
| TLS | TLS | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRF是否支持TLS(Transport Layer Security)。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRF的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| CAPACITY | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRF的权重。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。值越大表示容量越大。<br>默认值：无<br>配置原则：无 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRF的域名，为后续NRF使用FQDN对接做准备。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRF]] · 测试服务发现的NF信息（NRF）

## 使用实例

修改名称为NRF_Instance_0的NRF的信息，支持TLS。

```
MOD NRF: NRFINSTANCENAME="NRF_Instance_0", TLS=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NRF信息（MOD-NRF）_09652605.md`
