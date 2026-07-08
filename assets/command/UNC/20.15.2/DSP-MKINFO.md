---
id: UNC@20.15.2@MMLCommand@DSP MKINFO
type: MMLCommand
name: DSP MKINFO（查询主密钥信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MKINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 主密钥管理
status: active
---

# DSP MKINFO（查询主密钥信息）

## 功能

该命令用于显示主控上主密钥信息，包含主密钥ID，状态，个数，初始化时间和过期时间。当系统上报主密钥异常告警时，可以执行该命令查看主密钥信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MASTERORSLAVE | 主备OMU标识 | 可选必选说明：可选参数<br>参数含义：表示HA角色，“主”表示主OMU，“备”表示备OMU。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主主控。<br>- SLAVE：备主控。<br>默认值：MASTER |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MKINFO]] · 主密钥信息（MKINFO）

## 使用实例

查询主密钥信息：

```
DSP MKINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
主密钥域ID    激活的主密钥ID    主密钥状态    主密钥个数    主密钥初始化时间       主密钥过期时间     
2             2                 正常          2             2019-07-13 07:43:38    2039-07-13 07:43:38
3             2                 正常          2             2019-07-13 07:43:38    2039-07-13 07:43:38
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MKINFO.md`
