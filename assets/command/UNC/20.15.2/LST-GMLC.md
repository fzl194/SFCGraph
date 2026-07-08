---
id: UNC@20.15.2@MMLCommand@LST GMLC
type: MMLCommand
name: LST GMLC（查询GMLC配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMLC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC配置
status: active
---

# LST GMLC（查询GMLC配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查询GMLC配置。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的GMLC标识。<br>取值范围：0～639<br>默认值 ：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GMLC]] · GMLC配置（GMLC）

## 使用实例

查询GMLC参数设置：

LST GMLC:;

```
%%LST GMLC:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 GMLC 标识  GMLC IP地址类型  GMLC IP地址  GMLC 号码        GMLC 主机名                                GMLC所属MCC  GMLC所属MNC    接口类型      支持定位信息

 1          IPv4             10.10.10.15  861390123456789  example.com                                 123          01             Lg            E-UTRAN Cell Identifier & Cell Portion ID & Civic Address & Barometric Pressure & Velocity Estimate & Additional Positioning Data
 2          IPv4             10.10.10.16  861390123456780  example.com                                123          01             SLg           E-UTRAN Cell Identifier & Cell Portion ID & Civic Address & Barometric Pressure & Velocity Estimate & Additional Positioning Data
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GMLC.md`
