---
id: UNC@20.15.2@MMLCommand@SET RCFIXEDFC
type: MMLCommand
name: SET RCFIXEDFC（设置注册中心固定速率流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RCFIXEDFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSF固定速率流控
status: active
---

# SET RCFIXEDFC（设置注册中心固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF/VLR向注册中心发送请求的固定速率流控。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| REGFCSW | QRYFCSW | REGFCRATE | QRYFCRATE | RATELEVEL |
| --- | --- | --- | --- | --- |
| ON | ON | 1000 | 1000 | WholeSystem |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REGFCSW | SMSF/VLR向注册中心发送注册请求的固定速率流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF/VLR向注册中心发送注册请求的固定速率流控开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RCFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| QRYFCSW | SMSF/VLR向注册中心发送查询请求的固定速率流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF/VLR向注册中心发送查询请求的固定速率流控开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RCFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| REGFCRATE | SMSF/VLR向注册中心发送注册请求的固定速率流控的起控阈值(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF/VLR向注册中心发送注册请求的固定速率流控的起控阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RCFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| QRYFCRATE | SMSF/VLR向注册中心发送查询请求的固定速率流控的起控阈值(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF/VLR向注册中心发送查询请求的固定速率流控的起控阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RCFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| RATELEVEL | 阈值计算策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制“SMSF/VLR向注册中心发送注册请求的固定速率流控的起控阈值(个/秒)”和“SMSF/VLR向注册中心发送查询请求的固定速率流控的起控阈值(个/秒)”的计算策略。<br>数据来源：本端规划<br>取值范围：<br>- WholeSystem（整系统）<br>- Process（进程）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RCFIXEDFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RCFIXEDFC]] · 注册中心固定速率流控（RCFIXEDFC）

## 使用实例

运营商希望将SMSF/VLR向注册中心发送注册请求的固定速率流控开关打开，SMSF/VLR向注册中心发送查询请求的固定速率流控开关打开，SMSF/VLR向注册中心发送注册请求的固定速率流控的起控阈值设置为10000个/秒，SMSF/VLR向注册中心发送查询请求的固定速率流控的起控阈值设置为10000个/秒，阈值计算策略设置为整系统时，执行如下命令：

```
SET RCFIXEDFC: REGFCSW=ON, QRYFCSW=ON, REGFCRATE=10000, QRYFCRATE=10000, RATELEVEL=WholeSystem;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RCFIXEDFC.md`
