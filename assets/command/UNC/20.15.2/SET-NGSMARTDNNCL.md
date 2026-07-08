---
id: UNC@20.15.2@MMLCommand@SET NGSMARTDNNCL
type: MMLCommand
name: SET NGSMARTDNNCL（设置智能分流功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGSMARTDNNCL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN智能分流管理
- 智能分流功能管理
status: active
---

# SET NGSMARTDNNCL（设置智能分流功能）

## 功能

**适用NF：AMF**

该命令用于设置智能分流功能参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMARTCLSW |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMARTCLSW | 智能分流开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置系统智能分流开关。<br>当该参数设置为"ON"时，系统会根据用户签约和本地配置，判断用户是否是智能分流用户。如果用户是智能分流用户并且PDU会话建立时的请求DNN开启了智能分流功能，该会话将选择专用锚点SMF。<br>当该参数设置为“OFF”时，系统不区分智能分流用户和普通用户，执行通用SMF选择策略。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGSMARTDNNCL查询当前参数配置值。<br>配置原则：无 |
| DNNKEY | DNN智能分流关键字 | 可选必选说明：该参数在"SMARTCLSW"配置为"ON"时为条件必选参数。<br>参数含义：该参数用于设置智能分流DNN关键字，当用户签约DNN包含该关键字时，用户被标识为智能分流用户。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGSMARTDNNCL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGSMARTDNNCL]] · 智能分流功能（NGSMARTDNNCL）

## 使用实例

启用智能分流功能，关键字设置为"multidomain"，执行如下命令：

```
SET NGSMARTDNNCL: SMARTCLSW=ON, DNNKEY="multidomain";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGSMARTDNNCL.md`
