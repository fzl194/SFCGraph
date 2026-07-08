---
id: UNC@20.15.2@MMLCommand@SET HTTPMEMFC
type: MMLCommand
name: SET HTTPMEMFC（设置HTTP内存流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HTTPMEMFC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP内存流控管理
status: active
---

# SET HTTPMEMFC（设置HTTP内存流控）

## 功能

设置HTTP Body内存分区的内存流控。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MEMFCSWITCH | MEMFCSTARTTHD | MEMFCSTOPTHD | MEMFCBIGPKTTHD |
| --- | --- | --- | --- |
| TRUE | 30 | 50 | 512 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEMFCSWITCH | 内存流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内存流控功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMEMFC查询当前参数配置值。<br>配置原则：无 |
| MEMFCSTARTTHD | 内存流控起控阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Body内存分区的内存流控起控阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~512，单位是兆字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMEMFC查询当前参数配置值。<br>配置原则：<br>小于Body内存分区的内存流控停控阈值。 |
| MEMFCSTOPTHD | 内存流控停控阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Body内存分区的内存流控停控阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~512，单位是兆字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMEMFC查询当前参数配置值。<br>配置原则：<br>大于Body内存分区的内存流控起控阈值。 |
| MEMFCBIGPKTTHD | 内存流控大包阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Body内存分区的内存流控大包阈值，即超过该阈值的报文，参与内存流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~16384，单位是千字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPMEMFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPMEMFC]] · HTTP内存流控（HTTPMEMFC）

## 使用实例

如果要把内存流控功能关闭，可以执行如下命令：

```
SET HTTPMEMFC: MEMFCSWITCH=FALSE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置HTTP内存流控（SET-HTTPMEMFC）_01384198.md`
