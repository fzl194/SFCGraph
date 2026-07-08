---
id: UDG@20.15.2@MMLCommand@SET CERTUPDATPARA
type: MMLCommand
name: SET CERTUPDATPARA（设置证书更新流程参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CERTUPDATPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书更新流程参数管理
status: active
---

# SET CERTUPDATPARA（设置证书更新流程参数）

## 功能

该命令用于证书开关打开时设置证书更新流程的相关参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | PROINTERVAL | PROLINKNUM | ACTIVEOLDLINK | CLIFAULTLINKNUM |
> | --- | --- | --- | --- |
> | 4 | 10 | TRUE | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROINTERVAL | 单进程每批次重建链路间隔(s) | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下激活设备证书，每个进程每批次重建链路的间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是4~500，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CERTUPDATPARA查询当前参数配置值。<br>配置原则：无 |
| PROLINKNUM | 单进程每批次重建链路数 | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下激活设备证书，每个进程每批次重建链路数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~500，单位是条。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CERTUPDATPARA查询当前参数配置值。<br>配置原则：无 |
| ACTIVEOLDLINK | 证书更新时是否重建旧链路 | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下激活设备证书，是否重新建链。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CERTUPDATPARA查询当前参数配置值。<br>配置原则：无 |
| CLIFAULTLINKNUM | 单证书场景单进程客户端链路允许不更新的数量 | 可选必选说明：可选参数<br>参数含义：该参数用于控制证书开关打开的场景下激活设备证书，每个证书场景在每个进程上，客户端链路更新时允许更新失败的链路数，小于该值时，更新流程继续，超过该值后，更新流程会失败。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是条。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CERTUPDATPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CERTUPDATPARA]] · 证书更新流程参数（CERTUPDATPARA）

## 使用实例

如果要在更新证书时重建已经建立好的链路，可以执行如下命令：

```
SET CERTUPDATPARA: ACTIVEOLDLINK=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CERTUPDATPARA.md`
