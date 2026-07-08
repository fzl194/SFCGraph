---
id: UNC@20.15.2@MMLCommand@STR RESELECTAUSF
type: MMLCommand
name: STR RESELECTAUSF（启动重选AUSF）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: RESELECTAUSF
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G网络管理
- AUSF重选管理
status: active
---

# STR RESELECTAUSF（启动重选AUSF）

## 功能

**适用NF：AMF**

该命令用于触发AUSF重选流程。AMF收到该命令后会启动扫描任务，对符合重选条件的用户在后续需要鉴权的流程中重选AUSF并进行鉴权。

该命令适用于特定的AUSF发生故障或升级等场景下，AMF通过本命令触发AUSF重选功能。

## 注意事项

- 该命令执行后立即生效。

- 扫描速率受SET AMFAUSFRESET命令中的“RATE”参数控制。
- 扫描时长 = 5G用户数 / 扫描速率。其中，5G用户数可以通过DSP NGUSERNUM获取；扫描速率可以通过LST AMFAUSFRESET中的扫描速率获取。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUSFID | AUSF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要重选的AUSF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。AUSF Instance ID使用UUID格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESELECTAUSF]] · 重选AUSF（RESELECTAUSF）

## 使用实例

由于网络调整，A地数据中心的AUSF1上的业务需要其它的AUSF接管，为了配合该调整，需要手动执行如下命令，将AMF上原本在AUSF1上的鉴权用户重选到其他的AUSF。

```
STR RESELECTAUSF:AUSFID="AUSF1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动重选AUSF（STR-RESELECTAUSF）_96766645.md`
