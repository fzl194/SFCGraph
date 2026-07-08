---
id: UNC@20.15.2@MMLCommand@SET HTTPCCACONF
type: MMLCommand
name: SET HTTPCCACONF（设置HTTP CCA属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HTTPCCACONF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP CCA安全管理
status: active
---

# SET HTTPCCACONF（设置HTTP CCA属性）

## 功能

![](设置HTTP CCA属性（SET HTTPCCACONF）_54538297.assets/notice_3.0-zh-cn_2.png)

开启CCA校验以及修改CCA的有效时长，会影响消息的合法性校验结果，导致消息被丢弃。

该命令用于设置HTTP CCA属性，该属性设置后整系统生效。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCACHECKSW | CCAPERIOD |
| --- | --- |
| OFF | 86400 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCACHECKSW | CCA校验开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制HTTP服务端CCA校验功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPCCACONF查询当前参数配置值。<br>配置原则：无 |
| CCAPERIOD | CCA的有效时长(s) | 可选必选说明：可选参数<br>参数含义：该参数用于配置HTTP客户端生成的CCA的有效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~864000，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPCCACONF查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPCCACONF]] · HTTP CCA属性（HTTPCCACONF）

## 使用实例

如果HTTP服务端需要校验CCA，可以执行如下命令：

```
SET HTTPCCACONF: CCACHECKSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置HTTP-CCA属性（SET-HTTPCCACONF）_54538297.md`
