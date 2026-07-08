---
id: UNC@20.15.2@MMLCommand@SET N16ASMFDATACHK
type: MMLCommand
name: SET N16ASMFDATACHK（设置N16aSMF数据核查开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N16ASMFDATACHK
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- N16aSMF数据核查管理
status: active
---

# SET N16ASMFDATACHK（设置N16aSMF数据核查开关）

## 功能

![](设置N16aSMF数据核查开关（SET N16ASMFDATACHK）_13939901.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，开启数据核查开关，当校验不通过时，可能会导致会话异常去活。

**适用NF：SMF**

该命令用于修改N16aSMF数据核查功能，如是否支持基于UserAgent进行数据核查。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| USERAGENTCHK |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERAGENTCHK | UserAgent检查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示N16aSMF基于user agent信息检查的功能开关。当该开关打开时，N16aSMF作为服务端收到来自I-SMF发送的消息，且当消息中的http head中携带user agent时，根据user agent携带的客户端网元的Instance ID进行检查，如果该Instance ID与本地上下文中保存I-SMF的不一致，则给左侧回复404，反之不做额外处理。当该开关关闭时，N16aSMF不对user agent中信息进行检查。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N16ASMFDATACHK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N16ASMFDATACHK]] · N16aSMF数据核查功能（N16ASMFDATACHK）

## 使用实例

如N16aSMF作为服务端，需要基于UserAgent来检查I-SMF发送的消息，来识别哪些会话时多余或者无效的，可设置USERAGENTCHK为ON。

```
SET N16ASMFDATACHK: USERAGENTCHK = ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-N16ASMFDATACHK.md`
