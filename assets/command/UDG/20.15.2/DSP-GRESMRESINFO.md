---
id: UDG@20.15.2@MMLCommand@DSP GRESMRESINFO
type: MMLCommand
name: DSP GRESMRESINFO（显示Gresm资源信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GRESMRESINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Gresm调测
status: active
---

# DSP GRESMRESINFO（显示Gresm资源信息）

## 功能

该命令用于显示本设备上APP使用的Gresm资源信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPPID | APP ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示APP ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示资源类型包括label、iid。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- label：标签。<br>- iid：直连ID。<br>- DPOOL：资源池。<br>- SLABEL：静态标签。<br>- BLABEL：块标签。<br>默认值：无 |
| RESSTATUS | 资源状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示资源状态包括normal、once-error、twice-error。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- normal：Normal。<br>- once-error：一次错误。<br>- twice-error：两次错误。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GRESMRESINFO]] · Gresm资源信息（GRESMRESINFO）

## 使用实例

显示指定的APP资源使用信息：

```
DSP GRESMRESINFO:APPPID="6F4655", RESTYPE=iid, RESSTATUS=normal;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
APP ID      资源类型    资源状态    资源ID

0x6f4655    直连ID      Normal      7
0x6f4655    直连ID      Normal      92
0x6f4655    直连ID      Normal      91
0x6f4655    直连ID      Normal      90
0x6f4655    直连ID      Normal      89
0x6f4655    直连ID      Normal      88
0x6f4655    直连ID      Normal      87
0x6f4655    直连ID      Normal      86
0x6f4655    直连ID      Normal      85
0x6f4655    直连ID      Normal      84
0x6f4655    直连ID      Normal      45
0x6f4655    直连ID      Normal      43
0x6f4655    直连ID      Normal      12
0x6f4655    直连ID      Normal      11
0x6f4655    直连ID      Normal      10
0x6f4655    直连ID      Normal      9
0x6f4655    直连ID      Normal      8
(结果个数 = 17)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-GRESMRESINFO.md`
