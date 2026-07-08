---
id: UNC@20.15.2@MMLCommand@SET PSEUDONYPOLICY
type: MMLCommand
name: SET PSEUDONYPOLICY（设置CHR假名化本地策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PSEUDONYPOLICY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SGSN
- MME
- SGW-C
- PGW-C
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 软件参数管理
- 假名化策略
status: active
---

# SET PSEUDONYPOLICY（设置CHR假名化本地策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SGSN、MME、SGW-C、PGW-C、NCG、SMSF**

该命令用于设置CHR假名化本地策略，UNC的CHR假名化功能可以通过该命令配置本地策略，也可以通过网管集中配置。当UNC未连接网管，或已连接网管但网管上未进行假名化功能设置时，根据该命令配置判断是否做CHR假名化处理。当UNC已连接网管且网管上已有假名化功能配置时，根据网管上配置的假名化功能状态判断是否做CHR假名化处理。

## 注意事项

- 该命令执行后立即生效。

- CHR假名化本地策略中，口令必须由大写字母、小写字母、数字和特殊字符（`~!@#$%^&*()-_=+\|[{}];:'",<.>/）组成，且至少包含其中的两项。口令最小20位，最大36位。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOCALPOLICY |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALPOLICY | CHR假名化本地策略开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置CHR假名化本地策略是否开启。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。<br>配置原则：无 |
| KEY | CHR假名化本地策略口令 | 可选必选说明：该参数在"LOCALPOLICY"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于设置CHR假名化本地策略的口令，口令用于生成密钥并进行加密。<br>数据来源：本端规划<br>取值范围：Pwd，取值范围是20~36。口令必须由大写字母、小写字母、数字和特殊字符（`~!@#$%^&*()-_=+\\|[{}];:'",<.>/）组成，且至少包含其中的两项。口令最小20位，最大36位。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PSEUDONYPOLICY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [CHR假名化本地策略（PSEUDONYPOLICY）](configobject/UNC/20.15.2/PSEUDONYPOLICY.md)

## 使用实例

如果要把CHR假名化本地策略开关打开，可以执行如下命令：

```
SET PSEUDONYPOLICY: LOCALPOLICY=ON, KEY="*****";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置CHR假名化本地策略（SET-PSEUDONYPOLICY）_51175645.md`
