---
id: UNC@20.15.2@MMLCommand@SET NGMDTCTRL
type: MMLCommand
name: SET NGMDTCTRL（设置5G MDT控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGMDTCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G MDT管理
status: active
---

# SET NGMDTCTRL（设置5G MDT控制参数）

## 功能

**适用NF：AMF**

该命令用于设置5G MDT控制参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MNGMDTSW |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNGMDTSW | 基于管理的MDT开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定最小化路测（MDT）功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGMDTCTRL查询当前参数配置值。<br>配置原则：<br>当用户需要最小化路测（MDT）功能时，可以通过设置该参数为“ON”来开启该功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGMDTCTRL]] · 5G MDT控制参数（NGMDTCTRL）

## 使用实例

设置NGMDTCTRL参数，MNGMDTSW为ON，执行如下命令：

```
SET NGMDTCTRL: MNGMDTSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NGMDTCTRL.md`
