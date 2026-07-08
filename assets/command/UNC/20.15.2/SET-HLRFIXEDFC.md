---
id: UNC@20.15.2@MMLCommand@SET HLRFIXEDFC
type: MMLCommand
name: SET HLRFIXEDFC（设置VLR向HLR发送请求的固定速率流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HLRFIXEDFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- VLR固定速率流控
status: active
---

# SET HLRFIXEDFC（设置VLR向HLR发送请求的固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于设置VLR向HLR发送请求的固定速率流控。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UPLOCFCSW | UPLOCFCRATE | RATELEVEL |
| --- | --- | --- |
| ON | 1000 | WholeSystem |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLOCFCSW | VLR向HLR发送位置更新请求的固定速率流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR向HLR发送位置更新请求的固定速率流控开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HLRFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| UPLOCFCRATE | VLR向HLR发送位置更新请求的固定速率的起控阈值(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR向HLR发送位置更新请求的固定速率的起控阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HLRFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| RATELEVEL | 阈值计算策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制“VLR向HLR发送位置更新请求的固定速率的起控阈值(个/秒)”的计算方式。<br>数据来源：本端规划<br>取值范围：<br>- WholeSystem（整系统）<br>- Process（进程）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HLRFIXEDFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HLRFIXEDFC]] · VLR向HLR发送请求的固定速率流控（HLRFIXEDFC）

## 使用实例

运营商希望将VLR向HLR发送位置更新请求的固定速率流控开关打开，设置VLR向HLR发送位置更新请求的固定速率的起控阈值为10000个/秒，阈值计算策略设置为整系统时，执行如下命令：

```
SET HLRFIXEDFC: UPLOCFCSW=ON, UPLOCFCRATE=10000, RATELEVEL=WholeSystem;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HLRFIXEDFC.md`
