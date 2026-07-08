---
id: UNC@20.15.2@MMLCommand@LST NONRAI
type: MMLCommand
name: LST NONRAI（查询非广播RAI配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NONRAI
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- POOL区非广播RAI配置
status: active
---

# LST NONRAI（查询非广播RAI配置信息）

## 功能

**适用网元：SGSN**

此命令用于查询非广播RAI配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NONRAI | 路由区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定非广播路由区标识。用于在迁移的时候，目的SGSN来识别MS是从哪个SGSN迁移过来的。一个非广播路由区标识可以唯一地标志一个SGSN。<br>取值范围：长度必须为11或者12位，前5或6位为十进制数，后6位为十六进制数的字符串<br>默认值：无<br>说明：NONRAI = LAI + RAC。LAI = MCC + MNC + LAC。MCC由3个阿拉伯数字组成，MNC由2到3个阿拉伯数字组成，LAC是十六进制数，占2个字节。RAC是十六进制数，占1个字节。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NONRAI]] · 非广播RAI配置信息（NONRAI）

## 使用实例

查询所有非广播RAI记录信息：

LST NONRAI:;

```
%%LST NONRAI:;%%
RETCODE = 0  执行成功。

NONRAI信息
----------
路由区标识    IP类型  SGSN IPv4信令面地址   SGSN名称
123006666666  IPv4    192.168.111.111       sgsn1
12300233C01   IPv4    192.168.3.33          noname
12300010101   IPv4    192.168.222.222       noname
111111111111  IPv4    192.168.120.99        testsgsn
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NONRAI.md`
