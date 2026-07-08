---
id: UNC@20.15.2@MMLCommand@SET NFMGMTTIMER
type: MMLCommand
name: SET NFMGMTTIMER（设置NF管理模块的定时器配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NFMGMTTIMER
command_category: 配置类
applicable_nf:
- NRF
- SMF
- AMF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF定时器管理
status: active
---

# SET NFMGMTTIMER（设置NF管理模块的定时器配置）

## 功能

**适用NF：NRF、SMF、AMF、NSSF、NCG、SMSF**

该命令用于设置NF管理模块的定时器配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| URIADDRAGING | URIADDRREFRESH | URIADDRSCAN |
| --- | --- | --- |
| 168 | 10 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URIADDRAGING | URI地址表老化周期 | 可选必选说明：可选参数<br>参数含义：该命令用于设置URI地址表的老化周期。老化周期内业务未进行查询的地址表将在老化周期后失效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是小时。该参数取值需大于URIADDRREFRESH参数的取值。如果该参数为最大值（65535），则地址表不会老化。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFMGMTTIMER查询当前参数配置值。<br>配置原则：无 |
| URIADDRREFRESH | URI地址表刷新间隔 | 可选必选说明：可选参数<br>参数含义：该命令用于设置URI地址表的老化时间戳刷新间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255，单位是小时。该参数取值必须小于URIADDRAGING的取值。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFMGMTTIMER查询当前参数配置值。<br>配置原则：无 |
| URIADDRSCAN | URI地址表扫描间隔 | 可选必选说明：可选参数<br>参数含义：该命令用于设置URI地址表扫描任务的间隔。此值越低，超出老化周期的地址记录就会越快老化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFMGMTTIMER查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFMGMTTIMER]] · NF管理模块的定时器配置（NFMGMTTIMER）

## 使用实例

运营商A需要设置URI地址表老化周期为1天，URI地址表刷新间隔为12小时，URI地址表扫描间隔为20分钟。

```
SET NFMGMTTIMER: URIADDRAGING=24, URIADDRREFRESH=12, URIADDRSCAN=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NFMGMTTIMER.md`
