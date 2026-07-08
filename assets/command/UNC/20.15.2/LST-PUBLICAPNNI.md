---
id: UNC@20.15.2@MMLCommand@LST PUBLICAPNNI
type: MMLCommand
name: LST PUBLICAPNNI（查询公共APN NI配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PUBLICAPNNI
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 公共APNNI管理
status: active
---

# LST PUBLICAPNNI（查询公共APN NI配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询定制公用APN NI(Access Point Name Network Identifier)的信息。公用APN NI信息在激活请求信息纠正功能时使用。

## 注意事项

- 该命令在用户下次查询定制公用APN NI配置信息时生效。
- 当不输入查询条件时，显示所有记录信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：可选参数<br>参数含义：待查询的APN网络标识。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [公共APN NI配置（PUBLICAPNNI）](configobject/UNC/20.15.2/PUBLICAPNNI.md)

## 使用实例

查询所有定制公用APNNI的信息：

LST PUBLICAPNNI:;

```
%%LST PUBLICAPNNI:;%%
RETCODE = 0  操作成功。

公用APNNI列表
---------------
 APN网络标识

 CMNET
 CMWAP 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询公共APN-NI配置(LST-PUBLICAPNNI)_26305492.md`
